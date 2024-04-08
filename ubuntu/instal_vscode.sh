#!/bin/bash

if ! [  -x "$(command -v wget)"]; then
	echo " Error: Wget not installed. Trying to instal wget " >&2
	sudo apt update
	sudo apt install wget -y
	
fi 

# Download the VS Code repository key and add it to the system
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
rm packages.microsoft.gpg

# Add the VS Code repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" | sudo tee /etc/apt/sources.list.d/vscode.list

# Update the package index and install VS Code
sudo apt update
sudo apt install code -y

echo "Visual Studio Code has been installed successfully."

