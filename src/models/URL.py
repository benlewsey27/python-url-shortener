from helpers import db
import logging

logger = logging.getLogger(__name__)


def save_hash(long_url):
  url_hash = check_hash(long_url)

  if url_hash:
    return url_hash['hash']
  
  url_hash = abs(hash(long_url))
  url_hash_string = str(url_hash)

  connection = db.get_connection()
  cursor = connection.cursor()
  sql = f'INSERT INTO urls (long_url, hash) VALUES (%(long_url)s, %(hash)s)'

  url = {
    'long_url': long_url,
    'hash': url_hash_string,
  }

  cursor.execute(sql, url)
  connection.commit()

  cursor.close()
  connection.close()
  return url_hash_string


def check_hash(long_url):
  connection = db.get_connection()
  cursor = connection.cursor()

  sql = f'SELECT * FROM urls WHERE long_url = %(long_url)s'

  cursor.execute(sql, {'long_url': long_url})
  
  is_found = False
  for url in cursor:
    is_found = True

    url_id = url[0]
    long_url = url[1]
    url_hash = url[2]

    url = {
      'url_id': url_id,
      'long_url': long_url,
      'hash': url_hash,
    }
  
  cursor.close()
  connection.close()

  if not is_found:
    return False

  return url


def get_url(url_hash):
  connection = db.get_connection()
  cursor = connection.cursor()

  sql = f'SELECT * FROM urls WHERE hash = %(hash)s'

  cursor.execute(sql, {'hash': url_hash})
  
  is_found = False
  for url in cursor:
    is_found = True

    url_id = url[0]
    long_url = url[1]
    url_hash = url[2]

    url = {
      'url_id': url_id,
      'long_url': long_url,
      'hash': url_hash,
    }
  
  cursor.close()
  connection.close()

  if not is_found:
    return False

  return url['long_url']
