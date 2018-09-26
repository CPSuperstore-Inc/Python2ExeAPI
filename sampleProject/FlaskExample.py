from flask import Flask
import webbrowser

app = Flask(__name__)


@app.route("/")
def index():
    return """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Flask Hello World</title>
    </head>
    <body>
        <h1>Hello World</h1>
    </body>
</html>
    """

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run()
