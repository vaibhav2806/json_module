import json 

info = {
    "place" : 'Lucknow',
    "name" : 'Vaibhav',
    "age" : 21
}
with open("data" , 'w') as f:
    json.dump(info,f) 
    