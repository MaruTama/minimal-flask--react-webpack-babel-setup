#!/usr/bin/env python
# coding: utf-8
import os
from flask import Flask, render_template, request
import logging

# for import top level package
# ref: [[Python3] 相対パスのimportで上位ディレクトリを指定できない問題とその対策いろいろ](http://nisihunabasi.mods.jp/blog/?p=796)
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import calculation as cal


app = Flask(__name__)

# limit upload file size : 1MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

logging.getLogger().setLevel( logging.DEBUG )
# logging.info('### info output ###')
# logging.debug('### debug output ###')

@app.route("/")
def index():
    return render_template('index.html')

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

@app.route("/add", methods=['GET', 'POST'])
def addition():
    a = 0
    b = 0
    if request.method == 'GET':
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    total = a + b
    logging.info(total)
    return str(total)

if __name__ == "__main__":

    logging.info('### starting on local ###')
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 3000), debug=True, threaded=True)
