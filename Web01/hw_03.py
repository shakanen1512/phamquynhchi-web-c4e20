from flask import Flask, render_template
app = Flask(__name__)


@app.route("/user/<username>")
def profile(username):
    users = {
        "tokyo" : {
                "name" : "Tokyo",
                "age" : 1,
                "country" : "Japan",
                "hobby" : "Tokyo Sky Tree"
        },
        "chicago" : {
                "name" : "Chicago",
                "age" : 2,
                "country" : "USA",
                "hobby" : "Millenial Park"
        },
        "toronto" : {
                "name" : "Toronto",
                "age" : 3,
                "country" : "Canada",
                "hobby" : "University of Toronto"
        }
    }

    if username in users:
        name = users[username]["name"]
        age = users[username]["age"]
        country = users[username]["country"]
        hobby = users[username]["hobby"]
        return render_template('username.html', name=name,age=age,country=country,hobby=hobby)
    else:
        return "User not found"
    
if __name__ == '__main__':
  app.run(debug=True)
 