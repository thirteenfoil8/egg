from datetime import datetime, timezone
import json
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
class DBClient:
    def __init__(self):
        try:
            with open("src/egg/config/client.json") as json_file:
                connection_data = json.load(json_file)
        except: 
            with open("egg/config/client.json") as json_file:
                connection_data = json.load(json_file)
        connection_string = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(
            connection_data['username'], connection_data['password'],
            connection_data['host'], connection_data['port'], connection_data['database'])
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)

    def insert(self, table, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{value}'" for value in data.values())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        try:
            with self.engine.begin() as conn:
                conn.execute(text(sql))
        except Exception as e:
            print(f"Error: {e}")

    def select(self, table, where=None, columns='*'):
        sql = f"SELECT {columns} FROM {table}"
        if where:
            conditions = ' AND '.join(f"{column} = '{value}'" for column, value in where.items())
            sql += f" WHERE {conditions}"
        try:
            with self.engine.begin() as conn:
                result = conn.execute(text(sql)).fetchall()
            return result
        except Exception as e:
            print(f"Error: {e}")

    def update(self, table, data, where):
        updates = ', '.join(f"{column} = '{value}'" for column, value in data.items())
        conditions = ' AND '.join(f"{column} = '{value}'" for column, value in where.items())
        sql = f"UPDATE {table} SET {updates} WHERE {conditions}"
        try:
            with self.engine.begin() as conn:
                conn.execute(text(sql))
        except Exception as e:
            print(f"Error: {e}")

    def delete(self, table, where):
        conditions = ' AND '.join(f"{column} = '{value}'" for column, value in where.items())
        sql = f"DELETE FROM {table} WHERE {conditions}"
        try:
            with self.engine.begin() as conn:
                conn.execute(text(sql))
        except Exception as e:
            print(f"Error: {e}")

    def get_last_row(self, table):
        sql = f"SELECT * FROM {table} ORDER BY id DESC LIMIT 1"
        try:
            with self.engine.begin() as conn:
                result = conn.execute(text(sql)).fetchone()
            return result
        except Exception as e:
            print(f"Error: {e}")

