import requests

url = "https://celestrak.com/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
response = requests.get(url)
with open("data/starlink.txt", "w") as f:
    f.write(response.text)
