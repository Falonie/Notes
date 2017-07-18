import time,logging

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            # print(fmt.format(**locals()))
            logging.warning(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds, x, y):
        time.sleep(seconds)
        return seconds + x, y

    for i in range(3):
        snooze(.123, 10, 'Falonie')
        # print(snooze(.123, 10, 'Falonie'))

# print(repr('22'),'22',True)
# print(','.join(repr(i) for i in ['e',3]))