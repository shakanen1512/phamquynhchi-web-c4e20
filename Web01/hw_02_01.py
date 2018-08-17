from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<int:weight>/<int:height>')
def bmi(weight,height):
    BMI = weight/((height/100)**2)
    if BMI < 16:
        return "BMI: {}. You are severely underweight.".format(BMI)
    elif 16 < BMI < 18.5:
        return "BMI: {}. You are underweight.".format(BMI)
    elif 18.5 < BMI < 25:
        return "BMI: {}. You are normal.".format(BMI)
    elif 25 < BMI < 30:
        return "BMI: {}. You are overweight.".format(BMI)
    else:
        return "BMI: {}.You are obese".format(BMI)

if __name__ == '__main__':
  app.run(debug=True)
 