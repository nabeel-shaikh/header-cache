from flask import (
    Flask,
    session,
    request,
    redirect,
    url_for,
    flash,
    render_template,
)
from parse import parse_content

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljlnadjnfh20933210139k'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'header_file' not in request.files:
            flash('No file')
            return redirect(request.url)
        header_file = request.files['header_file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if header_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        else:
            content = header_file.read()
            data = parse_content(content)
            session['data'] = data
            return redirect(url_for('index'))  # Follow POST/Redirect/Get Pattern
    return render_template(
        'index.html',
        data=session.get('data')
        )


if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)