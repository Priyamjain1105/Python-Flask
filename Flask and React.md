# Emmbeding flask and React
## Step 1: Create Folder (react+flask)
## Step 2: Prepare Frontend
  - in terminal: `npx create-vite`
  - project_name: `client`
  - app type :`React`
  - Language used: `JavaScript`
  - Necessary Command 1:`cd client` (change into directory)
  - Necessary Command 2:`npm install` (to install necessary dependicies)
## Step 3: Prepare Backend (in new terminal)
   - **In main folder**: create new folder named: `server` where backend code will recide.
   - ### Creating virtual enviroment
      - To folder server: `cd server`
      - Create env in terminal: `python -m venv myenv`
      - Active the env: `myenv\Scripts\activate`
   - ### Now we will install necessay dependencies fro backend
      - Install flask: `pip install flask`
      - click on server: create new file `main.py`

# Theory
In the app where we have seperate frontend and seperate backend those server communicate thrugh http requests

## WORKING IN BACKEND (SERVER)
Example creating backend Route list of users return from that route, and frontend will be used to retrive those users name from the backend route and display them on the frontend.

```py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins ='*')  # * = accept all origins

@app.route("/api/users",methods=['GET'])
def users():
    return jsonify {
           {
              "users":['priyam', 'zach', 'jessie']
            }
        }

if __name__ == "__main__":
   app.run(debug=True,port=8080)
    
```
Test 1: if you'll run `localhost:8080/api/users` you'll get the api output
Test 2: 

1. `jsonify`: will be used to send the responce of our api route in a json format
2. 'C' to stop the backend server in terminal


now we will begin setting up our frontend and configure it so that it can fetch from this api route, before procefing to work with frontend we need to allow that we have cross-origin request to occour, since the frontend is calling the local host at 8080 to get date from this route, we need to ensure that this server is accepting those requests, to do that we need to enable origins

1. Install `pip install Flask-CORS`
2. `from flask_cors import CORS`     
3. `cors = CORS(app, origins ='*')`
   - it is set to all(*) to avoid any errors  
                             SERVER CONFICURATION IS COMPLETED

# WORKING IN FRONT-END
Inside App Jsx file
STEP 1: open new terminal
STEP 2: move to client directory `cd ../client`
STEP 3: `npm install axios`, using to fetch api request to our server
STEP 4: `npm run dev`
STEP 5: in parallel terminal start backend server in terminal :`main.py`

fetch the backend api

   - ## INSIDE App.jsx
     ```jsx
     import {useState,useEffect} from "react";
     import axios from "axios";
     function App(){
              const [count, setCount] = useState(0);

              const fetchAPI = async() => {
                    const responce = await axios.get("https://localhost:8080/api/users");
                                       }
                    console.log(responce.data.users);

               useEffect{() => {
                            fetchAPI();
                   }, []);
     ```
     - Resonce varialble is used to store data
     - users array
     - useEffect is grabbing the users object and print the result
    
   - ## Displaying the output
     ```jsx
     
     ```
