import os
from flask import Flask, render_template, session, url_for, request, redirect
app = Flask(__name__)

app.secret_key = os.urandom(8)
print(os.urandom(8))

vorur = [[0,"Air Jordan 1 Retro High OG Bred Toe","unnamed.png",25000],
        [1,"Travis Scott x Air Jordan 1 Retro High OG 'Mocha'","snusa-detail_20.png",100000],
        [2,"Air Jordan 1 Retro High OG 'Royal' 2017","royal.jpeg",2500],
        [3,"Air Jordan 4 Retro 'Military Blue' 2012","bm.jpeg",2500],
        [4,"Air Jordan 4 Retro 'Classic Green' 2004","green.jpeg",2500],
        [5,"Dunk Low Retro SP 'Syracuse'","orange.jpeg",2500],
        




        ]
@app.route("/")
def index():
    karfa = []
    fjoldi = 0
    if "karfa" in session:
        karfa = session["karfa"]
        fjoldi = len(karfa)
    return render_template("index.tpl", v=vorur, fjoldi=fjoldi)

@app.route("/add/<int:id>")
def frett(id):
    karfa = []
    fjoldi=0
    if "karfa" in session:
        karfa = session["karfa"]
        karfa.append(vorur[id])
        session["karfa"] = karfa
        fjoldi = len(karfa)
    else:
        karfa.append(vorur[id])
        session["karfa"] = karfa
        fjoldi = len(karfa)

    return render_template("index.tpl", v=vorur, fjoldi=fjoldi)
@app.route("/karfa")
def karfa():
    karfa = []
    summa = 0
    if "karfa" in session:
        karfa = session["karfa"]
        fjoldi = len(karfa)
        for i in karfa:
            summa += int(i[3])
        return render_template("karfa.tpl", k = karfa, tom = False, fjoldi= fjoldi, samtals=summa)
    else:
        return render_template("karfa.tpl", k = karfa, tom = False)
@app.route("/eydavoru/<int:id>")
def eydavoru(id):
    karfa = []
    karfa = session["karfa"]
    vara = 0
    for i in range(len(karfa)):
        if karfa[i][0] == id:
            vara = i
    karfa.remove(karfa[vara])
    session["karfa"] = karfa
    return render_template("eydavoru.tpl")

@app.route("/eyda")
def eyda():
    session.pop("karfa", None)
    return render_template("eyda.tpl")


@app.route("/result", methods = ["POST"])
def result():
    if request.method == "POST":
        kwargs={
                'name': request.form['nafn'],
                'email': request.form['email'],
                'phone': request.form['simi'],
                'price': request.form['samtals']
        }
        return render_template("result.tpl",**kwargs)


@app.route("/logout")
def logout():
    session.pop("karfa", None)

    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template("pagenotfound.html"), 404


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)