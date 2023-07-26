# การทำงานของโปรแกรม
# โปรแกรมนี้ยังเป็นการบวกเลขเหมือนเดิมที่เป็นแบบ async แต่เปลี่ยนวิธีการเขียนโปรแกรมใหม่โดยการใช้ฟังก์ชั่น
# gather ซึ่งเป็นการทำงานแบบ async

# 
# ผลจากการรันโปรแกรม
# Task A: Computing 0+1
# Time: 0.01
# Task B: Computing 0+1
# Time: 0.01
# Task A: Computing 1+2
# Time: 1.03
# Task B: Computing 1+2
# Time: 1.03
# Task A: Sum = 3

# Task B: Computing 3+3
# Time: 2.04
# Task B: Sum = 6

# Time: 3.06 sec

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

async def main():
    await asyncio.gather(sum("A",[1,2]),sum("B",[1,2,3]))

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time: {end-start:.2f} sec")
