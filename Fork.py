import os

def child():
   print(' A new child ',  os.getpid())
   os._exit(0)  

def parent():
   
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d" % pids)
      

parent()
