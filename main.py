from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
