#!/bin/sh
echo "{\"unix\":$(date +%s),\"iso\":\"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\"}" > page/plots/timestamp.json
