def eval_object(v):
    b = {"+": v['a'] + v['b'],
         "-": v['a'] - v['b'],
         "/": v['a'] / v['b'],
         "*": v['a'] * v['b'],
         "%": v['a'] % v['b'],
         "**": v['a'] ** v['b']}
    return b[v['operation']]


print(eval_object({'a': 3, 'b': 1, 'operation': '+'}), 4)
