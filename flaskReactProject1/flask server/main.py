from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins ='*')  # * = accept all origins

@app.route("/api/users",methods=['GET'])
def users():
    return jsonify (
           {
              "users":['priyam', 'zach', 'jessie']
            }
    )

if __name__ == "__main__":
   app.run(debug=True,port=8080)
    