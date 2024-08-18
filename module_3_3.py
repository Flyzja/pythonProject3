def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(9, 8, 6)
print_params('строка', True,1)
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [5, True, 'False']
values_dict = {'a': 'строка', 'b': True, 'c': 1}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7.84, 'опочки']
print_params(*values_list_2, 42)

print_params(7, 8, 6, 3)