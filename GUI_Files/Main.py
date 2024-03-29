#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request, send_from_directory
from camera import VideoCamera
import os
import manual
import auto


pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.
manual_control = manual.control_state()

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/<cmd>')
def command(cmd=None):
    response = cmd
    if cmd == 'up':
        response = 'up arrow'
        manual_control.move_up(5)
        print('up arrow')
    elif cmd == 'down':
        response = 'down arrow'
        manual_control.move_down(5)
        print('down arrow')
    elif cmd == 'right':
        response = 'right arrow'
        manual_control.move_right(5)
        print('right arrow')
    elif cmd == 'left':
        response = 'left arrow'
        manual_control.move_left(5)
        print('left arrow')
    elif cmd == 'fire':
        response = 'fire'
        print('fire')

    return response, 200, {'Content-Type': 'text/plain'}



if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)