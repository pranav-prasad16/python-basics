
def custom(func):
    def wrapper(*args, **kwargs):
        arg_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{key} : {value}' for key, value in kwargs.items())
        print(f'Calling {func.__name__} with args: {arg_value} and kwargs: {kwargs_value}')
        return func(*args, **kwargs)
    return wrapper

@custom
def hello():
    print('Hello')

@custom
def greet(name, greeting = "Greetings"):
    print(f'{greeting}! {name}')

hello()
greet('pranav')
greet('pranav', greeting = 'Yo')