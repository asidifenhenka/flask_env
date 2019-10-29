from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/p/<int:ids>/')
def ids(ids):
    return '这是一个ids, %s' % ids


@app.route('/f/<float:flo>/')
def ceshi_float(flo):
    return '这是一个float, %s' % flo


@app.route('/path/<path:pa>/')
def ceshi_path(pa):
    return '这是一个path, %s' % pa


# import uuid
# print(uuid.uuid4())
@app.route('/uuid/<uuid:uu>/')
def ceshi_uuid(uu):
    return '这是一个uuid, %s' % uu


# /blog/id/
# /user/id/
# 同时可以映射这两个path
@app.route('/<any(blog,user):user_path>/<float:id>/')
def ceshi_any(user_path,id):
    if user_path == 'blog':
        return '博客详情：%s' %id
    else:
        return 'user: %s' %id

#通过查询字符串的操作来传递参数  https://www.baidu.com/s?wd=python  即问号后面的参数
@app.route('/d/')
def ds():
    wd = request.args.get('wd')
    return '您通过查询字符串的操作传递的参数是 %s' %wd






if __name__ == '__main__':
    app.run(port=50050, debug=True)
