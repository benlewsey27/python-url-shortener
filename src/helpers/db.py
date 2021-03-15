import mysql.connector
import os
import logging
import time

logger = logging.getLogger(__name__)

mysql_host = os.getenv('MYSQL_HOST')
mysql_user = os.getenv('MYSQL_USER')
mysql_password = os.getenv('MYSQL_PASSWORD')
mysql_database = os.getenv('MYSQL_DATABASE')

def setup():
  logger.info('Waiting for connection...')
  is_connected = False

  while not is_connected:
    try:
      connection = get_connection()
      is_connected = True
    except Exception:
      logger.debug(f'Waiting for connection. Sleeping 1 second...')
      time.sleep(1)
      pass
  
  logger.info('Setting up tables...')
  cursor = connection.cursor()
  sql = f'CREATE TABLE IF NOT EXISTS urls (url_id INT(6) NOT NULL PRIMARY KEY AUTO_INCREMENT, long_url VARCHAR(255) NOT NULL, hash VARCHAR(255) NOT NULL);'
  cursor.execute(sql)

  logger.info('MYSQL is ready for connections.')

  return

def get_connection():
  return mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
  )
