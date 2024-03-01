import sys
from colorama import Fore, Style
from urllib.request import urlopen
import urllib.request
from git import Repo
import os

args = sys.argv
repo_url = "git@github.com:sailingteam4/sailingteam4.github.io.git"

if len(args) == 3:
	if args[1] == "-d":
		display_name = args[2]
		if (os.path.exists("/tmp/git-short-url/")):
			print(Fore.RED + "Repo already exists" + Style.RESET_ALL)
			entry = input("Do you want to remove the repo? (y/n): ")
			if entry == "y":
				os.system("rm -rf /tmp/git-short-url/")
			else:
				exit()
		if (' ' in display_name):
			print(Fore.RED + "Display name format invalid" + Style.RESET_ALL)
			exit()
		try:
			repo = Repo.clone_from(repo_url, "/tmp/git-short-url/")
		except:
			print(Fore.RED + "Error cloning repo" + Style.RESET_ALL)
			exit()
		if (os.path.exists("/tmp/git-short-url/u/" + display_name) == False):
			print(Fore.RED + "Display name not found" + Style.RESET_ALL)
			exit()
		try:
			os.system("rm -rf /tmp/git-short-url/u/" + display_name)
		except:
			print(Fore.RED + "Error deleting file" + Style.RESET_ALL)
			exit()
		try:
			repo.index.remove(["u/" + display_name + "/index.html"])
			repo.index.commit("Link shortner delete " + display_name)
			repo.remotes.origin.push()
		except:
			print(Fore.RED + "Error pushing to repo" + Style.RESET_ALL)
			exit()
		os.system("rm -rf /tmp/git-short-url/")
		print(Fore.GREEN + "URL deleted successfully" + Style.RESET_ALL)
	else:
		url = args[1]
		display_name = args[2]
		try:
			urlopen(url)
		except:
			print(Fore.RED + "Invalid URL" + Style.RESET_ALL)
			exit()
		if (' ' in display_name):
			print(Fore.RED + "Display name format invalid" + Style.RESET_ALL)
			exit()
		print("Shortening URL: "+ Fore.GREEN + url + Style.RESET_ALL +" with display name: " + Fore.GREEN + display_name + Style.RESET_ALL)
		if (os.path.exists("/tmp/git-short-url/")):
			print(Fore.RED + "Repo already exists" + Style.RESET_ALL)
			entry = input("Do you want to remove the repo? (y/n): ")
			if entry == "y":
				os.system("rm -rf /tmp/git-short-url/")
			else:
				exit()
		try:
			repo = Repo.clone_from(repo_url, "/tmp/git-short-url/")
		except:
			print(Fore.RED + "Error cloning repo" + Style.RESET_ALL)
			exit()
		try:
			os.makedirs("/tmp/git-short-url/u/" + display_name)
		except:
			print(Fore.RED + "Error creating directory" + Style.RESET_ALL)
			exit()
		try:
			with open("/tmp/git-short-url/u/" + display_name + "/index.html", "w") as file:
				template = urllib.request.urlopen('https://raw.githubusercontent.com/sailingteam4/sailingteam4.github.io/main/u/template').read().decode('utf-8')
				template = template.replace("url_to_go", url)
				template = template.replace("Displayname", display_name)
				file.write(template)
		except:
			print(Fore.RED + "Error writing to file" + Style.RESET_ALL)
			exit()
		try:
			repo.index.add(["u/" + display_name + "/index.html"])
			repo.index.commit("Link shortner " + display_name)
			repo.remotes.origin.push()
		except:
			print(Fore.RED + "Error pushing to repo" + Style.RESET_ALL)
			exit()
		os.system("rm -rf /tmp/git-short-url/")
		print(Fore.GREEN + "URL shortened successfully !" + Style.RESET_ALL)
	
else:
	print("Usage: urlshort <url_to_short> <display_name>\nOr urlshort -d <display_name> to delete a short url")