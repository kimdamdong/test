import json

data_file = '/Users/jw/Downloads/data.tsv'

with open(data_file, 'r') as stream:
    data = stream.read()
    
names_raw = data.splitlines()
names_total = names_raw[1:]  # 칼럼 제목 제거

# _, names, _, _, _, _ = [info.split('\t') for info in names_total]

names = []

for info in names_total:
    _, name, _, _, _, _ = info.split('\t')
    names.append(name)
    
with open('./names.txt', 'w') as stream:
    # stream.write(names)
    json.dump(names, stream)

# nm0000001
# Fred Astaire
# 1899
# 1987
# soundtrack,actor,miscellaneous
# tt0053137,tt0072308,tt0050419,tt0031983