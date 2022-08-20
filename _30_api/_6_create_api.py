from flask import Flask,request

app = Flask(__name__)

@app.route('/edyoda')
def greet():
    data = request.args()
    return {"greet":"Hello Edyoda","data":data}

if __name__ == "__main__":
    app.run()