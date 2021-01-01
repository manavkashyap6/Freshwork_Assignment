from crud import Crud
import threading

c=Crud()
t1 = threading.Thread(target=c.delete, args=(1,)) 
t2 = threading.Thread(target=c.read, args=(1,))
t3 = threading.Thread(target=c.create,args=(5,6,))

t1.start() 
t2.start() 
t3.start() 