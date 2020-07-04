import datetime
from pathlib import Path

# plaintext
with open("create_plaintext.sh", "w") as cb:
    for f in sorted(Path("page/keys").iterdir()):
        if f.name == ".gitkeep":
            continue
        if datetime.datetime.fromisoformat(f.stem) >= datetime.datetime.fromisoformat("2020-07-02"):
            cb.write(f"echo parsing {f}; python ../diagnosis-keys/parse_keys.py -u -n -a -d {f} > page/plaintext/{f.stem}.txt\n")
        else:
            cb.write(f"echo parsing {f}; python ../diagnosis-keys/parse_keys.py -u -a -d {f} > page/plaintext/{f.stem}.txt\n")


# users
with open("create_users.sh", "w") as cb:
    for f in sorted(Path("page/keys").iterdir()):
        if f.name == ".gitkeep":
            continue
        if datetime.datetime.fromisoformat(f.stem) >= datetime.datetime.fromisoformat("2020-07-02"):
            cb.write(f"echo parsing {f}; python ./create_users.py -n -d {f} > page/users/{f}.txt\n")
        else:
            cb.write(f"echo parsing {f}; python ./create_users.py -d {f} > page/users/{f}.txt\n")


# users hourly
with open("create_users_hourly.sh", "w") as cb:
    for f in sorted(Path("page/keys_hourly").iterdir()):
        if f.name == ".gitkeep":
            continue
        if datetime.datetime.fromisoformat(f.stem[: f.stem.rfind("-")]) > datetime.datetime.fromisoformat("2020-07-02"):
            cb.write(f"echo parsing {f}; python ./create_users.py -n -d {f} > page/users_hourly/{f}.txt\n")
        elif datetime.datetime.fromisoformat(f.stem[: f.stem.rfind("-")]) == datetime.datetime.fromisoformat("2020-07-02"):
            if int(f.stem[f.stem.rfind("-") + 1 :]) > 11:
                cb.write(f"echo parsing {f}; python ./create_users.py -n -d {f} > page/users_hourly/{f}.txt\n")
            else:
                cb.write(f"echo parsing {f}; python ./create_users.py -d {f} > page/users_hourly/{f}.txt\n")
        else:
            cb.write(f"echo parsing {f}; python ./create_users.py -d {f} > page/users_hourly/{f}.txt\n")
