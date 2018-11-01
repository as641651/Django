from flask import Flask, render_template, request

app = Flask(__name__)
app.debug=True

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')

        return "form submitted!" + "<p>" + username + "</p><p>" + email + "</p>"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
