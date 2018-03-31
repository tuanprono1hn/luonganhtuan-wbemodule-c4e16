from flask import Flask, render_template
app = Flask(__name__)
@app.route("/user/<username>")
def user(username):
    users = {
            "tuan": {"name" : "Luong Anh Tuan",
                    "gender": 0,
                    "age" : 24,
                    "hobby" : "playing game"},
            "quy" : {"name" : "Dinh Cong Quy",
                    "gender" : 0,
                    "age" : 20,
                    "hobby" : "coding"}
            }
    if username in users:
        return render_template("serex2_2.html", users = users[username])
    else:
        return "No User Found"
if __name__ == '__main__':
  app.run(debug=True)
