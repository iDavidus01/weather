from client.airClient import airClient
from config import get_coordinates

def main():
    lat, lon = get_coordinates()
    client = airClient(lat, lon)
    data = client.fetch_current_data()

    if data:
        for k, v in data.get("hourly", {}).items():
            print(f"{k}: {v[0]}")

if __name__ == "__main__":
    main()
