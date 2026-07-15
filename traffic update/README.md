# Real-Time Traffic Update 🚦

A Python program that provides real-time traffic congestion predictions using GPS data and a machine learning model (Random Forest Classifier).

## How It Works

1. **Generates** synthetic historical GPS + speed data (simulating the Guwahati region)
2. **Trains** a Random Forest classifier to predict congestion level (`LOW` / `MODERATE` / `HIGH`)
3. **Runs** a live feed — simulates incoming GPS readings every 2 seconds and predicts congestion in real time

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Press `Ctrl+C` to stop the live feed early.

## Sample Output

```
[23:15:42]  GPS: (26.14, 91.73)  |  Speed:  18.3 km/h  |  Congestion: HIGH 🔴
[23:15:44]  GPS: (26.18, 91.70)  |  Speed:  55.2 km/h  |  Congestion: LOW  🟢
[23:15:46]  GPS: (26.12, 91.77)  |  Speed:  32.7 km/h  |  Congestion: MODERATE 🟡
```

## Tech Stack

- **Python 3.8+**
- **scikit-learn** — Random Forest Classifier
- **pandas** — Data manipulation
- **numpy** — Numerical computation
