from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        return(render_template("index.html",result="no model yet.........."))
    else:
        return(render_template("index.html",result="waiting for rate..........."))
if __name__ == "__main__":
    app.run()
