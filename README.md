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
   app = flask(__name__)               //creating flask class object

   @app.route('/')                     //using obj function decorator
   def home():
       return "Hello World"

   if __name__ == '__main__':          
      app.run(debug = True)           //running the flask object
```

# Some Modules

 - ## 1. redirect and url_for
      Redirects to other route or function, with parameters
      ```python
      import redirect, url_for
      
      if user_age> 18:
              res = "applicable"    
              
          else:
              res = "not_applicable"   
          return redirect(url_for(res,name = user_name,age = user_age))
      
      # When Res = applicable
      @app.route('/applicable/<name>/<int:age>')
      def applicable(name,age):
          return render_template('a.html',name = name,age= age)
      
      # When Res != applicable
      @app.route('/not_applicable/<name>/<int:age>')
      def not_applicable(name,age):
          return render_template('na.html',name1 = name,age1 = age)
      
      ```

 - ## 2. render_template
      To display the html page, and also sending some data using jinja 2
      ```python
      import render_template
      return render_template('index.html',result = res)
      ```
      
      index.html
      ```html
      <p>hello your result is {{result}} <p>
      ```


 - ## 3. Handeling form's
      `import request`  
      
      ```python
      @app.route('/submit',method = ['POST','GET'])
      def submit():
          if request.method == 'POST':
             sciencMarkse = float(request.form['science'])
   
          if scienceMarks> 18:
             res = "applicable"    
           
          else:
              res = "not_applicable"   
              return redirect(url_for(res,name = user_name,age = user_age))
          
      ``` 


