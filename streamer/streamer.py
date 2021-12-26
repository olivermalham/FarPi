# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
# Initialize the Flask app
app = Flask(__name__)

# This works with normal cameras, but not the Realsense depth stream. Need to figure out how to get hold of that data.
camera = cv2.VideoCapture(0)

# TODO: Figure out how to stream modified or generated images so that I can send enhanced video
# Frames are ndarray objects, [y, x, colours]. All I need to do is create an image as one of these arrays,
# then use opencv to encode it as a jpg and transmit to the browser.


def gen_frames():
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
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
    app.run(debug=False)  # Note: Setting debug to true causes the video capture to fail
