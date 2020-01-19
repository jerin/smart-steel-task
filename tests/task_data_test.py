from task import TaskData
import pytest
from datetime import datetime

class TestTaskData:
    @staticmethod
    @pytest.mark.usefixtures('protect_db')
    def test_task_data():
        TaskData.insert_task_data(1001,1999.999,"1day.24hrs",datetime.now())
        data = TaskData.get_task_data()
        assert len(data)>0