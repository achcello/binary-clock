from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/getTime')
def idk():
    print('sending the time:', getTime())
    return(getTime())


def getTime():
    fullTime = str(datetime.now().time())
    hours = fullTime.split(':')[0]
    if len(hours) == 1:
        hours = '0' + hours
    minutes = fullTime.split(':')[1]
    return hours + minutes


if __name__ == '__main__':
    app.run(debug=True)
