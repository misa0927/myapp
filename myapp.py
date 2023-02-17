from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello/api")
def hello_api():
    message = {'message' : "Hello world"}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
