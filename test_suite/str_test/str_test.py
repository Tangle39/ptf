"""
@date: 2025/8/23
@author: tangle
"""
from infrustructure.lib import api

cmd = 'sh ./script.sh'
cmd = api.wrap_string(cmd)
print(cmd)
