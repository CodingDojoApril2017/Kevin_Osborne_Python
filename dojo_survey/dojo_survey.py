from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    print "received 1"
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print "received 2"
    print request.form
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)
