from jinja2 import Template
from pathlib import Path
from datetime import datetime
import locale

available_dates = Path("page/keys/").iterdir()
available_dates = sorted([val.stem for val in available_dates if not val.name == ".gitkeep"], reverse=True)
print(available_dates)

locale.setlocale(locale.LC_ALL, 'sl_SI.UTF-8')
now = datetime.now().strftime("%A, %_d. %B %Y ob %H:%M")
print(now)

with open("page/template.html") as f:
    template = Template(f.read())

with open("page/index.html", "w") as f:
    f.write(template.render(dates=available_dates, now=now))
