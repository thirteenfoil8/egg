from egg.models.models import WebCounter
from egg.database.client import DBClient
from egg.dao.common import DAO


class WebCounterDAO(DAO):
    def increase_counter(self, webcounter:WebCounter):
        self.db_client = DBClient()
        data = {
            'new_value': webcounter.new_value,
            'last_value': webcounter.last_value,
            'updated_at': webcounter.updated_at}
        self.db_client.insert(table= " web_page_counter",data=data)

    def get_counter(self) -> WebCounter:
        self.db_client = DBClient()
        row = self.db_client.get_last_row(table= " web_page_counter")
        return self.get_model_from_result_set(row)

    @staticmethod
    def get_model_from_result_set(result_set) -> WebCounter:
        if result_set:
            return WebCounter(
                result_set[0],
                result_set[1],
                result_set[3],
                result_set[2]
                
            )
        else:
            return None

if __name__ == "__main__":
    dao = WebCounterDAO()
    print(dao.get_counter().__dict__)