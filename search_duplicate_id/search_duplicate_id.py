# https://stackoverflow.com/questions/7370801/how-to-measure-elapsed-time-in-python
import json
import time
from datetime import timedelta

with open('./names.txt', 'r') as stream:
    data = stream.read()    
data_arr = json.loads(data)

# start_time = time.time()
# index_by_name = {name:idx for idx, name in enumerate(data_arr)}  # 로딩에 걸리는 시간을 감안해서 2번 검색으로 시간 비교
# 여러 아이디를 비교한다고 했을 때 index_by_name을 저장하는 것만 미리 로드가 되어 있다면 속도는 hash search가 압도적
# # print(index_by_name)  # {'Ryan Kennedy': 11101903, 'Sandy Kennedy': 7652423, 'Sanford Kennedy': 424045, 'Sarah Kennedy': 11243851, 'Sarah Ann Kennedy': 424049}
# candidate = 'Melanie Griffith'
# if candidate in index_by_name:
#     # print(index_by_name[candidate])
#     print(candidate)
# first_finish_time = time.time()
# print(f'{timedelta(seconds=first_finish_time-start_time)} sec')

# candidate = 'Baoyin Liu'  # 한참 뒤에 있는 이름
# if candidate in index_by_name:
#     # print(index_by_name[candidate])
#     print(candidate)
# print(f'{timedelta(seconds=time.time()-first_finish_time)} sec')
"""
Melanie Griffith
0:00:04.732177 sec
Baoyin Liu
0:00:00.000067 sec
"""

start_time = time.time()
candidate = 'Melanie Griffith'
# linear search
for name in data_arr:
    if name == candidate:
        print(candidate)
        break
first_finish_time = time.time()
print(f'{timedelta(seconds=first_finish_time-start_time)} sec')

candidate = 'Baoyin Liu'  # 한참 뒤에 있는 이름
for name in data_arr:
    if name == candidate:
        print(candidate)
        break
print(f'{timedelta(seconds=time.time()-first_finish_time)} sec')
"""
Melanie Griffith
0:00:00.000063 sec
Baoyin Liu
0:00:00.768446 sec
"""