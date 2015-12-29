from flask import Flask
from redis import Redis
import subprocess

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    bashCommand ="cat /etc/hosts"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    redis.incr('hits')
    output = process.communicate()[0]
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

