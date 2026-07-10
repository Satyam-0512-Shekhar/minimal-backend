from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello from my backend!"}

@app.route("/about")
def about():
    return {
        "name": "Satyam Shekhar",
        "course": "BCA",
        "backend": "Flask"
    }

if __name__ == "__main__":
    app.run(debug=True)