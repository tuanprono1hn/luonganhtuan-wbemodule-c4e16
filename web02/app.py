from flask import Flask, render_template
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
@app.route("/search/<int:gender>")
def search(gender):
    all_services = Service.objects(gender=gender, yob__lte=1998, address__icontains= "Hà Nội")
    # kieu_anh = all_services[0]
    return render_template("search.html", all_services=all_services)

if __name__ == '__main__':
  app.run(debug=True)
