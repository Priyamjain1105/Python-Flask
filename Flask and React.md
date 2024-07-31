# Emmbding flask and React
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
      - Active the env: `myenv\Script\activate`
   - ### Now we will install necessay dependencies fro backend
      - Install flask: `pip install flask`
      - click on server: create new file `main.py`

# Theory
In the app where we have seperate frontend and seperate backend those server communicate thrugh http requests

## Example
Example creating backend Route list of users return from that route, and frontend will be used to retrive those users name from the backend route and display them on the frontend.

```py
from flask import Flask, jsonify
app = Flask(__name__)
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
`jsonify`: will be used to send the responce of our api route in a json format

