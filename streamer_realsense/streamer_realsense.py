# Import necessary libraries
import sys
import pyrealsense2 as rs
import numpy as np
from flask import Flask, render_template, Response
import cv2

# Initialize the Flask app
app = Flask(__name__)

port = 5000

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# Get device product line for setting a supporting resolution
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)


def gen_frames():
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        # Convert images to numpy arrays
        depth_image = np.asanyarray(depth_frame.get_data())

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        ret, buffer = cv2.imencode('.jpg', depth_colormap)

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/')
def index():
    # Default route just to provide a simple test page
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    # Use the co-routine to generate and send image frames
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    port = int(sys.argv[1])
    camera_number = int(sys.argv[2])
    print(f"Port Number {port}")
    app.run(host='0.0.0.0', port=port, debug=False)  # Note: Setting debug to true causes the video capture to fail
