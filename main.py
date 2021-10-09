import os
from pml import app
from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def home():
   return render_template("index.html")
port = int(os.getenv('PORT'))
if __name__=="__main__":
  app.run(debug=True,port)