from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/AC2', methods=["GET"])
def timão():
    return 'TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO TIMÃO'


if __name__ == '__main__':
    app.run(debug=True, port=5004)
