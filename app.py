from flask import Flask , render_template

# INITIALIZING FLASK APPLICATION
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.jinja")

@app.route('/products')
def product():
    return render_template("product.jinja")



if __name__=='__main__':
    app.run(debug=True, port = 8000)