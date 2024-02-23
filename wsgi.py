# importing necessary packages
from flask import Flask, render_template, request
from database import Quiz

app = Flask(__name__)

app.secret_key = "c$7cdap2cs84d+3&p=c*#z)@g(7&ds5e47d9&1%kdx@dsiwnca"

Quiz().init_db()

@app.template_filter('duration_format')
def duration_format(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m"


# HOME PAGE 
@app.route("/")
def index():
    quizzes = Quiz().list_quiz()
    return render_template("index.html", quizzes = quizzes)

# Create Quiz Page
@app.route("/quiz/create", methods = ["GET", "POST"])
def quiz_create():
    if request.method == "POST":
        Quiz().create_quiz(request)
    return render_template("quiz/create.html")

@app.route("/quiz/attend/<code>")
def attend_quiz(code):
    print(code)
    return code