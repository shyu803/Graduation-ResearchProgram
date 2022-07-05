d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

keys = [k for k, v in d.items() if v == 'aaa']
print(keys)
# ['key1', 'key2']

keys = [k for k, v in d.items()]
print(keys)
# ['key3']

keys = [k for k, v in d.items() if v == 'xxx']
print(keys)
# []