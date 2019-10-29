from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class TelephoneConveter(BaseConverter):
    regex = r'1[85743]\d{9}'


class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    # 这个方法的返回值，将会传递到view函数中作为参数。

    def to_url(self, value):
        return '+'.join(value)

    # 这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。


app.url_map.converters['tel'] = TelephoneConveter  # 将自定义好的转换器添加到DEFAULT_CONVERTERS 中才能生效
app.url_map.converters['lists'] = ListConverter


@app.route('/')
def hello_world():
    print(url_for('posts', boards=['a', 'b']))
    return 'Hello World!'


@app.route('/telephone/<tel:my_tel>/')
def user_ple(my_tel):
    return '您的电话号码是%s' % my_tel


@app.route('/posts/<lists:boards>')
def posts(boards):
    print(boards)
    return '您提交的板块是 %s' % boards


if __name__ == '__main__':
    app.run(port=50050, debug=True)
