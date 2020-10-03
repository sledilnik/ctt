from jinja2 import Template
from pathlib import Path
from datetime import datetime

available_dates = Path("page/keys/").iterdir()
available_dates = sorted([val.stem for val in available_dates if not val.name == ".gitkeep"], reverse=True)
print(available_dates)

now = datetime.now().strftime("%_d. %_m. %Y ob %H:%M")
print(now)

with open("page/template.html") as f:
    template = Template(f.read())

with open("page/index.html", "w") as f:
    f.write(template.render(dates=available_dates, now=now))
