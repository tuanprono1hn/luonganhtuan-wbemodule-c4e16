from flask import Flask, render_template
app = Flask(__name__)

# vao trang chu
@app.route('/')
def index():
    posts = [{"title" : "Tho con nhai",
            "content": "ádkjsahdhsakjhdjksahkjdh",
            "gender" : 1,
            "author": "Tuan To"},
            {"title": "Tho con nong noc",
            "content" : "asdhjksajdkjsadj",
            "gender" : 0,
            "author" : "Tuan to"
            }]
    return render_template("index.html", posts = posts)

@app.route("/hello")
def hello():
    return "Hello C4E16"

@app.route("/sayhi/<name>/<age>")
def sayhi(name, age):
    return "Hi, " + name + ". You're" + age + " years old!"

@app.route("/sum/<int:x>/<int:y>")
def calc(x, y):
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
  # khoi dong sv
