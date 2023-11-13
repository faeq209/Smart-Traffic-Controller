import time
import multiprocessing
from multiprocessing import Pool
import os
from RPI_Sub import sub
from finalDecisionMaking import traffic_controller

def multi():
    print(os.cpu_count)
    p1=multiprocessing.Process(target=sub)
    p2=multiprocessing.Process(target=traffic_controller)
    p1.start() 
    # starting process 2 
    p2.start() 
  
    # wait until process 1 is finished 
    p1.join() 
    # wait until process 2 is finished 
    p2.join()
    
    
if _name=="__main_":
    multi()