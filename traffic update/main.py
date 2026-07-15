import numpy as np
import pandas as pd
import time
import datetime
import sys

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


# ---------------------------------------------------------------------------
# 1. Generate synthetic historical GPS + traffic data
# ---------------------------------------------------------------------------
def generate_historical_data(num_samples=2000):
    """
    Simulates historical GPS traffic records with features:
      - latitude, longitude  (Assam / Guwahati region by default)
      - hour                 (0-23)
      - day_of_week          (0=Mon … 6=Sun)
      - speed_kmh            (observed speed)
      - congestion_level     (LOW / MODERATE / HIGH — the label)
    """
    np.random.seed(42)

    latitudes = np.random.uniform(26.10, 26.20, num_samples)
    longitudes = np.random.uniform(91.65, 91.80, num_samples)
    hours = np.random.randint(0, 24, num_samples)
    days = np.random.randint(0, 7, num_samples)

    # Speed depends on hour to make patterns learnable
    base_speed = np.random.uniform(15, 80, num_samples)
    # Rush hours (8-10, 17-19) slow things down
    rush_mask = ((hours >= 8) & (hours <= 10)) | ((hours >= 17) & (hours <= 19))
    base_speed[rush_mask] *= 0.45  # cut speed during rush hours

    # Label: LOW >= 50 km/h, MODERATE 25-50, HIGH < 25
    labels = np.where(base_speed >= 50, 0,
             np.where(base_speed >= 25, 1, 2))  # 0=LOW, 1=MODERATE, 2=HIGH

    df = pd.DataFrame({
        "latitude": latitudes,
        "longitude": longitudes,
        "hour": hours,
        "day_of_week": days,
        "speed_kmh": np.round(base_speed, 1),
        "congestion_level": labels,
    })
    return df


# ---------------------------------------------------------------------------
# 2. Train a Random Forest model
# ---------------------------------------------------------------------------
LABEL_MAP = {0: "LOW", 1: "MODERATE", 2: "HIGH"}
EMOJI_MAP = {0: "🟢", 1: "🟡", 2: "🔴"}


def train_model(df):
    """Train a RandomForestClassifier and print its accuracy report."""
    features = ["latitude", "longitude", "hour", "day_of_week", "speed_kmh"]
    X = df[features]
    y = df["congestion_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("=" * 55)
    print("  MODEL EVALUATION — Random Forest Classifier")
    print("=" * 55)
    target_names = [LABEL_MAP[i] for i in sorted(LABEL_MAP)]
    print(classification_report(y_test, y_pred, target_names=target_names))
    print("=" * 55)

    return model


# ---------------------------------------------------------------------------
# 3. Simulate a live GPS feed and predict congestion in real time
# ---------------------------------------------------------------------------
def simulate_live_feed(model, duration=20, interval=2):
    """
    Generates random GPS readings every *interval* seconds for
    *duration* seconds and predicts congestion using the trained model.
    """
    print("\n>>> LIVE TRAFFIC FEED  (press Ctrl+C to stop)\n")

    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            # Simulate a live GPS reading
            lat = round(np.random.uniform(26.10, 26.20), 4)
            lon = round(np.random.uniform(91.65, 91.80), 4)
            hour = datetime.datetime.now().hour
            dow = datetime.datetime.now().weekday()
            speed = round(np.random.uniform(8, 75), 1)

            # Predict
            sample = pd.DataFrame(
                [[lat, lon, hour, dow, speed]],
                columns=["latitude", "longitude", "hour", "day_of_week", "speed_kmh"],
            )
            pred = model.predict(sample)[0]

            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            label = LABEL_MAP[pred]
            emoji = EMOJI_MAP[pred]

            print(
                f"  [{timestamp}]  GPS: ({lat}, {lon})  |  "
                f"Speed: {speed:5.1f} km/h  |  Congestion: {label} {emoji}"
            )

            time.sleep(interval)

    except KeyboardInterrupt:
        pass

    print("\n>>> Feed stopped.\n")


# ---------------------------------------------------------------------------
# 4. Main
# ---------------------------------------------------------------------------
def main():
    print("\n" + "-" * 55)
    print("  REAL-TIME TRAFFIC UPDATE — GPS + Machine Learning")
    print("-" * 55 + "\n")

    # Step 1 — data
    print("[1/3] Generating historical GPS traffic data ...")
    df = generate_historical_data()
    print(f"      {len(df)} records created.\n")

    # Step 2 — train
    print("[2/3] Training Random Forest model ...\n")
    model = train_model(df)

    # Step 3 — live feed
    print("[3/3] Starting live traffic feed ...\n")
    simulate_live_feed(model, duration=30, interval=2)

    print("Done! Exiting.")


if __name__ == "__main__":
    main()
