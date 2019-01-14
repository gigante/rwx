import flask
from chmod import Chmod

app = flask.Flask(__name__)
app.config["DEBUG"] = False
permission = {}


@app.route("/")
def hello():
    return "<h1>rwx api</h1> <p>see docs in <a href='http://github.com/gigante/rwx'>github.com/gigante/rwx</a></p>"


@app.route('/chmod/<param>')
def api_chmod(param):
    c = Chmod(param)
    permission['numeric_mode'] = c.getNumeric()
    permission['text_mode'] = c.getText()
    return flask.jsonify(permission)


if __name__ == "__main__":
    app.run()
