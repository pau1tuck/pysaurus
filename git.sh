#!/bin/bash

datetime=$(date "+%Y-%m-%d_%H:%M_UTC%Z_%a")

echo $datetime

git add .
git commit -m \"$datetime\"
git push -u origin main