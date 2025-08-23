"""
@date: 2024/8/1
@author: tangle
"""
from infrustructure.lib import api

dict1 = {'a': {'b': 1, 'key_b': 3},
         'c': 2}
dict2 = {'key_a': 2,
         'c': 3,
         'key_b': 4,
         'a': {'b': 5}}
api.update_nested_dict(dict1, dict2)
print(dict1)
