from flask import Flask, request, jsonify


app = Flask (__name__)

@app.route("/")
def index():

    return "<h2>main_page</h2>"

if __name__== "__main__":
    app.run(debug=True)