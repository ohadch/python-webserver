import asyncio
import datetime


def log(*args):
    print(f"[{datetime.datetime.now().isoformat()}]", *args)


async def say_hello():
    log("Will say hello in 2 seconds")
    await asyncio.sleep(2)
    log("Hello World")


if __name__ == '__main__':
    asyncio.run(say_hello())
