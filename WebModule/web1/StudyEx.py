from flask import Flask, render_template,redirect

app = Flask(__name__)


@app.route("/about-me")         # router
def about_me():
    return " My name is Truong I love  purple, like the fidelity "

@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)

if __name__ == "__main__":
    app.run(debug=True)

