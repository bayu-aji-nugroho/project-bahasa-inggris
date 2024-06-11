try:
    with open("database1.csv","r") as file:
        pass
    with open("database2.csv","r") as file:
        pass
    with open("databaseIdentitas.csv","r") as file:
        pass
except FileNotFoundError:
    with open("database1.csv","w",newline="") as file:
        pass
    with open("database2.csv","w",newline="") as file:
        pass
    with open("databaseIdentitas.csv","w",newline="") as file:
        pass