# Docker-Usage-for-Ros2

#Tutorial
https://www.youtube.com/watch?v=KCckWweNSrM
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04

#System
Ubuntu 16.04

#Step 1: Install Docker
Prepare Installation
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
```
Actual installation:
```
sudo apt-get install -y docker-ce
sudo systemctl status docker
```

#Step 2 — Executing the Docker Command Without Sudo (Optional)
If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group (with Ubuntu User Account):
`sudo usermod -aG docker ${USER}`
`su - ${USER}`




