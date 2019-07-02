from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')      
def hello_world():
    return render_template('index.html')  
@app.route('/dojo')
def dojo():
    return 'Dojo!'
@app.route('/say/<name>')
def hello(name):
    print(name)
    return 'Hello, ' + name
@app.route('/repeat/<num>/<greeting>')
def repeating(num, greeting):
    print(int(num))
    print(greeting)
    return(greeting * int(num))
if __name__=="__main__":   
    app.run(debug=True)    
