def log(f):
    def wrapper(*args,**kw):
        print('call %s():' % f.__name__ )
        return f(*args,**kw)
    return wrapper

@log
def now():
    print('123')

now()

def log(text):
    def decorator(f):
        def wrapper(*args,**kw):
            print('%s %s():' %(text,f.__name__))
            return f(*args,**kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('123')

now()

