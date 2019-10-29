# from flask import Flask, render_template
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     context = {
#         'position': -9,
#         'sign':'',
#         'article':'hello world'
#     }
#     return render_template('test.html',**context)
#
#
# @app.template_filter('cut')
# def cut(value):
#     value = value.replace('hello','')
#     return value
#
#
# if __name__ == '__main__':
#     app.run(port=50050, debug=True)
