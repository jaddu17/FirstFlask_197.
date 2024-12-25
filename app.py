from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for form submission using POST method
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    dob = request.form.get('dob')
    if not name or not dob:
        return "Please enter both your name and date of birth!", 400
    return render_template('greeting.html', name=name, dob=dob)

if __name__ == '__main__':
    app.run(debug=True)
