#!/bin/bash

# python3 ./streamer/streamer.py 5001 1 >> ./log/camera1_stream.log 2>&1 &
# python3 ./streamer/streamer.py 5002 2 >> ./log/camera2_stream.log overlay 2>&1 &
python3 ./streamer_realsense/streamer_realsense.py 5000 >> ./log/realsense_stream.log 2>&1 &

