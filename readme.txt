--> JSON stands for JavaScript Object Notation. 
--> JSON is a DATA-INTERCHANGE FORMAT, derived from JavaScript. 
--> It is mostly used for STORING or TRANSFERRING data. 
--> So, if we want our program to interact with the internet, we must be familiar with this module, 
even only to send or receive data through the internet. 

--> It is one of Python's most important modules because, however small level of our  program is if 
we want it to interact only a bit through the internet, the Json module must be imported first. 

--> A JSON is an unordered collection of key and value pairs similar to a python dictionary. 

-->The following are some important points about JSON :

-> Keys are unique strings that cannot be null.
-> Values can be anything from a String, Number, Tuple, Boolean, list, or null.
-> A JSON is represented by a string which is enclosed within curly braces { }
with keys-value pairs which are separated by a colon ( : ), and pairs separated by a comma(,).

--> If we convert a JSON string to a Python, the resultant will be a dictionary. 
--> The conversion is also known as parsing, and that is the keyword we use professionally for the conversion. 
-->We can either convert from JSON to Python or from Python to JSON by using json.loads() or json.dumps() methods.

--> Methods:

-> load()  : This method is used to load data from a JSON file into a python dictionary.
-> loads() : This method is used to load data from a JSON variable into a python dictionary.
-> dump()  : This method is used to load data from the python dictionary to the JSON file.
-> dumps() : This method is used to load data from the python dictionary to the JSON variable.


--> JSON is most commonly used for client-server communication because it is human readable and both easy to read/write.
--> JSON is mainly based on key-value pairs, similar to a dictionary in Python. 
--> The separators could be full stops, commas, blank spaces, etc.
--> To use the JSON module in python, we have to import it. While using json.dumps(), 
we can send separators in parameters to make the code more readable and well defined.