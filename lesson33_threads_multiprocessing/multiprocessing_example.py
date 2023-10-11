from multiprocessing import Pool, Process, Queue, Lock


def f(x):
    return x * x


def other_ord_func(q):
    q.put([42, None, 'Mr.Hello'])


def func_to_test_lock(l, x):
    l.acquire()
    try:
        print(f'Hello Mr.{x}, welcome back')
    finally:
        l.release()


if __name__ == '__main__':

    '''
    with Pool(10) as p:
        result = p.map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(result)
    '''

    l = Lock()
    for number in range(15):
        pr = Process(target=func_to_test_lock, args=(l, number))
        pr.start()

    '''
    proc = Process(target=f, args='Johnathan')
    proc.start()
    proc.join()
    q = Queue()
    p = Process(target=other_ord_func, args=(q,))
    p.start()
    print(q.get())
    p.join()
    '''
