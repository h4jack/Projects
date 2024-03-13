# Import the required modules
from pdf2docx import Converter
from sys import argv, exit
from os.path import * 
from ptdhelp import *
from glob import glob

# from spire.doc import Document
# from spire.doc.common import *





def main():
    paths = []
    for i in argv[1:]:
        paths.extend(glob(i))

    for path in paths:
        if(exists(path)):
            i = 0
            filename, extension = splitext(path)
            if(extension == '.pdf'):
                newfilename = f"{filename}.docx"
                while(exists(newfilename)):
                    newfilename = f"{filename}_{i}.docx"
                    i+=1
                convertpd(path, newfilename)
            elif(extension == '.docx'):
                # newfilename = f"{filename}.pdf"
                # while(exists(newfilename)):
                #     newfilename = f"{filename}_{i}.pdf"
                #     i+=1
                # convertdp(path, newfilename)
                print("[UNAVAILABLE] This won't work for DOCX file please wait for future update..")
                continue
            else:
                print(f"The extension of file: '{path}' is not .pdf")
                continue
        else:
            print(f"The file: '{path}' doesn't exists.")


def convertpd(pdf_file, docx_file):
    print("Converting PDF to DOCX...")
    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        print(f"[SAVED] File Saved: '{docx_file}'")
        cv.close()
    except:
        print("[FAILED] Convertion Field...")
        return False
    return True

# def convertdp(docx_file, pdf_file):
#     print("Converting DOCX to PDF...")

#     try:
#         print(f"[CONVERTING] Started Convertion of file: '{docx_file}'")
    
#         document = Document()
#         document.LoadFromFile(docx_file)

#         pdf_options = PdfSaveOptions()
#         document.SaveToFile(pdf_file, pdf_options)

#         print(f"[SAVED] File Saved: '{docx_file}'")
#         document.Close()
#     except:
#         print("[FAILED] Convertion Field...")
#         return False
#     return True

def checkError(l):
    if(l < 2):
        print_error("Argument Required.")
        print_usage()
        return False
    elif(l == 2):
        if( argv[1] in ("help", "-h", "--help", "h") ):
            print_help()
            return False
        # elif not exists(argv[1]):
        #     print_error(f"the argument '{argv[1]}' is not recognized.")
        #     print_usage()
    return True

if __name__ == '__main__':
    l = len(argv)
    if not checkError(l):
        exit()
    main()