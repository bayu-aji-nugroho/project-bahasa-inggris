import random
import os
from time import sleep

class onTest():
    __poin = 0
    __poinSalah = 0
    
    def __init__(self,data:list,database:list,banyakSoal:int,indexJawaban:int,IndexSoal:int) -> None:
        self.__Database = database
        self.__banyakSoal = banyakSoal
        self.__indexJawaban = indexJawaban
        self.__IndexSoal = IndexSoal
        self.__data = data
    
    def __generateNUmber(self):
        data = []
        while True:
            i =  random.randint(0,self.__banyakSoal) # [0,banyak soal]
            if i not in data and i < self.__banyakSoal:
                data.append(i)
            elif len(data) == self.__banyakSoal:
                break 
        return data
    
    def mainFun(self) -> int:
        try:
            if len(self.__generateNUmber()) == 0:
                return "data kosong"
            else:
                for index,data in enumerate(self.__generateNUmber()):
                    os.system("cls")
                    print("="*20)
                    print(f"jumlah soal: {self.__banyakSoal}")
                    print(f"nama peserta : {self.__data[0]} status: {self.__data[1]}")
                    print(f"nilai sementara: {(self.__poin/self.__banyakSoal)*100} |{self.__statistik()}")
                    print("="*20)
                    print(f"{index+1}. apa terjemahan dari {self.__Database[data][self.__IndexSoal]}")
                    jawaban = input(": ")
                    if jawaban == self.__Database[data][self.__indexJawaban]:
                        self.__poin += 1
                    else:
                        self.__poinSalah +=1
                        print(f"jawaban salah! {self.__Database[data][self.__IndexSoal]} = {self.__Database[data][self.__indexJawaban]}")
                        sleep(1)
                return (self.__poin/self.__banyakSoal)*100
        except IndexError:
            print(data)
            return "gagal!"
        except EOFError:
            return "tidak ada karena anda mengakhiri Test"
        
        
    def __statistik(self) -> str:
        if self.__poinSalah == 0:
            return "sempurna"
        elif (self.__poinSalah == int((1/2)*self.__banyakSoal)) and (self.__banyakSoal%2 == 0):
            return "setengah soal telah SALAH!"
        elif self.__poinSalah == int((1/4)*self.__banyakSoal) and (self.__banyakSoal%2 == 0):
            return "ayo berlatih lagi!"
        elif( self.__poinSalah == self.__banyakSoal-1) and (self.__banyakSoal >5):
            return "MEMALUKAN!!!"
        else:
            return f"anda telah salah {self.__poinSalah} kali!"
        
        
        
    
        
    

        
    