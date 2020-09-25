from pathlib import Path
import requests

# https://svc90.cwa.gov.si/version/v1/diagnosis-keys/country/SI/date
protocol = "https://"
host = "svc90.cwa.gov.si"
version = "v1"
country = "SI"

dates_url = f"{protocol}{host}/version/{version}/diagnosis-keys/country/{country}/date"
available_dates = set(requests.get(dates_url).json())
print(f"available dates: {available_dates}")
downloaded_dates = {f.stem for f in Path("page/keys").iterdir()}

for date in available_dates.difference(downloaded_dates):
    print(f"downloading file for {date}")
    file_url = f"{dates_url}/{date}"
    r = requests.get(file_url)
    with open(f"page/keys/{date}.zip", "wb") as f:
        f.write(r.content)
