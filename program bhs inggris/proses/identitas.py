from .data import IO
import os

class Identitas():
    nama = "tidak diketahui"
    status = "tidak diketahui"
    
    def __cekIdentitas(self,nama:str,password:str) -> bool:
        self.ob = IO("databaseIdentitas.csv")
        cek_nama = False
        cek_password = False
        for i in range(len(self.ob.maindata)):
            if nama  == str(self.ob.maindata[i][0]):
                cek_nama = True
            if password == str(self.ob.maindata[i][1]):
                cek_password = True
        if (cek_nama) and (cek_password):
            return True
        else:
            return False
    def rekon(self,nama:str)->str:
        newname = ""
        for i in nama.upper().split():
            if i != " ":
                newname += i
        return newname
                
        
    
    def login(self):
        while True:
            try:
                os.system("cls")
                print("selamat datang silakan login terlebih dahulu")
                nama = input("masukkan nama anda: ")
                password = input("masukkan password anda: ")
                
                if self.__cekIdentitas(self.rekon(nama),password):
                    if password == "808":
                        status = "pengembang/operator"
                    else:
                        status = "siswa"
                    self.nama =  self.rekon(nama)
                    self.status = status
                    break
                else:
                    print("password salah atau anda tidak terdaftar!, 888 untuk daftar: ")
                    a = int(input())
                    if a == 0:
                        exit()
                    elif a == 888:
                        self.__registrasi()
            except ValueError:
                pass
            except EOFError:
                pass
                    
    def __registrasi(self):
        os.system("cls")
        try:
            nama = input("masukkan nama anda: ")
            password = input("buat password anda: ")
            if password == "808":
                self.ob.tambahData([[self.rekon(nama),password,"pengembang/operator"]])
            else:
                self.ob.tambahData([[self.rekon(nama),password,"siswa"]])
            print("registrasi berhasil (: )")
            input()
        except ValueError:
            print("registrasi gagal")
            input()
                
        
        
        