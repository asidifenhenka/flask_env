from flask import Flask,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return url_for('my_list',page=1,lists='asdd',asd=1.22)
    # return 'Hello World!'


@app.route('/p/<page>')
def my_list():
    return 'my_list'


if __name__ == '__main__':
    app.run(port=50050,debug=True)
