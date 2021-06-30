from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route('/expressions/')
def hello_world():

    #Interpolation
    color = "Brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and Subtraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 150

    # String Concatenation
    first_name = "Captain"
    last_name= "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template('expressions.html',**kwargs)

# Dealing with Data Structures.

@app.route('/data-structures/')
def render_data_structures():

    movies = ["Leon the professional",
    "The Usual Suspects",
    "A Beautiful Mind"
    ]

    car = {
        "brand": "Tesla",
        "model": "Roadster",
        "year": "2020",
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Galisto")

    return render_template("data_structures.html", movies = movies, car=car, moons=moons)

@app.route('/conditionals-basics/')
def render_conditionals():
    company = "Apple"
    return render_template("conditionals_basics.html",company=company)

@app.route("/for-loop/")
def render_for_loops():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    return render_template("for_loop.html", planets=planets)

@app.route("/for-loop-and-conditionals/")
def render_for_loop_conditionals():
    user_os = {
        "Bob Smith": "Widnows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salv": "Windows"
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)
