from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/hello", methods=['POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()
        return make_response({"message": f"Successfully received the data:  {data}"}, 200)


if __name__ == "__main__":
    app.run()