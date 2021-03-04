from flask import Flask
from flask import request

app = Flask(__name__)
count = 0

@app.route("/", methods=['GET', 'POST'])
def hello():
    global count
    
    if request.method == 'POST':
       count += 1
       return "Ok"
    else:
        return "POST requests: %i" % count


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
