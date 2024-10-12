from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods=['POST'])
def greeting():
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        result = f'Hello, {username}! Your email is {email} and your password is {password}.'

        return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run()
