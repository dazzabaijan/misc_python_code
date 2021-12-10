import time
import asyncio

def sync_count():
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3')

def sync_main():
    for i in range(3):
        sync_count()

async def async_count():
    await asyncio.sleep(1)
    print('1')
    await asyncio.sleep(1)
    print('2')
    await asyncio.sleep(1)
    print('3')
    
async def async_main():
    await asyncio.gather(async_count(), async_count(), async_count())

if __name__ == '__main__':
    t = time.perf_counter()
    sync_main()
    print(f'Total time elapsed: {time.perf_counter() - t:0.2f} seconds')
    
    t = time.perf_counter()
    asyncio.run(async_main())
    print(f'Total time elapsed: {time.perf_counter() - t:0.2f} seconds')
   