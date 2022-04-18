"""
    Very simple little flask server implementation that takes numpy arrays from a Redis stream
    and pushes them out as multipart jpg images for the browser to render.
"""

# Import necessary libraries
import sys
from flask import Flask, render_template, Response
import cv2

# Initialize the Flask app
app = Flask(__name__)

port = 5000


def gen_frames():
    frame_count = 0
    while True:
        colour_image = None
        ret, buffer = cv2.imencode('.jpg', colour_image)

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

        
@app.route('/')
def index():
    # Default route just to provide a simple test page
    return render_template('index.html')


@app.route('/image_feed')
def image_feed():
    # Use the co-routine to generate and send image frames
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    port = int(sys.argv[1])
    print(f"Port Number {port}")

    # Start streaming
    app.run(host='0.0.0.0', port=port, debug=False)  # Note: Setting debug to true causes the video capture to fail
