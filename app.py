from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    names = None
    if request.method == "POST":
        raw = request.form.get("names", "")
        # Split on commas, strip whitespace, ignore empty entries
        names = [n.strip() for n in raw.split(",") if n.strip()]
    return render_template("index.html", names=names)


if __name__ == "__main__":
    app.run(debug=True)
