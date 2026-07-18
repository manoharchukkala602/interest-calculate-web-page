from flask import Flask,render_template,request
app =Flask(__name__)
@app.route("/" ,methods=["GET", "POST"])
def boom():
    result =None
    if request.method == "POST":
        principal =float(request.form["principal"])
        rate =float(request.form["rate"])
        time =float(request.form["time"])
        result =(principal*rate*time) / 100
        
    return render_template("index.html",result=result)

if __name__ =="__main__":
    app.run(debug=True)
    