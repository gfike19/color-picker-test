from flask import Flask, request, redirect, render_template
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
def indexGet():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def indexPost():
    favcolor = request.form['favcolor']
    #/pagename?(evaluate)variableWhichHas=value
    #method=post is needed on form
    return render_template("lastcolor.html", favcolor=favcolor)
    
# @app.route("/lastcolor", methods=['GET'])
# def lastColorGet():
#     test = "words"
#     favcolor = request.args.get("favcolor")
#     return render_template("lastcolor.html", favcolor=favcolor, test=test)

if __name__ == "__main__":
    app.run()