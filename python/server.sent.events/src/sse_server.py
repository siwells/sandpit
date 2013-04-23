import gevent
import gevent.monkey

gevent.monkey.patch_all()

from flask import Flask, request, Response, render_template

app = Flask(__name__)

def event_stream():
    count = 0
    while True:
        gevent.sleep(1)
        yield 'data: %s\n\n' % count
        count += 1

def json_stream():
    while True:
        gevent.sleep(1)
        yield  'data: {"id": "John123", "msg":"HELLO WORLD"}\n\n'

@app.route('/my_event_source')
def sse_request():
    return Response(
            json_stream(),
            mimetype='text/event-stream')

@app.route('/')
def page():    
    return render_template('sse.html')

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
