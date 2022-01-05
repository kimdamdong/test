# https://stackoverflow.com/questions/21732123/convert-true-false-value-read-from-file-to-boolean
import json
from ast import literal_eval

with open('./tf_str.json', 'r') as stream:
    tf_str = stream.read()
    
tf_str_json = json.loads(tf_str)

# print(json.loads(tf_str_json['value1']))
# print(literal_eval('True'))
# print(literal_eval('true'))  #  소문자는 인식 못함

for k, v in tf_str_json.items():
    tf_str_json.update({k: json.loads(v)})
    
print(tf_str_json)
