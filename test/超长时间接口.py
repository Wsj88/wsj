from flask import Flask, request
import json
import time
app = Flask(__name__)
app.debug = True
@app.route("/", methods=['post'])

def check():
    # 默认返回内容
    return request.data

if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0",port=8803,debug=True)