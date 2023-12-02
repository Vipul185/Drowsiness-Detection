from flask import Flask,render_template,request
import os
from index import d_dtcn

secret_key = str(os.urandom(24))

app = Flask(__name__)                                                #configuring flask settings with their true value
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site                                  #Defining the Endpoints of the URL
@app.route("/",methods=['GET', 'POST'])                               #routing the home page with the flask , r. This route also handles both GET and POST
def home():
    print(request.method)
    # code checks HTTPS request using request module 
    if request.method == 'POST':                          
        if request.form.get('Continue') == 'Continue':                #if if form data = true value  , it will render the main page
           return render_template("test1.html")                       #render the main page
    else:
        # pass # unknown
        return render_template("index.html")                          #else it will stay at the same page and render itself again

@app.route("/start", methods=['GET', 'POST'])                         #routing the main page with the flask and Defining the Endpoints of the URL
def index():                                                                    
    print(request.method)   
    # code checks HTTPS request using request module                                                    
    if request.method == 'POST':                                      #post method is Used to send HTML form data to the server.
        if request.form.get('Start') == 'Start':                      #if form data = true value if will call the function  d_dtcn()  and then returns the template "templates\index.html"
            # pass
            d_dtcn()
            return render_template("index.html")                      #rendering the index page
    else:
        # pass # unknown
        return render_template("index.html")
if __name__ == "__main__":                                            #Current name of python module,
    app.run(debug=True,port=8080)
