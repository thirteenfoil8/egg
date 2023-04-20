from datetime import datetime
from egg.dao.web_counter import WebCounterDAO
from egg.models.models import WebCounter

def get_counter():
    dao = WebCounterDAO()
    now = datetime.now()
    counter = dao.get_counter()
    new_counter = counter
    updated_at = now.strftime('%Y-%m-%d %H:%M:%S')
    last_value = counter.new_value
    new_value = last_value+1
    dao.increase_counter(WebCounter(id=0,new_value=new_value,last_value=last_value,updated_at=updated_at))
    return new_value, now