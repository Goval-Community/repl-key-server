import flask
import json
import os

_keys = os.getenv("REPL_PUBKEYS")

if _keys is None:
    raise RuntimeError(
        """Please run this on replit.
If this is running on replit and fully up to date file a bug at:
https://github.com/Goval-Community/repl-key-server"""
    )

KEYS = json.loads(_keys)
app = flask.Flask(__name__)


@app.route("/keys")
def keys():
    return KEYS

@app.errorhandler(404)
def notfound(_):
    return {}


app.run(host="0.0.0.0", port=8080)
