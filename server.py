from flask import Flask

app = Flask(__name__)
from flask import send_file
import logging
from flask import request

@app.route("/download")
def download():
    path = "Comatose-Servers-Redux-2017.pdf"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    app.run(host='0.0.0.0', port=5000, debug=True)
