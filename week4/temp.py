def flood_fill(grid, r, c, current_height):
    R = len(grid)
    C = len(grid[0])

    # ถ้าออกนอกขอบเขต แปลว่าทำอะไรไม่ได้
    if r < 0 or r >= R or c < 0 or c >= C:
        return

    # ถ้าช่องนี้สูงกว่าระดับที่ไหลไปได้ ก็หยุด
    if grid[r][c] > current_height:
        return

    # ถ้าช่องนี้ถูกท่วมแล้ว ก็หยุด
    if grid[r][c] == 0:
        return

    # จำความสูงของจุดนี้ไว้ (เพื่อให้เพื่อนบ้านใช้เป็น current_height)
    h = grid[r][c]

    # ทำให้ช่องนี้กลายเป็น 0 (น้ำท่วม)
    grid[r][c] = 0

    # ไหลไปเพื่อนบ้านทั้ง 4 ทิศ (บน ล่าง ซ้าย ขวา)
    flood_fill(grid, r-1, c, h)  # บน
    flood_fill(grid, r+1, c, h)  # ล่าง
    flood_fill(grid, r, c-1, h)  # ซ้าย
    flood_fill(grid, r, c+1, h)  # ขว


# ----------------- รับ Input ตามรูปแบบโจทย์ -----------------
raw = input().strip()  # เช่น 5,5/13361,86412,83455,09591,34223/2,2
size_str, map_str, start_str = raw.split("/")

R, C = map(int, size_str.split(","))
rows = map_str.split(",")
start_r, start_c = map(int, start_str.split(","))

# แปลงเป็น list[int]
grid = [[int(ch) for ch in row] for row in rows]

# เรียก Recursion เริ่มจากจุดเริ่มต้น
flood_fill(grid, start_r, start_c, grid[start_r][start_c])

# แสดงผลลัพธ์
for row in grid:
    print("".join(map(str, row)))
