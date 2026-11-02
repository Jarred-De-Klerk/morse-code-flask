from flask import Flask, render_template, redirect, url_for, request, session
from form import MorseCode
from morse_logic import produce_morse_code
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY'] #Check out this new config.py on the article.

@app.route("/",methods=["GET","POST"])
def home():
    form = MorseCode()
    if form.validate_on_submit():
        text_to_convert = request.form.get("text_to_convert")
        morse_code = produce_morse_code(text_to_convert) #How to get this morse_code variable, into another function? 
        session['result'] = morse_code
        return redirect(url_for("morse"))
    
    return render_template("home.html",form=form)

@app.route("/morse")
def morse():
    output = session.pop("result","Please Click the Button Beneath to Convert Other Text.")
    return render_template("morse.html",result=output)


if __name__ == "__main__":
    app.run(debug=True)