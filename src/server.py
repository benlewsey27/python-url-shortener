from flask import Flask, request, redirect
from helpers import filters, db
from models import URL
import logging

logging.basicConfig(level=logging.INFO)

werkzeug = logging.getLogger('werkzeug')
werkzeug.addFilter(filters.HealthFilter())

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route('/health')
def health():
  return 'Hello, World!', 200


@app.errorhandler(404)
def catch(err):
  return 'Error: Route Not Found', 404


@app.errorhandler(405)
def catch(err):
  return 'Error: Invalid Method', 405


@app.route('/generate', methods=['POST'])
def generate_hash():
  if 'url' not in request.json or type(request.json['url']) != str:
    return {
      'status': 400,
      'message': 'url either not found in body or invalid'
    }, 400
  
  long_url = request.json['url']
  base_url = request.base_url
  base_url = base_url.replace('/generate', '')

  protocol = long_url.split('://')[0]
  if protocol != 'http' and protocol != 'https':
    return {
      'status': 400,
      'message': 'Invalid url in request body. URL must start with http or https'
    }, 400

  url_hash = URL.save_hash(long_url)
  return {
    'status': 200,
    'message': 'URL generated successfully',
    'url': f'{base_url}/{url_hash}'
  }, 200


@app.route('/<url_hash>', methods=['GET'])
def redirect_url(url_hash):
  long_url = URL.get_url(url_hash)

  if not long_url:
    return {
      'status': 400,
      'message': 'URL does not exist. Please try another one.'
    }, 400
  
  return redirect(long_url), 302


if __name__ == '__main__':
  db.setup()
  app.run(host='0.0.0.0', port=3000)
