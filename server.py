from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)



@app.route("/")
def index():
    if "visits" in session:
        session["visits"]+= 1
    else:
        session["visits"] = 1
    return render_template("index.html", views = session["visits"])


@app.route("/twoViews", methods=["POST"])
def addTwo():
    session["visits"] += 1
    return redirect("/")




@app.route("/destroy_session", methods=["POST"])
def clearVis():
    session.clear()
    return redirect("/")

















if __name__=="__main__":
    app.run(debug=True)
