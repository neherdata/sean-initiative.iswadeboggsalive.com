from flask import Flask, render_template, request, redirect, url_for, flash
import re
import random
from collections import Counter

app = Flask(__name__)
app.secret_key = "replace-with-a-real-secret"  # set in env for production

SPLIT_RE = re.compile(r'[,\n;]+')  # split on commas, newlines, or semicolons


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/parse", methods=["POST"])
def parse():
    raw = request.form.get("names", "")
    # Split by comma/newline/semicolon, trim, and drop empties
    names = [n.strip() for n in SPLIT_RE.split(raw) if n.strip()]
    if not names:
        flash("No valid names found. Enter at least one name separated by commas.")
        return redirect(url_for("index"))
    return render_template("confirm.html", names=names, raw=raw)


@app.route("/results", methods=["POST"])
def results():
    # retrieve repeated 'names' inputs
    names = request.form.getlist("names")
    if not names:
        flash("No names provided to generate results.")
        return redirect(url_for("index"))

    # Assign random integers 1..10 (inclusive)
    rnds = [random.randint(1, 10) for _ in names]
    rows = [{"name": n, "value": v} for n, v in zip(names, rnds)]

    # Find which integer values appear more than once
    counts = Counter(r["value"] for r in rows)
    duplicate_values = {val for val, cnt in counts.items() if cnt > 1}

    return render_template("results.html", rows=rows, duplicate_values=duplicate_values)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
