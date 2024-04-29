from flask import Flask, redirect, url_for, render_template
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template(f'index.html')


@app.route("/" , methods=['POST'])
def home():
    return render_template(f'index.html')

if __name__ == "__main__":
    app.run(debug=True)