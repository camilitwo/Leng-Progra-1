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

if __name__ == "__main__":
    main()  
