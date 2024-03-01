# Git URL Shortener

This Python script allows you to shorten URLs using a Git repository. It provides options to create a new shortened URL and to delete an existing one.

## Installation

If you want to install it on your local machine using the installer script :
```bash
curl https://raw.githubusercontent.com/sailingteam4/git-short-url/main/installer.sh | zsh
```
Or if you want to install it manually, follow these steps:

1. Clone this repository to your local machine.
```bash
git clone https://github.com/sailingteam4/git-short-url.git
```
2. Ensure you have Python installed. This script was developed using Python 3.
3. Install the required Python packages using pip:
```bash
pip install colorama gitpython
```

## Usage

```bash
python git-url-shortener.py [url] [shortened_url]
```
Or if you want to delete a shortened URL:
```bash
python git-url-shortener.py -d [shortened_url]
```