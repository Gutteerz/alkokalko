from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    result = None
    if request.method == 'POST':
        strpercent = float(request.form['strpercent'])
        strcl = float(request.form['strcl'])
        endpercent = float(request.form['endpercent'])
        ABV = strcl * strpercent
        endcl = ABV / endpercent
        result = f"If you have {strcl}cl of {strpercent}% alcohol, you have {endcl:.2f}cl of {endpercent}% alcohol."
    return render_template('convert.html', result=result)

@app.route('/mix', methods=['GET', 'POST'])
def mix():
    result = None
    if request.method == 'POST':
        drink1percent = float(request.form['drink1percent'])
        drink1cl = float(request.form['drink1cl'])
        drink2percent = float(request.form['drink2percent'])
        drink2cl = float(request.form['drink2cl'])
        ABV1 = drink1cl * drink1percent
        ABV2 = drink2cl * drink2percent
        endpercent = (ABV1 + ABV2) / (drink1cl + drink2cl)
        result = f"If you mix {drink1cl}cl of {drink1percent}% alcohol with {drink2cl}cl of {drink2percent}% alcohol, you get {endpercent:.2f}% alcohol."
    return render_template('mix.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
