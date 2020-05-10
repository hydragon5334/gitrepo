def log(f):
    def wrapper(*args,**kw):
        print('call %s():' % f.__name__ )
        return f(*args,**kw)
    return wrapper

@log
def now():
    print('123')

now()
