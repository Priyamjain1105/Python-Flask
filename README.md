# Python-Flask
##  Starting
### Creating Virtual Enviroment
1. Directory Address should not have the folders which has space in their name
2. In Terminal:  `pip install venv`
3. **Create the enviroment** :  `python –m venv c:\desktop…\project_name\venv`
4. **Activate the enviroment** : ctrl+shift+p  -> python:search interpeture -> select Activate.ps1
   
### Create the Folder Structure
1. **Templates Folder**: for storing the html pages
2. **Static Folder**:  __static/__  ->  _script/script.js_ and _style/style.css_

### Base Syntax
```python
   from flask import Flask
   app = flask(__name__)

   @app.route('/')
   def home():
       return "Hello World"

   if __name__ == '__main__':
      app.run(debug = True)
```

## Some Modules

### 1. redirect and url_for
`import redirect, url_for`  
`return redirect(url_for(pass,score = marks))`
### 2. render_template
`import render_template`  
`return render_template('index.html')`
### 3. request
`import request`  

```python
@app.route('/submit',method = ['POST','GET'])
def submit():
    if request.method == 'POST':
       science = float(request.form['science'])
``` 


