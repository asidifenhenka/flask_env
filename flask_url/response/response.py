from flask import Flask, Response, jsonify, render_template

app = Flask(__name__)


class JSONResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        """
        :param response:
        :param environ:
        :return:
        """
        #isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
        # isinstance() 与 type() 区别
        # type() 不会认为子类是一种父类类型，不考虑继承关系。
        # isinstance() 会认为子类是一种父类类型，考虑继承关系
        # 如果要判断两个类型是否相同推荐使用 isinstance()。
        if isinstance(response, dict):
            response = jsonify(response)
            # jsonify除了将字典转换成json对象，还将改对象包装成了一个Response对象
        return super(JSONResponse, cls).force_type(response, environ)



app.response_class = JSONResponse


@app.route('/')
def hello_world():
    Response('Hello', status=200, mimetype='text/html')
    return 'Hello World!', 200, {'X-NAME': 'list'}


@app.route('/list1/')
def list1():
    resp = Response('list1')
    resp.set_cookie('country', 'China')
    return resp


@app.route('/list2/')
def list2():
    return {'username': 'li', 'age': 18}


if __name__ == '__main__':
    app.run(port=50050, debug=True)
