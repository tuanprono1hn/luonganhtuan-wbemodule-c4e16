from flask import *
from mongoengine import *
from models.service import Service
from models.users import User
from models.order import Order
import mlab

app = Flask(__name__)
app.secret_key = "none"
mlab.connect()

@app.route('/')
def index():
    all_services = Service.objects()
    return render_template('index.html', all_services=all_services)

@app.route('/service-detail/<service_id>', methods = ["GET", "POST"])
def service_detail(service_id):
    if "user_signed_in" in session:
        service = Service.objects.with_id(service_id)
        return render_template('service_detail.html', service=service)
    else:
        return redirect(url_for('sign_in'))
        # return render_template('sign_in.html')

@app.route('/order/<ordered>')
def order(ordered):
    if "user_id" in session:
        order = Order(userid=session["user_id"], serviceid=ordered, is_accepted=False)
        order.save()
        return render_template('order.html')
    else:
        return redirect(url_for('sign_in'))

@app.route('/sign-in', methods = ["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template('sign_in.html')
    elif request.method == "POST":
        form = request.form
        all_user = User.objects()
        username = form["username"]
        password = form["password"]
        user = User.objects(username=username, password=password)
        if list(user) == []:
            return redirect(url_for('sign_up'))
            # Chuyen sang sign up
        else:
            session["user_signed_in"] = True
            session["user_id"] = str(user[0].id)
            # return render_template('service_detail.html')
            return redirect(url_for('index'))

@app.route('/sign-out')
def sign_out():
    del session["user_signed_in"]
    return redirect(url_for('index'))

@app.route('/sign-up', methods = ["GET", "POST"])
def sign_up():
    if request.method == "GET":
        return render_template('sign_up.html')
    elif request.method == "POST":
        form = request.form
        all_user = User.objects()
        username = form["username"]
        password = form["password"]
        user = User.objects(username=username, password=password)
        if list(user) == []:
            session["user_signed_in"] = True
            fullname = form["fullname"]
            email = form["email"]
            username = form["username"]
            password = form["password"]
            new_user = User(fullname=fullname, email=email, username=username, password=password)
            new_user.save()
            return redirect(url_for('index'))
        else:
            return render_template('sign_up_error.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/new-service')
def new_service():
    return render_template('new_service.html')

@app.route('/update-service')
def update_service():
    return render_template('update_service.html')


if __name__ == '__main__':
  app.run(debug=True)
