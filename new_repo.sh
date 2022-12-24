#!/bin/bash

echo "# pysaurus 0.1.0" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pau1tuck/pysaurus.git
git push -u origin main