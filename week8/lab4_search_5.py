def can_split(times, k, limit):
    groups = 1
    cur = 0
    for t in times:
        if t > limit:
            return False

    for t in times:
        if cur + t <= limit:
            cur += t
        else:
            groups += 1
            cur = t
            if groups > k:
                return False
    return True

def min_max_period(times, k):

    # if not times:
    #     return 0
    # if k <= 0:
    #     return sum(times) 
    
    low = max(times)
    high = sum(times)

    result = high 

    while low <= high:
        mid = (low + high) // 2
        if can_split(times, k, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1
    return result

def partition_exact_k(times, k, limit):
    """แบ่งรายการ times ออกเป็น k กลุ่มให้ได้ผลรวมไม่เกิน limit"""
    if not times or k <= 0:
        return []
    
    # 1) left->right greedy to get minimal groups (len(groups) <= k)
    groups = []
    cur = []
    cur_sum = 0
    for t in times:
        if cur_sum + t <= limit:
            cur.append(t)
            cur_sum += t
        else:
            groups.append(cur)
            cur = [t]
            cur_sum = t
    if cur:
        groups.append(cur)

    if len(groups) > k:
        return []

    # 2) if we need more groups (len(groups) < k), split groups until reach k
    i = 0
    while len(groups) < k and i < len(groups):
        if len(groups[i]) > 1:
            x = groups[i].pop() 
            groups.insert(i + 1, [x])
        else:
            i += 1 

    return groups
def min_sum_li(groups):
    cur = sum(groups[0])
    for i in groups:
        if sum(i) < cur:
            cur = sum(i)
    return cur    
# ส่วนหลักของการทำงาน (ใช้ input ที่คุณกำหนด)
def main():
    print("*** CLASS SCHEDULE ***")
    input_line = input("Lesson times / periods: ")
    inp, max_str = input_line.split("/")
    k = int(max_str)
    times = [int(i) for i in inp.split(" ") if i]
    

    limit = min_max_period(times, k)
    groups = partition_exact_k(times, k, limit)
    min_value = min_sum_li(groups)
    # print(groups,limit,min_value,limit-min_value)
    print(f"Max period: {limit}")
    print(f"Diff: {limit-min_value}")
    print("Groups:")
    for i in range(len(groups)):
        print(f"  Group {i+1}: {groups[i]} → sum = {sum(groups[i])}")


        
main()