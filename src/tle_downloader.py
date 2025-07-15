import os
import requests

def download_tle(url: str, output_path: str = "data/starlink.txt") -> None:
    """
    Downloads TLE data from the given URL and saves it to output_path.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(output_path, "w") as f:
            f.write(response.text)

        print(f"[✔] TLE data downloaded to {output_path}")
    except Exception as e:
        print(f"[✖] Failed to download TLE data: {e}")

# Example usage
if __name__ == "__main__":
    STARLINK_URL = "https://celestrak.com/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
    download_tle(STARLINK_URL)
