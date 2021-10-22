import asyncio
import datetime
from typing import TypedDict, Literal


async def main():
    await asyncio.create_task(say_hello())


def log(*args):
    print(f"[{datetime.datetime.now().isoformat()}]", *args)


async def say_hello():
    log("Will say hello in 2 seconds")
    await asyncio.sleep(2)
    log("Hello World")


def test(a: str) -> int:
    return 2


class Airplane(TypedDict):
    id: str
    name: str
    engine: Literal['piston', 'turbo_prop', 'jet']


if __name__ == '__main__':
    airplane = Airplane(id="id", name="Piper Pawnee", engine="piston")

    print(airplane)



