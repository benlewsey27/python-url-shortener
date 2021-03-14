from flask import Flask
from helpers import filters, db
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

if __name__ == '__main__':
  db.setup()
  app.run(host='0.0.0.0', port=3000)
