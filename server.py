from flask import Flask

app = Flask(__name__)
from flask import send_file


@app.route("/")
def download():
    path = "Comatose-Servers-Redux-2017.pdf"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
