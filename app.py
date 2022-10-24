from flask import Flask, render_template
import os

app = Flask(__name__)

# Endpoint for 'localhost:5000/'
@app.route("/")
def home():
    """Returns a rendered version of the index.html file with
    a username argument.
    """
    # Just get the enironment variable 'USER'.
    # Its further rendered into the 'index.html'
    user_name = os.environ.get("USER")
    return render_template("index.html", user=user_name)

# Endpoint for 'localhost:5000/get_data'
@app.route("/get_data")
def get_data():
    """Returns a dictionary containing a list of nnumbers."""
    dummy_data = { 
        "data": [1,2,3,4,5,6,7,8,9]
    }
    return dummy_data

if __name__ == "__main__":
    app.run(debug=True)
