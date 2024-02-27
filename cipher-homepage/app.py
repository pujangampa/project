from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/text-proj')
def text_proj():
    return render_template('../text-proj/templates/index.html')

@app.route('/fold-proj')
def fold_proj():
    return render_template('../fold-proj/templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)
