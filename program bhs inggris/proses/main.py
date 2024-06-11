from time import sleep
from .abstrak import onTest
from .data import IO
import os

def tes(data:list):#masih kurang 2
    os.system("cls")
    print("1.inggris-indonesia\n2.indonesia-inggris\n3.v1-v2\n4.v1-v3")
    try:
        i = int(input(": "))
        if i == 1 or i ==2:
            banyakSoal = int(input(f"Banyak soal:{len(IO("database1.csv").maindata)}/ "))
            if banyakSoal > len(IO("database1.csv").maindata):
                print("Terlalu banyak soal")
                sleep(0.5)
            else:
                match i:
                    case 1:
                        ujian = IE(banyakSoal,data)
                        hasil = ujian.mainFun()
                        os.system("cls")
                        Hasil(hasil)
                        input()
                    case 2:
                        ujian = EI(banyakSoal,data)
                        hasil = ujian.mainFun()
                        os.system("cls")
                        Hasil(hasil)
                        input()
    except ValueError:
        print("yang anda masukkan bukan angka !")
        input()
        
def Hasil(hasil:int = "NONE"):#ada yang kurang
    print("="*10)
    print(f"hasil akhir anda: {hasil}")
    print("="*10)

def lihatData():
    os.system("cls")
    nd = int(input("masukkan database: "))
    if nd == 1:
        print("="*20)
        data = IO("database1.csv")
        data.lihatData()
        list = data.maindata#dibagi jadi 2 ya besok!!!
        for i in range(len(list)):
            print(f"{list[i][0]}:{list[i][1]}")
        print("="*20)
        input()  
            
def tambahData(namaDatabase:str):#perlu di tambah filter biar gak ada bug
    os.system("cls")
    data = []
    n = int(input("berapa jumlah data yang inggin dimasukkan: "))
    for i in range(n):
        os.system("cls")
        bing = input("masukkan kosakata b.ing: ")
        bindo = input("masukkan kosakata b-indo: ")
        data.append([rekonsString(bing),rekonsString(bindo)])
    IO(namaDatabase).tambahData(data)

def rekonsString(kata:str)->str: #masih gak efektif
        kataBaru = str()
        for i,data in enumerate(kata.lower().split()):
            if data != " ":
                kataBaru +=data
        return kataBaru
        
    
    

def MainMenu(data:list):
    while True:
        try:
            os.system("cls")
            print("1.test\n2.database\n3.identitas")
            cek = int(input(": "))
            if cek == 1:
                tes(data)
            elif cek ==2:
                print("1.tambah data\n2.edit data\n3.lihat data")
                i = int(input(": "))
                match i:
                    case 1:
                        namadatabase = int(input("database1/2(1/2): "))
                        if namadatabase == 1:
                            tambahData("database1.csv")
                        elif namadatabase == 2:
                            tambahData("database2.csv")
                    case 3:
                        lihatData()
                    
            elif cek == 0:
                break
        except ValueError:
            pass
            
            
        
class IE(onTest):#ontest aman
    def __init__(self, banyakSoal: int,data:list) -> None:
        super().__init__(data,IO("database1.csv").maindata, banyakSoal, 0, 1)
        
class EI(onTest):
    def __init__(self, banyakSoal: int,data:list) -> None:
        super().__init__(data,IO("database1.csv").maindata, banyakSoal, 1, 0)


