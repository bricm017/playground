from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def index(): 
    return render_template("index.html")

@app.route('/play')
def play(): 
    return render_template("play.html", x = 3)

@app.route('/play/10')
def play10(): 
    return render_template("play10.html", x = 10)

@app.route('/play/50/yellow')
def play50(): 
    return render_template("play50.html", x = 50)


if __name__=="__main__":
    app.run(debug=True)

#@app.route('/play/2')
#def index(): 

#@app.route('/play/2/yellow')
#def index(): 