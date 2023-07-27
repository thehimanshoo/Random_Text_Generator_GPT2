import string
from flask import Flask, render_template, request
from matplotlib.pyplot import title
from transformers import pipeline

app = Flask(__name__)
generator = pipeline(task='text-generation', model='gpt2')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output', methods = ['POST'])
def textGen():
    title = request.form['name']
    output = generator(title, max_length=500, num_return_sequences=1)
    
    #Converting list to string and removing newline chars
    string = ""
    for i in output:
        string += str(i)
    n = len(string)
    string = string[20:n-2]
    string = string.replace('\\n', '')

    return render_template('output.html', name=string)


if __name__ == '__main__':
    app.debug = True
    app.run()