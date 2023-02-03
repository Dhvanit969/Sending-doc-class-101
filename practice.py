from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token = "tKPeIgyDHvAAAAAAAAAAAS4jiyJ1T1cAGp76SIo2yQjGN-gT9UulKFtCTShtMW-Wc"
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer:- ")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_files(file_from,file_to)
    print("File has been moved succesfully")

main()    