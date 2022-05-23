import asyncio
async def x(i):
    await asyncio.sleep(i)
    print(i)
    return i

async def main(N):
    for f in asyncio.as_completed([x(i) for i in N]):
        result = await f

if __name__ == '__main__':
    N = list(map(int, input().split()))
    print(N)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(N))
    loop.close()