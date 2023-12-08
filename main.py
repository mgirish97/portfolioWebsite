from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['subject']
        message = request.form['body']
        print(name)
        return redirect(f'mailto:meghanagirish@hotmail.com?subject={name}&body={message}')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)