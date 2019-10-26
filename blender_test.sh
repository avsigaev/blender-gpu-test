#!/usr/bin/env bash

if ! [ -f /usr/bin/nvidia-docker ]; then
	curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | apt-key add -
	distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
	curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | tee /etc/apt/sources.list.d/nvidia-docker.list
	apt-get update
	apt-get install nvidia-docker2 -y
	pkill -SIGHUP dockerd
fi

docker run -it --rm --runtime=nvidia -e FRAME=1 -e SAMPLES=100 avsigaev/blender-test
