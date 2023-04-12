#get file from web url
import urllib.request

def downloadFile(url, path):
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print(e)
        print("Error downloading file: " + url)
        return False
    return True

def main():
    url = "https://www.loteria.cl/loterianet/Content/sincronizacion/Kino.xls"
    path = "C:\\Users\\camil\\OneDrive\\Documentos\\pythonFiles\\Kino.xls"
    if downloadFile(url, path):
        print("Downloaded file: " + path)
        # Path: uploadFile.py
        if uploadFile(path, "Kino.xls"):
            print("Uploaded file: " + "KN/KINO.xls")
        else:
            print("Error uploading file: " + path)



#upload file to google drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def uploadFile(path, name):
    try:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        drive = GoogleDrive(gauth)
        file = drive.CreateFile({'title': name})
        file.SetContentFile(path)
        file.Upload()
        print("Uploaded file: " + path)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()  
