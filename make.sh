#!/bin/bash
python download_files.py
python download_files_hourly.py
python generate_bash.py
bash create_json.sh
bash create_json_hourly.sh
bash create_plaintext.sh
bash create_users.sh
bash create_users_hourly.sh
python generate_data.py
python generate_html.py
python generate_filehashes.py
#bash cleanup_before_publication.sh
#netlify deploy --dir=page --prod
