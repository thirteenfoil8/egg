from egg.database.client import DBClient


class DAO:
    def __init__(self):
        self.db_client = DBClient()

    def get_element_by_id_from_sql(self, sql, args):
        result = self.db_client.select(sql, args)
        row = result.first()
        if row is None:
            return None
        else:
            return row