import time
import multiprocessing
from multiprocessing import Pool
import os
from img_car_cnt import detect 
ports=['1','2','3','4']


def multi():
    print(os.cpu_count)
    p=Pool()
    result=p.map(detect,ports)

    p.close()
    p.join()
    print(type(result))
    return result