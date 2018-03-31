from flask import Flask
app = Flask(__name__)
@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi = weight*10000/(height*height)
    if bmi < 16:
        return "Severely underweight"
    elif bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    else:
        return "Obese"
if __name__ == '__main__':
  app.run(debug=True)
