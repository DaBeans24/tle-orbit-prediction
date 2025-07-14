import os
import requests

# Ensure "data" folder exists
os.makedirs("data", exist_ok=True)

# Download latest Starlink TLEs from Celestrak
url = "https://celestrak.com/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
response = requests.get(url)

# Save to file
tle_path = "data/starlink.txt"
with open(tle_path, "w") as f:
    f.write(response.text)

print(f"Downloaded TLEs to {tle_path}")

