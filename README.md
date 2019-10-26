# blender-gpu-test

Test for all GPUs:

`sudo bash -c "$(curl -s https://raw.githubusercontent.com/avsigaev/blender-gpu-test/master/blender_test.sh)"`

Test for certain gpu (after running test for all GPUs):

`docker run -it --rm --runtime=nvidia -e FRAME=1 -e SAMPLES=10 -e NVIDIA_VISIBLE_DEVICES=0 avsigaev/blender-test`

NVIDIA_VISIBLE_DEVICES may have multiple values (comma-separated), i.e. "0", or "0,1,2,3"
