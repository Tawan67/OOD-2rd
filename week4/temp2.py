def fibo(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

memo_purity = {}

def purity(n, w):
    if w <= 0:
        return -1
    if n == 1:
        return w

    c = fibo(n-1)
    best = -1
    for total in range(2*w - c, 2*w + 2 - c):
        if total < 2:
            continue
        
        a = total // 2
        b = total - a
        
        res_a = purity(n-1, a)
        res_b = purity(n-1, b)
        
        if res_a != -1 and res_b != -1:
            candidate = res_a + res_b
            if candidate > best:
                best = candidate

    return best


# ทดสอบ
n, w = map(int, input("Enter n,w: ").split(","))
ans = purity(n, w)
print(f"Purity and Weight needed: {n} {w}")
print(f"Total weight of used minerals with Purity 1 : {ans}")
