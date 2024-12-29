from flask import Flask, request

app = Flask(__name__)

@app.route('/c/<path:subpath>', methods=['GET', 'POST'])
def log_xss(subpath):
    print("Blind XSS payload triggered!")
    print(f"Request path: /c/{subpath}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Query Params: {request.args}")
    print(f"Body: {request.data.decode('utf-8') if request.data else 'None'}")
    return "Payload received", 200

@app.route('/')
def home():
    return "XSS Report Server is running.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
