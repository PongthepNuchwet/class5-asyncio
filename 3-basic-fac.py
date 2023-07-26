# การทำงานของโปรแกรม 
# เป็นการคำนวน factorial ซึ่งเป็นการทำงานแบบ async 
# ซึ่งเริ่มการทำงานพร้อมกัน ที่ gather 
# แต่จบการทำงานไม่พร้อมกันเนื่องจากการทำงานแต่ละ factorial ใช้เวลาในการทำงานต่างกัน
# และทุก Task ทำงานเสร็จและแสดงผลออกมา

# ผลการรันโปรแกรม 
# Computing factorial(2), currently i=2...
# Computing factorial(3), currently i=2...
# Computing factorial(4), currently i=2...
# Computing factorial(3), currently i=3...
# Computing factorial(4), currently i=3...
# Computing factorial(4), currently i=4...
# [2, 6, 24]
# Time: 3.03 sec

import asyncio 
import time

async def factorial(n):
    f =1 
    for i in range(2,n+1) : 
        print(f"Computing factorial({n}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i 
    return f

async def main():
    L = await asyncio.gather(factorial(2),factorial(3),factorial(4))
    print(L) # [2,6,24]


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time: {end-start:.2f} sec")