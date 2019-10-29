from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'position': -9,
        'sign':'',
        'alert':" <script>alert('个性签名： hello')</script>",
        'time':datetime(2019,10,1,21,00)

    }
    return render_template('index.html',**context)


@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif 60 <= timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif 60*60 <= timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return "%s小时前" % int(hours)
        elif 60*60*24 <= timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y-%m-%d %H:%M')








if __name__ == '__main__':
    app.run(port=50050, debug=True)
