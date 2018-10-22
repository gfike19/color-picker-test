from flask import Flask, request, redirect, render_template
import os
# import jinja2

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
def indexGet():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def indexPost():
    # below removes # at start and converts to decimal
    # favcolor = str(request.form['favcolor'])[1:]
    # conv = int(str(request.form['favcolor'])[1:], 16)

    favcolor = str(request.form['favcolor'])
    # color input is unicode type from request.form
    #/pagename?(evaluate)variableWhichHas=value
    #method=post is needed on form
    return render_template("lastcolor.html", favcolor=favcolor)
    

if __name__ == "__main__":
    app.run()