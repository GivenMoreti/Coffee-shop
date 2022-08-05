from flask import Flask,render_template,request,url_for,redirect,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:given@localhost:5432/coffeedb'
# app.config['SQLALCHEMY_DATABASE_URI'] = False

db = SQLAlchemy(app,session_options={"expire_on_commit":False})
migrate = Migrate(app, db)

class Coffee(db.Model):
    __tablename__ = 'coffee'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(),nullable = False)
    price = db.Column(db.Float(),nullable=False)
    order_id = db.Column(db.Integer,db.ForeignKey('orders.id'),nullable=True)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer,primary_key = True)
    customer = db.Column(db.String(),nullable = False)
    order_quantity = db.Column(db.Integer,nullable = False)
    order_list = db.relationship('Coffee',backref ='order',lazy = True)

# db.create_all()
@app.route("/coffees/<order_id>")
def order(order_id):
    return render_template('coffee.html',coffees=Coffee.query.all())

@app.route("/")
def index():
    return redirect(url_for('order',order_id = 1))
    # return render_template('coffee.html',coffees=Coffee.query.all())


@app.route("/coffees/<cart>")
def bucket(cart):
    return "items in a bucket"
# @app.route('/Order',methods = ['POST'])
# def insert_coffee():
#     if request.method =='POST':
#         coffee_name = request.form['coffee_name']
#         my_coffee = Coffee(coffee_name)
#         db.session.add(my_coffee)
#         db.session.commit()
#     return redirect(url_for('index'))


   
# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#   error = False
#   body = {}
#   try:
#     description = request.get_json()['description']
#     todo = Todo(description=description)
#     db.session.add(todo)
#     db.session.commit()
#     body['description'] = todo.description
#   except:
#     error = True
#     db.session.rollback()
#     print(sys.exc_info())
#   finally:
#     db.session.close()
#   if error:
#     abort (400)
#   else:
#     return jsonify(body)

















    





def __repr__(self):
    return f"<Coffee ID: {self.id},name: {self.name},price:{self.price}>"

if __name__ == '__main__':
    app.run(debug=True)