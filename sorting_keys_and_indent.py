import json

info = {
    "cat" : [{'name' : 'zeo', 'color' : 'orange'}, {'name' : 'appe', 'color' : 'white'}]
}

# Using indent to beautify output
d = json.dumps(info , indent=2)
print(d)

# Sorting keys of dictionary
sort = json.dumps(info , sort_keys=True)
print(sort)

# Storing data in data file
with open('data', 'w') as f:
    json.dump(info,f)

# Getting rid of whitespaces to get compact output 
print(json.dumps(info,separators=(',' , ':')))