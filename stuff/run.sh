#!/usr/bin/env bash

echo "Running apt-get update.."
apt-get update > /dev/null
echo "Installing dependencies.."
apt-get install -y ocl-icd-opencl-dev > /dev/null

if [ -z $FRAME ]; then
  RENDER_FRAME=""
else
  RENDER_FRAME="-f $FRAME"
fi

if [ -z $SAMPLES ]; then
  RENDER_SAMPLES=10
else
  RENDER_SAMPLES=$SAMPLES
fi

/usr/local/blender280/blender --background /source.blend -noaudio -y -P /script_2.80.py $RENDER_FRAME -- "{\"scene\":\"Scene\",\"camera\":\"Camera.006\",\"res_x\":1920,\"res_y\":816,\"samples\":$RENDER_SAMPLES,\"run_mode\":\"render\",\"result_dir\":\"/result/\"}"

if [ $? -eq 0 ]; then
  echo "================================"
  echo ""
  echo "Test result: OK :)"
  echo ""
  echo "================================"
else
  echo "================================"
  echo ""
  echo "Test result: Errors has been occured during test scenario :("
  echo ""
  echo "================================"
fi
