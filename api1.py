from flask import Flask
import json

app = Flask(__name__)

texto = [
    {
        'name': "Corinthians minha vida",
        "description": "THE BEST"
    }
]

textoJSON = json.dumps(texto)


@app.route('/api/texto')
def texto():
    return textoJSON


if __name__ == '__main__':
    app.run(debug=True, port=5004)
