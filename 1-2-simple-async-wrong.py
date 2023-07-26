
# ผลจากการรันโปรแกรม

# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.02
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.04
# Task B: Computing 1+2
# Time: 3.05
# Task B: Computing 3+3
# Time: 4.06
# Task B: Sum = 6

# Time: 5.08 sec

# การทำงานของโปรแกรม
# โปรแกรมนี้ยังคงเป็นโปรแกรมบวกเลขเหมือนกับข้อที่แล้ว โดยข้อนี้เริ่มการทำงานแบบ async 
# โดยเริ่มมีการใช้ฟังก์ชั่น create_task และสั่งทำงานโดยใช้ฟังก์ชั่น run_until_complete เมื่อ Task ทำงานเสร็จหมดแล้วจะปิดการทำงาน
# เพียงแต่คำสั่งในการ sleep ยังไม่ถูกต้อง
# ทำให้โปรแกรมทำงานแบบไม่เป็น async 

import asyncio
import time

async def sleep():
    print(f"Time: {time.time() - start:.2f}")
    time.sleep(1)

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
