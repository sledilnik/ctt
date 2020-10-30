#!/bin/bash
rm page/keys_hourly/????-??-??-*.zip && cp ../cwa-scrape/data/SI/hourly/????-??-??-*.zip page/keys_hourly
rm page/keys/????-??-??.zip && cp ../cwa-scrape/data/SI/????-??-??.zip page/keys
rm -rf page/json/*.json
rm -rf page/json_hourly/*.json
rm -rf page/users/*.txt
rm -rf page/users_hourly/*.txt
rm -rf page/plaintext/*.txt
python download_files.py
python download_files_hourly.py
python generate_bash.py
bash create_json.sh
bash create_json_hourly.sh
bash create_plaintext.sh
bash create_users.sh
bash create_users_hourly.sh
python generate_data.py
bash create_timestamp.sh
python generate_html.py
python generate_filehashes.py
#bash cleanup_before_publication.sh
git checkout page/keys
git checkout page/keys_hourly/
#netlify deploy --dir=page --prod
#http-server page/
