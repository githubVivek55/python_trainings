# AsyncIO
# Concurrency
# Parallelism

# https://realpython.com/python-concurrency/

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    await asyncio.gather(
        say_after(1, "Hello"),
        say_after(2, "World"),
        say_after(3, "!")
    )
    print("All tasks completed")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Completed in {end_time - start_time} seconds")