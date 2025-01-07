from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["Get"])
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
