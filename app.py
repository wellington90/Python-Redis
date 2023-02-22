from flask import Flask, render_template
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='localhost', port=6379)

@app.route('/')
def index():
    count = redis_client.get('count')
    return render_template('index.html', count=count)

@app.route('/update')
def update():
    redis_client.incr('count')
    count = redis_client.get('count')
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(debug=True)

