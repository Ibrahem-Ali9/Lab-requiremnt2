from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        username = request.form.get('username')  # Use .get() for safety
        result = f'Hello, {username}! Welcome to the Flask App.'
        return render_template('index.html', result=result)
    
    # Handle the GET request properly
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
