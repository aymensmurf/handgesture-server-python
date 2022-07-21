from random import Random
import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*", async_mode='eventlet')
app = socketio.WSGIApp(sio)

motions = ['left', 'right']


def send_motion():
    while True:
        sio.sleep(1)
        sio.emit('motion', motions[Random().randint(0, 1)])


def send_position():
    while True:
        sio.sleep(.1)
        sio.emit('position', {'x': Random().randint(
            0, 1800), 'y': Random().randint(0, 900)})


thread_send_motion = sio.start_background_task(send_motion)
thread_send_position = sio.start_background_task(send_position)

eventlet.wsgi.server(eventlet.listen(('', 8080)), app)
