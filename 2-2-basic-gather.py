# การทำงงานของโปรแกรม
# โปรแกรมนี้เป็นพื้นฐานการเขียนโปรแกรมแบบ async 
# โดยมีการสร้าง Task ขึ้นมา 2 task โดน 2  Task นี้ ทำงานพร้อมกันและจบการทำงานพร้อมกัน
# เราสามารถดูที่เวลาที่ส่งออกมา

# โปรแกรมนี้ได้มีการใช้ฟังก์ชั่น gather เพื่อให้การเขียนเริ่มการทำงานแบบ async เขียนง่ายขึ้น

# ผลการรันโปรแกรม 
# Wed Jul 26 14:33:57 2023 hello 1 started
# Wed Jul 26 14:33:57 2023 hello 2 started
# Wed Jul 26 14:34:01 2023 hello 1 done
# Wed Jul 26 14:34:01 2023 hello 2 done
# Time: 4.01 sec

import asyncio
import time

async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time: {end-start:.2f} sec")