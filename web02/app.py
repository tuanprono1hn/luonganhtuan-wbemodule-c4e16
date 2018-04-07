from flask import *
from models.service import Service
import mlab

app = Flask(__name__)
mlab.connect()


# # create document
# new_service = Service(
#                         name="Linh Ka",
#                         yob=2002,
#                         gender=0,
#                         height=148,
#                         phone="0987763542",
#                         address="Hà Đông",
#                         status=True)
# new_service.save()

@app.route('/')
def index():
    return render_template("index.html")
@app.route("/service")
def service():
    all_services = Service.objects()
    return render_template("service.html", all_services=all_services)
@app.route("/detail/<id_to_find>")
def detail(id_to_find):
    service = Service.objects.with_id(id_to_find)
    if service is None:
        return "Not found"
    else:
        return render_template("detail.html", service=service)
@app.route("/search/<int:gender>")
def search():
    all_services = Service.objects(yob__lte=1998)
    # kieu_anh = all_services[0]
    return render_template("search.html", all_services=all_services)
@app.route("/admin")
def admin():
    services = Service.objects()
    return render_template("admin.html", services = services)
@app.route("/delete/<service_id>")
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is None:
        return "Not found"
    else:
        service_to_delete.delete()
        return redirect(url_for("admin"))
@app.route("/new-service", methods = ["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("new-service.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        yob = form["yob"]
        gender = form["gender"]
        phone = form["phone"]

        new_service = Service(name=name, yob=yob, gender=gender, phone=phone)
        new_service.save()
        return redirect(url_for("admin"))
@app.route("/update-service/<id_to_find>", methods = ["GET", "POST"])
def update(id_to_find):
    service_to_update = Service.objects.with_id(id_to_find)
    if id_to_find is None:
        return "Not found"
    if request.method == "GET":
        return render_template("update.html", service=service_to_update)
    elif request.method == "POST":
        form = request.form
        service_to_update.name = form["name"]
        service_to_update.yob = form["yob"]
        service_to_update.gender = form["gender"]
        service_to_update.phone = form["phone"]
        service_to_update.height = form["height"]
        service_to_update.save()
        return redirect(url_for("admin"))

if __name__ == '__main__':
  app.run(debug=True)
