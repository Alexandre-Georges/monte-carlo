import distributions

import traceback

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/index.js')
def js_index():
  return redirect(url_for('static', filename = 'index.js'))

@app.route('/materialize.min.css')
def materialize_css():
  return redirect(url_for('static', filename = 'materialize.min.css'))

@app.route('/materialize.min.js')
def materialize_js():
  return redirect(url_for('static', filename = 'materialize.min.js'))

@app.route('/generate-data', methods = ['POST'])
def generate_data():
  try:
    payload = request.get_json()
    return jsonify(distributions.evaluate(
      interval_size = payload['intervalSize'],
      xile_size = payload['xileSize'],
      expression = payload['expression'],
      sample_size = payload['sampleSize'],
      variables = payload['variables'],
    ))
  except Exception as e:
    print e
    print traceback.print_exc()
    response = jsonify(error=str(e))
    response.status_code = 400
    return response