from flask import Flask, render_template, request
import dao
app = Flask(__name__)

@app.route('/')
def index():
    request.args.get('kw')
    products=dao.load_product('kw')

    return render_template('index.html',product=products)
if __name__ == '__main__':
    app.run(debug=True)