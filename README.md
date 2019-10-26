# blender-gpu-test

Install the environment and run test for all GPUs:

`sudo bash -c "$(curl -s https://raw.githubusercontent.com/avsigaev/blender-gpu-test/master/blender_test.sh)"`

Test for certain gpu:

`docker run -it --rm --runtime=nvidia -e FRAME=1 -e SAMPLES=100 -e NVIDIA_VISIBLE_DEVICES=0 avsigaev/blender-test`

NVIDIA_VISIBLE_DEVICES may have multiple values (comma-separated), i.e. "0", or "0,1,2,3"
To control test duration, modify value for "SAMPLES" variable (10 - very fast test, 1000 - heavy test, default=100).
