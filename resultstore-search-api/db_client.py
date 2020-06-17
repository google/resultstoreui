import sys
import psycopg2
import logging
from psycopg2.extras import DictCursor

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

INITIALIZE_TABLES = [
    "CREATE TABLE TOOL_TAGS (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL);"
]


class Database:
    """PostgreSQL Database class."""
    def __init__(self, config):
        self.host = config['DATABASE_HOST']
        self.username = config['DATABASE_USERNAME']
        self.password = config['DATABASE_PASSWORD']
        self.port = config['DATABASE_PORT']
        self.dbname = config['DATABASE_NAME']
        self.conn = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(host=self.host,
                                             user=self.username,
                                             password=self.password,
                                             port=self.port,
                                             dbname=self.dbname)
            except psycopg2.DatabaseError as e:
                _LOGGER.error(e)
                sys.exit()
            finally:
                _LOGGER.info('Connection opened successfully.')

    def select_rows(self, query):
        """Run a SQL query to select rows from table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            records = [row for row in cur.fetchall()]
            cur.close()
            return records

    def update_rows(self, query):
        """Run a SQL query to update rows in table."""
        self.connect()
        with self.conn.cursor() as cur:
            cur.execute(query)
            cur.close()
            self.conn.commit()
            _LOGGER.info(f"{cur.rowcount} rows affected.")

    def select_rows_dict_cursor(self, query):
        """Run a SQL query to select rows from table and return dictionarys."""
        self.connect()
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute(query)
            for row in cur.fetchall():
                _LOGGER.info(row['first_name'])
        cur.close()
        self.conn.commit()

    def create_tables(self):
        """ Initialize Tables """
        self.connect()
        with self.conn.cursor() as cur:
            for command in INITIALIZE_TABLES:
                cur.execute(command)
        self.conn.commit()
        cur.close()

    def close_connection(self):
        """ Close database connection"""
        self.conn.close()
