from flask import Flask, render_template
app = Flask(__name__)
@app.route("/user/<username>")
def user(username):
    users = [
            {
            "tuan": {"name" : "Luong Anh Tuan",
                    "gender": 0,
                    "age" : 24,
                    "hobby" : "playing game"}
            },
            {
            "quy" : {"name" : "Dinh Cong Quy",
                    "gender" : 0,
                    "age" : 20,
                    "hobby" : "coding"}
            }
            ]
    return render_template("serex2.html", users = users)
if __name__ == '__main__':
  app.run(debug=True)
