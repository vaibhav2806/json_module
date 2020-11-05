import json

# Python Dict to JSON str

student = {"101" : {"class" : 'V' , "name" : 'Vaibhav'  , "roll_no" : 7  },
           "102" : {"class" : 'V' , "name" : 'Himanshu' , "roll_no" : 17  },
           "103" : {"class" : 'V' , "name" : 'Uditansh' , "roll_no" : 27  }}
jscomp = json.dumps(student,indent=3)
print("Python Dictionaries to JSON strings: \n",type(jscomp))
print("Python Dictionaries to JSON strings: \n",jscomp)
print("\n")

# JSON str to Python Dict

json_data = '{"101": {"class": "V", "name": "Vaibhav", "roll_no": 7}, "102": {"class": "V", "name": "Himanshu", "roll_no": 17}, "103": {"class": "V", "name": "Uditansh", "roll_no": 27}}'
parsed = json.loads(json_data)
print("JSON strings to Python Dictionaries: \n",type(parsed))
print("JSON strings to Python Dictionaries: \n",parsed)
