import asyncio, time


async def do_some_work(x):
    print('Waiting:', x)


a = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(do_some_work(2))
print('time:{}'.format(time.time() - a))

print('\ncreate a task')


async def do_some_work2(x):
    print('Waiting:{}'.format(x))


b = time.time()
loop = asyncio.get_event_loop()
task = loop.create_task(do_some_work2(2))
print(task)
loop.run_until_complete(task)
print(task)
print('time:{}'.format(time.time() - b))

print('\nbundle callback')


async def do_some_work3(x):
    print('Waiting:{}'.format(x))
    return 'Done after {}s'.format(x)


def callback(future):
    print('Callback:{}'.format(future.result()))


c = time.time()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(do_some_work3(2))
task.add_done_callback(callback)
loop.run_until_complete(task)
print('time:{}'.format(time.time() - c))

print('\nfuture and result')


async def do_some_work4(x):
    print('Waiting {}'.format(x))


d = time.time()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coro_or_future=do_some_work4(2))
loop.run_until_complete(task)
print('Task ret:{}'.format(task.result()))
print('time:{}'.format(time.time() - d))

print('\nawait')


async def do_some_work5(x):
    print('Waiting:{}'.format(x))
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


e = time.time()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coro_or_future=do_some_work5(2))
loop.run_until_complete(task)
print('Task ret:'.format(task.result()))
print('time:{}'.format(time.time() - e))

print('\nconcurrent and parallel')


async def do_some_work6(x):
    print('waiting:{}'.format(x))
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


f = time.time()
tasks = [asyncio.ensure_future(coro_or_future=do_some_work6(1)), asyncio.ensure_future(coro_or_future=do_some_work6(2)),
         asyncio.ensure_future(coro_or_future=do_some_work6(3))]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('task ret:{}'.format(task.result()))
print('time:{}'.format(time.time() - f))