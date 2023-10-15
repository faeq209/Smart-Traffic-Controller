import time
import multiprocessing
from multiprocessing import Pool
import os
from car_count import detect
ports=['1','2','3','4']


if __name__=="__main__":
    print(os.cpu_count)
    p=Pool()
    result=p.map(detect,ports)
    p.close()
    p.join()
