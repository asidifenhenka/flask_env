from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    return '这是登陆界面'


@app.route('/profile/')
def profile():
    if request.args.get('name'):   #获取获取地址栏中参数 ，不分get请求方式还是post请求方式.
        return '这是个人中心'
    else:
        # redircet 重定向
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port=50050, debug=True)
