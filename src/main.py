from datetime import datetime, timezone


def main() -> None:
    print("water-utility-sensor-anomaly-detection initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
