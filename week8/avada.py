
# หาจำนวนช่วงที่ยาวที่สุดขั้นต่ำ (minimize maximum period)
# และคืนการแบ่งเป็น k ช่วงต่อเนื่อง (list of lists)
from typing import List, Tuple

def can_split(times: List[int], k: int, limit: int) -> bool:
    """ตรวจสอบว่าเราสามารถแบ่งเป็น <= k ช่วง โดยแต่ละช่วง sum <= limit"""
    groups = 1
    cur = 0
    for t in times:
        if cur + t <= limit:
            cur += t
        else:
            groups += 1
            cur = t
            if groups > k:
                return False
    return True

def min_max_period(times: List[int], k: int) -> int:
    """Binary search เพื่อหาค่า min possible max period"""
    low = max(times)          # ต้องไม่น้อยกว่าบทเรียนที่ยาวที่สุด
    high = sum(times)
    while low < high:
        mid = (low + high) // 2
        if can_split(times, k, mid):
            high = mid
        else:
            low = mid + 1
    return low

def partition_into_k(times: List[int], k: int, limit: int) -> List[List[int]]:
    """
    สร้างการแบ่งจริง ๆ ให้ได้ exactly k groups โดยใช้ limit เป็น max allowed sum.
    ทำแบบย้อนจากขวาเพื่อรับประกันว่าได้ k กลุ่ม (และไม่เกิน limit).
    """
    n = len(times)
    groups: List[List[int]] = []
    cur_group: List[int] = []
    cur_sum = 0
    remaining = k
    # เดินจากขวาไปซ้าย
    for i in range(n - 1, -1, -1):
        t = times[i]
        # ถ้าใส่ t ลงไปแล้วเกิน limit หรือจำนวนรายการที่เหลือต้องแยกให้พอดีกับ remaining groups
        if cur_sum + t > limit or i + 1 < remaining:
            # ปิดกลุ่มปัจจุบัน แล้วเริ่มกลุ่มใหม่
            groups.append(list(reversed(cur_group)))  # กลับลำดับเพราะเราเก็บย้อน
            cur_group = [t]
            cur_sum = t
            remaining -= 1
        else:
            cur_group.append(t)
            cur_sum += t
    # เพิ่มกลุ่มสุดท้าย
    groups.append(list(reversed(cur_group)))
    # ผลลัพธ์ตอนนี้เป็นจากขวา->ซ้าย (reverse เพื่อได้ลำดับเดิม)
    groups = list(reversed(groups))
    return groups

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    tests = [
        ([30, 45, 20, 25, 50], 3),
        ([10,20,30,40,50], 2),
        ([15,15,15,15,15,15], 3),
        ([60,50,40,30,20,10], 4),
        ([5,10,5,10,5,10,5,10], 4),
        ([100,50,50,50,50,50], 3),
        ([7,3,2,5,8,6,4,1], 3),
        ([10,20,30,40,50,60], 5),
    ]

    for idx, (times, k) in enumerate(tests, start=1):
        mm = min_max_period(times, k)
        groups = partition_into_k(times, k, mm)
        sums = [sum(g) for g in groups]
        diff = mm - min(sums) if sums else 0
        print(f"Testcase : #{idx}")
        print("*** CLASS SCHEDULE ***")
        print("Lesson times / periods:", " ".join(map(str, times)), "/", k)
        print("Max period:", mm)
        print("Diff:", diff)
        print("Groups:")
        for i, g in enumerate(groups, start=1):
            print(f"  Group {i}: {g} → sum = {sum(g)}")
        print()

