from logs import Log
import pytest
import uuid
from datetime import datetime

class TestLog:
    @staticmethod
    @pytest.mark.usefixtures('protect_db')
    def test_log():
        Log.insert_log("info","test action","test message")
        log = Log.get_log()
        assert len(log)>0