"""Extract curated PNG outputs from Jupyter notebooks into docs/images/."""
from __future__ import annotations

import base64
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "docs" / "images"

# Curated exports for README (notebook, output label -> filename)
CURATED = {
    "notebooks/01_svr_stock_prediction.ipynb": {
        "svr_aapl_prediction.png": lambda labels: _pick(labels, ["rmse_1.58", "aapl"], 0),
        "svr_goog_generalization.png": lambda labels: _pick(labels, ["goog_rmse_1.45", "goog"], 4),
        "svr_nvda_generalization.png": lambda labels: _pick(labels, ["nvda_rmse_1.18", "nvda"], 5),
    },
    "notebooks/02_xgboost_stock_prediction.ipynb": {
        "xgboost_aapl_prediction.png": lambda labels: labels[0] if labels else None,
    },
    "notebooks/03_lstm_stock_prediction.ipynb": {
        "lstm_aapl_training.png": lambda labels: labels[0] if labels else None,
        "lstm_forecast.png": lambda labels: labels[-1] if labels else None,
    },
}


def _pick(labels: list[str], preferred: list[str], index: int) -> str | None:
    for key in preferred:
        for lab in labels:
            if key in lab:
                return lab
    return labels[index] if index < len(labels) else (labels[0] if labels else None)


def label_for_image(recent_text: str) -> str:
    m = re.findall(r"([A-Z]{2,5})\s+RMSE:\s*([\d.]+)", recent_text)
    if m:
        ticker, val = m[-1]
        return f"{ticker.lower()}_rmse_{val}"
    m = re.search(r"RMSE:\s*([\d.]+)", recent_text)
    if m:
        return f"rmse_{m.group(1)}"
    return "plot"


def collect_images(nb_path: Path) -> dict[str, bytes]:
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    images: dict[str, bytes] = {}
    recent_text = ""
    counters: dict[str, int] = {}

    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        for out in cell.get("outputs", []):
            if out.get("output_type") == "stream":
                recent_text += "".join(out.get("text", []))
            data = out.get("data", {})
            if not data.get("image/png"):
                continue
            label = label_for_image(recent_text)
            counters[label] = counters.get(label, 0) + 1
            key = label if counters[label] == 1 else f"{label}_{counters[label]}"
            images[key] = base64.b64decode(data["image/png"])

    return images


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Remove previously extracted PNGs (keep .gitkeep)
    for png in OUT_DIR.glob("*.png"):
        png.unlink()

    for rel_nb, mapping in CURATED.items():
        all_images = collect_images(ROOT / rel_nb)
        labels = list(all_images.keys())
        for out_name, picker in mapping.items():
            key = picker(labels)
            if key is None or key not in all_images:
                print(f"WARN: missing {out_name} from {rel_nb} (wanted {key})")
                continue
            (OUT_DIR / out_name).write_bytes(all_images[key])
            print(f"Wrote {out_name} <- {key}")

    print(f"Done. Files in {OUT_DIR}:")


if __name__ == "__main__":
    main()
