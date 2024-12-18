from flask import Flask,request ,render_template
app=Flask(__name__)
@app.route('/')
def home_page():
    return render_template('bmi_calculator.html')

@app.route('/calculate_bmi', methods=['POST'])
def bmicalc():
    if request.method=="POST":
        weight=float(request.form['weight'])
        height=float(request.form['height'])
        hei=height/100

        bmi=weight/(hei**2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        return render_template('bmi_result.html',bmi=round(bmi,2), category=category)

if __name__ == "__main__":
    app.run(debug=True)