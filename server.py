from fastapi import FastAPI
import json
from fastapi_socketio import SocketManager
import socketio


app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi')    
socket_app = socketio.ASGIApp(sio, static_files={'/': 'app.html'})    
background_task_started = False    
    
    
async def background_task():
    with open('data.json', 'r') as f:
        data = json.load(f)
        await sio.emit('data', data)

@sio.on('disconnect')
def test_disconnect(sid):
    print('Client disconnected')


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


app.mount('/', socket_app)