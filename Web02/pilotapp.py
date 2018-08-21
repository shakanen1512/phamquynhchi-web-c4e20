from flask import Flask, render_template
import mlab
from mongoengine import *
from models.services import Service
from models.customers import Customer

app = Flask(__name__)
mlab.connect()

#design pattern (MVC, MVP)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(
        gender=g,
        yob__lte=1998,
        height__gte=165,
        address__icontains="Hà Nội")
    return render_template(
        'search.html',
        all_service=all_service
        )

@app.route('/customer/')
def customer():
    all_customer = Customer.objects(
        gender=1,
        status=True
        ).limit(10)
    return render_template(
        'customer.html',
        all_customer=all_customer
        )

if __name__ == '__main__':
  app.run(debug=True)
 