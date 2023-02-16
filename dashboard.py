from urllib import request
import time
import datetime
import numpy as np
gesamteZeit=0
data=[]
zeitanfang=time.time()
while(gesamteZeit < 60):
    rueckgabewert = request.urlopen('http://www.oh14.de/')
    if(rueckgabewert.code==200):
        data.append(["OK",datetime.datetime.now()])
    elif(rueckgabewert.code==404):
        data.append(["NO",datetime.datetime.now()])
    time.sleep(5)
    zeitende=time.time()
    gesamteZeit=zeitende - zeitanfang
new_array = np.array(data)
file = open("sample.txt", "w+")
content = str(new_array)
file.write(content)
file.close()