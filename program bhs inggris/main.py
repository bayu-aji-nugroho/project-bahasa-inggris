from proses import main
from proses import identitas
import time
if __name__ == "__main__":
    a = identitas.Identitas()
    a.login()
    print(f"=====selamat datang {a.nama}=====")
    print("tunggu sebentar sedang menyiapkan...")
    time.sleep(1)
    main.MainMenu([a.nama,a.status])