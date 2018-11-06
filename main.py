from flask import Flask, request, redirect, render_template
from PIL import ImageDraw
from PIL import Image

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
    # return redirect("/lastcolor?col="+favcolor)
    

@app.route("/test", methods=['GET'])
def colorRep():
    img = Image.new("RGB", 1024, "white")
    draw = ImageDraw.Draw(img)
    test = draw.rectangle(((0, 00), (100, 100)), fill="black")
    return render_template("lastcolor.html", test=test)

if __name__ == "__main__":
    app.run()