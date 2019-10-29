from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': '阿斯蒂',
        'age': 18,
        'child': {
            'name': 'abs',
            'high': 193
        }

    }
    # return render_template('index.html', context= context)  这种方式传递的参数是一个字典的格式，不需要在html中定义好接受参数的{{ }}

    return render_template('index.html', **context)
    # 这种方式相当于render_template('index.html',username=username, age= age) 是直接将字典打散成关键参数 需要在html中定义好接受参数的{{ }}


if __name__ == '__main__':
    app.run(port=50050, debug=True)
