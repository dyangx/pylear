import time


def consumer():
    message = ''
    while True:
        n = yield message
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(2)
        message = "200 ok"


def produce(c):
    c.__next__()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # c.close()

def run():
    c = consumer()
    produce(c)