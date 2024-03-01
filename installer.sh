#!/bin/bash

curl -o ~/git-url-short.py https://raw.githubusercontent.com/sailingteam4/git-short-url/main/git-url-short.py
chmod +x ~/git-url-short.py
echo "alias urlshort='~/git-url-short.py'" >> ~/.zshrc
source ~/.zshrc