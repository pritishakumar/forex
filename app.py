from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from converter import converting

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-secret"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= True


@app.route("/")

def homepage():
    """ Renders homepage and user input form """
    return render_template("index.html")

@app.route("/converted")   
def converted():
    """ Processes the GET request from form, either converts the
    amount and renders template with converted amount, or 
    flashes any error messages and redirects back to the
    homepage for resubmitting information """
    convert1 = request.args['convert1'].upper()
    convert2 = request.args['convert2'].upper()
    amount = request.args['amount']

    # if browser input required parameters fail
    if not convert1 or not convert2 or not amount:
        flash("Please fill in all the fields prior to submitting", "error")
        return redirect("/")

    resp = converting(convert1, convert2, amount)

    # either flashes error messages and prints proper template
    if resp['messages']:
        for message in resp['messages']:
            flash(message, "error")
        return redirect("/")
    else:
        return render_template("converted.html", symbol= resp['symbol'], amount= resp['amount'])

        
        
        
