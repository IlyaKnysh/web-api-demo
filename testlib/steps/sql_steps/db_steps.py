import struct
import pyodbc
from config.db_config import *
from testlib.helpers.logger import logger


class DbConnector:
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        self.connection = pyodbc.connect(
            f'Driver={DRIVER};'
            f'SERVER={DATA_SOURCE};'
            f'DATABASE={self.db};'
            f'UID={USER};'
            f'PWD={PASSWORD};')
        self.connection.add_output_converter(-155, handle_datetimeoffset)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()


def handle_datetimeoffset(dto_value):
    tup = struct.unpack("<6hI2h", dto_value)
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked)


def db_query_executor(db, queries, message):
    if isinstance(queries, str):
        queries = (queries,)
    with DbConnector(db) as conn:
        logger.info(f'{message} {db} started')
        for _query in queries:
            conn.cursor.execute(_query)
            try:
                result = conn.cursor.fetchone()
            except pyodbc.ProgrammingError as ex:
                logger.info(ex)
                result = None
            while conn.cursor.nextset():
                pass
            conn.cursor.commit()
        logger.info(f'{message} {db} finished')
        return result
