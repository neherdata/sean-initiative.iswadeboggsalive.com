from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/startgame', methods=['POST', 'GET'])
def startgame():
    if request.method == 'POST':
        user = request.form['player']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('player')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
