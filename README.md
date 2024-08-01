# Python-Flask
##  Starting
 - ### Creating Virtual Enviroment
   1. Directory Address should not have the folders which has space in their name
   2. In Terminal:  `pip install venv`
   3. **Create the enviroment** :  `python –m venv c:\desktop…\project_name\venv`
   4. **Activate the enviroment** : ctrl+shift+p  -> python:search interpeture -> select Activate.ps1
      
 -  ### Create the Folder Structure
     1. **Templates Folder**: for storing the html pages
     2. **Static Folder**:  __static/__  ->  _script/script.js_ and _style/style.css_
   
 - ### Base Syntax
   ```python
      from flask import Flask
      app = Flask(__name__)               //creating flask class object
   
      @app.route('/')                     //using obj function decorator
      def home():
          return "Hello World"
   
      if __name__ == '__main__':          
         app.run(debug = True)           //running the flask object
   ```

  - ### Linking HTML,CSS and JS Pages
    Inside index.htnl
    ```html
    <head>
           <link rel ="stylesheet href = "{{url_for('static',filename = 'css.style.css}}" >
    <head>

    <body>
    <body>
    <script type = "text/javascript" src =" {{url_for('static',filename = 'script/script.js')}} "> </script>
    
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
      ```html
       <form action="submit" method="post">
       <p>Enter Your Science Marks</p>
       <input type="number" name = "science" id="science">
       </form>
      ```
      
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

# Jinja 2
  The Variable you want to use should be passed in render template
 - ## If-else condition
   ```html
   {% if result > 50 %}
      <h1> Your result is passed <h1>

   {% else %}
      <h1> Yur result is failed <h1>

   {% endif %}   <!--used to close the if-else block-->
   
   ```
 - ## for loop
   ```html
   <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
   </ul>
     ```
 - ## Macro
   ```
   <!-- Defining a Macro -->
   {% macro render_item(item) %}
      <li>{{ item }}</li>
   {% endmacro %}

   <!-- using the macro -->
   <ul>
    {% for item in items %}
        {{ render_item(item) }}
    {% endfor %}
   </ul>


   ```

    
 - ## filters
   ```html
   <p>{{ "hello world" | title }}</p> <!-- Output: Hello World -->
   <p>{{ user.username | upper }}</p> <!-- Convert to uppercase -->
   ```

 - ## Template inheritance
   Template inheritance in Jinja2 is a powerful feature that allows you to create 
   reusable and maintainable templates by defining a base template and extending it 
   with child templates

   - BASE TEMPLATE: The general layout which include common elements
   - BLOCKS: The placeholders in the base template that child template can overide
   - CHILD TEMPLATE: These template extend the base template and provide content for the defined blocks

  BASE TEMPLATE
   ```html
   html<!-- templates/base.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{% block title %}My Site{% endblock %}</title>
       <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
   </head>
   <body>
       <header>
           <h1>My Website</h1>
           <nav>
               <ul>
                   <li><a href="{{ url_for('home') }}">Home</a></li>
                   <li><a href="{{ url_for('about') }}">About</a></li>
                   <li><a href="{{ url_for('contact') }}">Contact</a></li>
               </ul>
           </nav>
       </header>
       <main>
           {% block content %}
           <!-- Default content goes here -->
           {% endblock %}
       </main>
       <footer>
           <p>&copy; 2024 My Website</p>
       </footer>
   </body>
   </html>

   ```
  - `{% block title %}`: This block allows child templates to set their own title.
  - `{% block content %}`: This block is where child templates will insert their main content.
  - `{{ url_for('home') }}`: Generates URLs for Flask routes, ensuring links are dynamic.

Child Template
```html
<!-- templates/home.html -->
{% extends 'base.html' %}

{% block title %}Home - My Site{% endblock %}

{% block content %}
    <h2>Welcome to My Site</h2>
    <p>This is the home page. Enjoy browsing!</p>
{% endblock %}

```


- ## Using Include
  The {% include %} tag allows you to insert the contents of one template into another

 Base template
  ```html
  <!-- sidebar.html -->
  <div class="sidebar">
      <ul>
          <li><a href="{{ url_for('home') }}">Home</a></li>
          <li><a href="{{ url_for('about') }}">About</a></li>
          <li><a href="{{ url_for('contact') }}">Contact</a></li>
      </ul>
  </div>

  ```
  Child template
  ```html
  <!-- extended_template.html -->
  {% extends 'base.html' %}
  
  {% block content %}
      {% include 'sidebar.html' %}
      <h2>Main Content Area</h2>
      <p>This is the main content of the page.</p>
  {% endblock %}

  ```
