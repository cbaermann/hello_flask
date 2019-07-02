from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play')
def home():
    return render_template('playground.html', times=1, color = 'aqua')
@app.route('/play/<num>')
def multiples(num):
    return render_template('playground.html', times=int(num), color = 'aqua')

@app.route('/play/<num>/<color>')
def multiple_colors(num, color):
    return render_template('playground.html', times=int(num), color = color )

if __name__=='__main__':
    app.run(debug=True)