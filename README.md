# Docker-Usage-for-Ros2

# Tutorial
https://www.youtube.com/watch?v=KCckWweNSrM
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
https://docker-curriculum.com/
Example Image https://hub.docker.com/r/missxa/bouncy-roboy

# System
Ubuntu 16.04

# Step 1: Install Docker
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

# Step 2 — Executing the Docker Command Without Sudo (Optional)
If you want to avoid typing sudo whenever you run the docker command, add your username to the docker group (with Ubuntu User Account):
`sudo usermod -aG docker ${USER}`
`su - ${USER}`


# Step 3 - Helpful commands
- Info Subcommands: `docker`
- Running Docker Images: `docker ps`
- Make a shared folder between container and host: `docker run -v /host/directory:/container/directory -other -options image_name command_to_run` e.g. `docker run -v /home/martin/Docker-Usage-for-Ros2:/tmp -it missxa/bouncy-roboy bash`


# Step 4 - Working with Docker Images
Test a image from Docker
```
docker run hello-world
```
Pull a existing Docker
```
https://hub.docker.com/r/missxa/bouncy-roboy
```
See existing Docker images on your computer
```
docker images
```

# Step 5 - Running a Docker Container
Choose Ubuntu Container and then start the container
```
docker run missxa/bouncy-roboy
```
Run commands (general)
```
docker run -it missxa/bouncy-roboy bash
```
Run commands (in a shell)
```
docker run -v /home/martin/Docker-Usage-for-Ros2:/tmp -it missxa/bouncy-roboy bash
```

# Step 6 - Managing Docker Containers

See active Docker container
```
docker ps
```
See active and inactive Docker Container
```
docker ps -a
```
Search for commands in container
```
docker search missxy/bouncy-roboy




# Non related commands
- List of ROS Services `ros2 service list`
- Switch between windows `byobu` (Start with `byobu`. Use F2 to switch and F3 to create new terminals)
```
Stop docker
```
docker stop missxa/bouncy-roboy
```
Login Docker (if Required) e.g. docker-registry-username is sharcc92
```
docker login -u docker-registry-username
```
