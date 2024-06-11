"menanggani data input dan ouput"

import csv
from abc import ABC


class IO(ABC):
    maindata = []
    def __init__(self,File:str) -> None:
        self.__File = File
        self.__read()
    
    
    def __read(self):
        self.maindata.clear()
        with open(self.__File,mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.maindata.append(row)
                
    def tambahData(self,newData:list):
        with open(self.__File,mode="a",newline="") as file:
            writter = csv.writer(file)
            writter.writerows(newData)
        self.__read()
        
    def lihatData(self):
        self.__read()
        
        
        
    def editData(self,newMainData:list):
        with open(self.__File,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerows(newMainData)
        self.__read()
        
    
            
                    
            

