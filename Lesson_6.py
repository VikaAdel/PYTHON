values = [1, 23, 42, 'asdfg']

transformed_values = list(map(lambda a: a, values))

if values == transformed_values:
    print('ok')
else:
    print('fail')