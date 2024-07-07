def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

print_kwargs(name = "pranav", power = "consistency", enemy = "phone")
print_kwargs(power = "consistency")
print_kwargs(name = "pranav")