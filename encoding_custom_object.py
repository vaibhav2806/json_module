import json
from datetime import date , datetime

data = {'datetime' : datetime(2020 , 10 , 18 , 1 , 44)}
print(json.dumps(data))

class DatetimeJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.isoformat()
        except AttributeError:
        # obj has no isoformat let bulitin jsonEncoder handle it 
            return super(DatetimeJSONEncoder, self).default(self,obj)
encoder = DatetimeJSONEncoder()
print(encoder.encode(data))
