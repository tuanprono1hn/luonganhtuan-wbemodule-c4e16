from flask import Flask, redirect
app = Flask(__name__)
@app.route("/about-me")
def about_me():
    return "Họ Lương tên Tuấn đệm là Anh. Từng là sinh viên tại HUST và hiện đang là nhân viên tại HEAD Doanh Thu. No crush, no dog !!!"
@app.route("/school")
def school():
    return redirect("http://techkids.vn")
if __name__ == '__main__':
  app.run(debug=True)
