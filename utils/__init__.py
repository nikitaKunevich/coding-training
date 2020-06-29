import time
def measure(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % \
                  (method.__name__, (te - ts) * 1000))
        return result
    return timed

def measure_avg(method, times=1000):
    def timed(*args, **kw):
        from statistics import mean
        vals = []
        for _ in range(times):
            ts = time.time()
            result = method(*args, **kw)
            te = time.time()
            vals.append(te - ts)
        value = mean(vals)
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int(value * 1000)
        else:
            print('%r  %2.5f ms' % \
                  (method.__name__, value * 1000))
        return result
    return timed