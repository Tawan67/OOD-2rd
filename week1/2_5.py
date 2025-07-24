# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

# 1. หาความยาวของ String

# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

# 3. Reverse String (ห้ามใช้คำสั่ง reversed)

# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String



class funString():

    def __init__(self,string = None):
        if string == None:
            string = ""
        self.string = string
        pass
        ### Enter Your Code Here ###

    def __str__(self):
        pass
        ### Enter Your Code Here ###

    def size(self) :
        size = 0
        for i in self.string:
            size+=1
        return size
        pass
        ### Enter Your Code Here ###

    def changeSize(self):
        new_str = []
        for i in self.string:
            if ord(i)>=ord('a') and ord(i)<=ord('z'):
                new_str.append(chr(ord(i)-32))
                # print(chr(ord(i)-32))
            elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
                new_str.append(chr(ord(i)+32))
                # print(chr(ord(i)+32))
        return "".join(new_str)
        pass
        ### Enter Your Code Here ###

    def reverse(self):
        char_list = list(self.string)
        new_list = []
        for i in range(len(char_list)-1,-1,-1):
            new_list.append(char_list[i])
        return "".join(new_list)
        pass
        ### Enter Your Code Here ###

    def deleteSame(self):
        new_list = []
        for i in self.string:
            if not i in new_list:
                new_list.append(i)
        return "".join(new_list)
        pass
       ### Enter Your Code Here ###



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())