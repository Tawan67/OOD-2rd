import time

for i in range(10):
    print(f"Loading... {i*10}%", end="\r")
    time.sleep(0.5)
# print(chr(27))
# print("a")
