# การทำงานของโปรแกรม
# โปรแกรมนี้ยังเป็นการบวกเลขเหมือนเดิมที่เป็นแบบ async
# แต่ปัญหาของโจทน์นี้คือเมื่อฟังก์ชั่นหรือ Lib ไม่ได้เป็นแบบ async และเราไม่ต้องการแก้ไข Code
# ดังนั้นเราจึงใช้ thread เมื่อให้ฟังก์ชั่นที่ไม่ใช่ async สามารถทำงานแบบ async  ได้

# 
# ผลจากการรันโปรแกรม
# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Task B: Computing 1+2
# Time: 1.01
# Time: 1.01
# Task B: Computing 3+3
# Task A: Sum = 3

# Time: 2.02
# Task B: Sum = 6

# Time: 3.03 sec

import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor

def sleep():
    print(f"Time: {time.time() - start:.2f}")
    time.sleep(1)

async def sum(name, numbers):
    _executor = ThreadPoolExecutor(2)
    total = 0
    for number in numbers:
        print(f"Task {name}: Computing {total}+{number}")
        await loop.run_in_executor(_executor,sleep)
        total += number
    print(f"Task {name}: Sum = {total}\n")

start = time.time()
loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time()
print(f"Time: {end-start:.2f} sec")
