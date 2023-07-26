# 1-1-sample-sync.py
# โปรแกรมทำงานอย่างไร
# เป็นโปรแกรมบวกเลข โดยกระบวนการเริ่มจากการ สร้าง Tasks ที่เป็นลำดับจากนั้นทำการคำนวนโดยเรียกฟังก์ชั่น sum โดยแต่ละ tasks ได้กำหนดชื่อของ task และตัวเลขที่เราต้องการคำนวน
# ในขั้นตอนการบวกเลขจะแสดงให้เห็นถึงเวลาที่คำนวนในขณะนั้น โดยจะบวกทีละเลข โดยแต่ละการบวกจะใช้เวลา 1 second
# และสุดท้ายแสดงเวลาที่โปรแกรมทำงาน

# ผลที่ได้จากการรัน
# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 1+2
# Time: 1.01
# Task A: Sum = 3

# Task B: Computing 0+1
# Time: 2.02
# Task B: Computing 1+2
# Time: 3.04
# Task B: Computing 3+3
# Time: 4.05
# Task B: Sum = 6

# Time: 5.05 sec
import time


def sleep():
    print(f"Time: {time.time() - start:.2f}")
    time.sleep(1)

# ฟังก์ชั่นนี้เป็นการบวกเลขตามจำนวนตัวเลขที่ส่งเข้ามาโดยการบวกแต่ละเลขจะใช้เวลา 1 second
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f"Task {name}: Computing {total}+{number}")
        sleep()
        total += number

    # ส่งออก ชื่อ Task และผลรวมของตัวเลข
    print(f"Task {name}: Sum = {total}\n")


start = time.time()

# สร้าง Task สำหรับการบวกเลขเป็นลำดับจาก code เรามี 1 Task คือ A และ B
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f"Time: {end-start:.2f} sec")
