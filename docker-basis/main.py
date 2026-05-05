from flask import Flask
import os
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/")
def hello_world():
    counter = redis.incr("counter")
    return f"Hello World - counter {counter}"


""" @app.route("/")
def hello_world():
    path = "/data/counter.txt"

    counter = 1  # default starting value

    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                data = f.readline().strip()
                if data:  # not empty
                    counter = int(data) + 1
        except (ValueError, IOError):
            # file exists but content is invalid → reset to 1
            counter = 1

    # persist updated value
    with open(path, "w") as f:
        f.write(f"{counter}\n")

    return f"Hello World - counter {counter}" """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
