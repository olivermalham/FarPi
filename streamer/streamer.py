# Import necessary libraries
from flask import Flask, render_template, Response
import cv2
# Initialize the Flask app
app = Flask(__name__)

# This works with normal cameras, but not the Realsense depth stream. Need to figure out how to get hold of that data.
camera = cv2.VideoCapture(0)


def gen_frames():
    frame_count = 0
    while True:
        frame_count = frame_count + 1
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame = draw_overlay(frame, frame_count)
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


def draw_overlay(frame, frame_count=0):
    # Frames are ndarray objects, [y, x, blue, green, red]
    frame = draw_crosshair(frame)
    font = cv2.FONT_HERSHEY_PLAIN
    fontScale = 1.2
    color = (0, 255, 0)
    thickness = 1
    frame = cv2.putText(frame, f'Marvin Video Feed {frame_count}', (10, 470), font, fontScale, color, thickness, cv2.LINE_AA)
    return frame


def draw_crosshair(frame):
    # Main cross hair lines
    cv2.line(frame, (320, 0), (320, 480), (0, 255, 0), 1)
    cv2.line(frame, (0, 240), (640, 240), (0, 255, 0), 1)

    minor_tick = 5
    major_tick = 10

    # Minor ticks
    for i in range(20, 640, 40):
        cv2.line(frame, (i, 240-minor_tick), (i, 240+minor_tick), (0, 255, 0), 1)
    for i in range(20, 480, 40):
        cv2.line(frame, (320-minor_tick, i), (320+minor_tick, i), (0, 255, 0), 1)

    # Major ticks
    for i in range(40, 620, 40):
        cv2.line(frame, (i, 240-major_tick), (i, 240+major_tick), (0, 255, 0), 1)
    for i in range(40, 460, 40):
        cv2.line(frame, (320-major_tick, i), (320+major_tick, i), (0, 255, 0), 1)
    return frame


if __name__ == "__main__":
    app.run(debug=False)  # Note: Setting debug to true causes the video capture to fail
