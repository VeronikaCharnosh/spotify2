from flask import Flask, render_template, request, redirect
from create_map import result

app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search():
    phrase = request.form['phrase']
    # title = 'Here are your results:'
    results = result(phrase)
    return render_template('Result_map.html')

@app.route('/')
@app.route('/entry')
def entry_page():
    return render_template('entry.html', the_title='Artist from Spotify')

if __name__ == '__main__':
    app.run(debug = True)