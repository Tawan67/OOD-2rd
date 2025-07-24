class TorKham:

    def __init__(self):

        self.words = []
        self.play_list = []
        
   

         ### Enter Your Code Here ###

    def start(self):
        for i in self.words:
            if self.check(i)==0:
                break
            
    def restart(self):
        self.play_list.clear()
        print("game restarted")
        pass
    def set_list(self,new_list : list):
        self.words.clear()
        self.play_list.clear()
        for i in new_list:          
            self.words.append(i)
            # self.play_list.append(i)
        # print("add word",self.words)
        return 0
    def play(self, word):
        for i in word:
            if i == " ":
                com,word = word.split(" ")
                break
        
        logic = self.is_same(word)
        # print(len(self.play_list))
        
        first = 0
        if (len(self.play_list) == 0):
            self.play_list.append(word)
            print(f"'{self.play_list[0]}' -> ['{word}']")
            first = 1
            return 0
        voice = self.is_voice(word)
        if(logic==1 and voice and first == 0):
            self.play_list.append(word)     
            b=self.play_list[-1]
            print(f"'{b}' -> {self.play_list}")
            

        else:
            print(f"'{word}' -> game over")  
         ### Enter Your Code Here ###

        return "game over"
    def is_voice(self,word:str):
        after = word[0]+word[1]
        after = after.lower()
        word_checked = self.play_list[-1]
        checked=word_checked[-2]+word_checked[-1]
        checked = checked.lower()
        # print(f"input = {after} ,lastes is {checked}")
        return checked == after
    def is_same(self,word):
        
        w_check = ""
        if len(self.play_list) == 0:
            return 1
        for i in self.play_list:
            # print(i)
            # command,w_check = i.split(" ")
            w_check = i.lower()
            # print(word.lower(),"  ",w_check)
            if word.lower() == w_check.lower():
                   return 0
        return 1
    
    def check(self,words):
        for i in words:
            if i == " ":
                command,word=words.split(" ")
                break
            else:
                command = words
    
        if command=='P':
            self.play(word)
        elif command == 'R':
            self.restart()
        elif command == 'X':
            return 0
        else:
            print(f"'{words}' is Invalid Input !!!")
            return 0
        return 1
        pass


torkham = TorKham()

print("*** TorKham HanSaa ***")


S = input("Enter Input : ").split(',')
torkham.set_list(S)
torkham.start()
 ### Enter Your Code Here ###