import asyncio, datetime, time


async def display_date(num, loop):
    end_time = loop.time() + 10
    while True:
        print('Loop:{} Time:{} LoopTime:{} end_time:{}'.format(num, datetime.datetime.now(), loop.time(), end_time))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(2)
        # time.sleep(2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [display_date(1, loop), display_date(2, loop), display_date(3, loop)]
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()