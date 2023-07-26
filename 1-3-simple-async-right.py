# การทำงานของโปรแกรม
# โปรแกรมนี้ยังเป็นโปรแกรมบวกเลขเหมือนเดิมโดยแก้ไขข้อผิดพลาดของข้อ 2 ที่ใช้ฟังก์ชั่น sleep ยังไม่ถูกต้อง
# โดยโปรแกรมนี้เรียกใช้ฟังก์ชั่น await asyncio.sleep(1) ซึ่งเป็นการ sleep ที่ถูกต้อง
# และการทำงานเป็นแบบ async
# ผลจากการรันโปรแกรม
# Task A: Computing 0+1
# Time: 0.00
# Task B: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task B: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.02
# Task B: Sum = 6

# Time: 3.04 sec

import asyncio
import time

async def sleep():
    print(f"Time: {time.time() - start:.2f}")
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f"Task {name}: Computing {total}+{number}")
        await sleep()
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
