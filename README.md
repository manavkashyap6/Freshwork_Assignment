# Freshwork_Assignment
Built a file based key-value data store that supports the basic CRD(create,read,delete) operations.

Language used-Python
OS- Windows is supported.
The data store is present in the form of a JSON file and the key-value pair being added is in the form of a JSON object. 
I have created a class named as Crud inside a file named as crud.py and inside the class four methods(create,read,delete,show) are present.They perform their respective functionalities and appropriate error messages are shown if data store is used in unexpected ways(like deleting any key which is not present in the datastore).
This data store is thread safe as well.
test.py is also added to check the working of code.
