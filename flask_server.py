import flask from Flask, request, jsonify


app = Flask(_name_)

@app.route("/")
def first():
    logging.info("User request to /")
    return "Hello!"