from flask import render_template, Blueprint

# The . is a shortcut that tells it search in current package before rest of the PYTHONPATH
from .auth import login_required

__author__ = 'Zhongxuan Wang'
__doc__ = 'iGlossary'


app = Blueprint('app', __name__)


@app.route('/', methods=['Get'])
def index():
    return render_template('index.html')


@login_required
def read_file(filename):
    try:
        with open(filename) as f:
            return f.readline()
    except IOError:
        print("IO ERROR Raised. Reading file failed,")
        f = open(filename, "w")
        f.write('email@example.com')
        f.close()
        return 'content'


@login_required
def write_file(filename, file_content):
    try:
        with open(filename, 'w') as f:
            f.write(file_content)
    except IOError:
        print("IO ERROR Raised. Writing file failed,")
    return ''


if __name__ == '__main__':
    app.run(debug=False)
