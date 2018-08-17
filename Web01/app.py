from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {"title" : "Songs I like right now",
        "content" : "Sleep in the car",
        "author" : "Mamamoo",
        "author_gender" : 1},
        {"title" : "Songs I like right now",
        "content" : "Insomnia",
        "author" : "Stray Kids",
        "author_gender" : 0}
    ]
    return render_template("index.html", posts=posts)

@app.route("/hello")
def say_hello():
    return "Hello from the other side"

@app.route("/hi/<name>/<age>")
def say_hi(name,age): #parameter phia tren trung voi argument phia duoi
    return "Hi {}, you are {} years old".format(name,age)

@app.route("/sum/<int:x>/<int:y>")
def total(x,y):
    sum = x + y
    return "{}".format(sum)

if __name__ == '__main__':
  app.run(debug=True)
 