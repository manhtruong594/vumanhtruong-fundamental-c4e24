from flask import Flask
app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    bmi = w/(h/100*h/100)
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi <= 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return " Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    

if __name__ == '__main__':
  app.run(debug=True)