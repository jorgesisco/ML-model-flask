from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello gente"

if __name__ == "__main__":
    app.run(debug=True)


# sudo lsof -i:5000
# sudo kill PID