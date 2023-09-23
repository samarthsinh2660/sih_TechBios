from flask import Flask,render_template,request
app=Flask(__name__)

'''@app.route("/")
def login():
  return render_template("duplicate.html")

@app.route("/abhano")
def page2():
  return render_template("page2.html")'''

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/register",methods=['GET','POST'])
def register():
  if request.method == 'POST':
    pass
  return render_template("page2.html")

@app.route("/login",methods=['GET','POST'])
def login():
  if request.method == 'POST':
    pass
  return render_template("duplicate.html")

if __name__=="main_":
  app.run(host="0.0.0.0",debug=True)