import json
import time
import os
import threading

class Crud:

    temp={}

    def __init__(self):  

        if os.stat("db.json").st_size != 0:
            with open('db.json','r') as dbr:
                data=json.load(dbr)
            self.temp=data
        self._lock = threading.Lock()
        
      
    def create(self,key,val):
        with self._lock:
            if str(key) in self.temp.keys():
                print("This key is already present,please enter a different key!")
            else:
                self.temp[key]=val
                with open('db.json','w') as dbw:
                    json.dump(self.temp,dbw)
                print("The key-value pair is successfully stored in database")
    
    def read(self,key):
        with self._lock:
            if str(key) not in self.temp.keys():
                print("Please enter a valid key!")
            else:
                print(str(key)+":"+str(self.temp[str(key)]))
    
    
    def delete(self,key):
        with self._lock:
            if str(key) not in self.temp.keys():
                print("Please enter a valid key!")
            else:
                del self.temp[str(key)]
                with open('db.json','w') as dbw:
                    json.dump(self.temp,dbw)
                print("The key-value pair is successfully deleted from database")
    
    def show(self):
        with self._lock:
            print(self.temp)





    
