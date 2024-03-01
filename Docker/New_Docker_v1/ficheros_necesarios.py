import os
import sql_connection

def lastRegistryFile(temp):
    if (os.path.getsize("/opt/files/lastregistry.txt") == 0) or (temp > 0):
        miConexion = sql_connection.ConexionDB()
        tempID = miConexion.lastregistry()

        with open("/opt/files/lastregistry.txt", "w") as file:
            for ID in tempID:
                file.write(str(ID) + "\n")

def newFiles():
    if not os.path.isfile("/opt/files/message.log"):
        os.system("touch /opt/files/message.log")
    
    if not os.path.isfile("/opt/files/lastregistry.txt"):
        os.system("touch /opt/files/lastregistry.txt")
    lastRegistryFile(temp = 1)

def ultimo_ID():
    lastRegistryFile(temp = 1)

    with open("prueba.txt") as archivo:
        print(archivo.readline())

if __name__ == "__main__":
    newFiles()
