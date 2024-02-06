#a python program to generate qr code and decode qr code.

import qrcode
import cv2
    
def main():
    op = input("Enter your choice 1 for generate 2 for decode 3 for webcam decode: ")
    if(op == '1'):
        encodeQr()
    elif(op == '2'):
        decodeQr()
    elif(op == '3'):
        wcamQrDecode()
    else:
        return
    main()

def encodeQr():
    qrdata = input("Enter the qr data: ")
    qrfilename = input("Enter the file name: ")
    qrimg = qrcode.make(qrdata)
    qrimg.save(f"{qrfilename}.png")

def wcamQrDecode():
    # initalize the camera
    cap = cv2.VideoCapture(0)

    # initialize the OpenCV QRCode detector
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()

        # detect and decode
        data, vertices_array, _ = detector.detectAndDecode(img)

        # check if there is a QRCode in the image
        if vertices_array is not None:
            if data:
                print("QR Code detected, data:", data)
                break

        # display the result
        cv2.imshow("img", img)

        # Enter q to Quit
        if cv2.waitKey(1) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def decodeQr():
    qrfilename = input("Enter the file name: ")
    image = cv2.imread(qrfilename)
    detector = cv2.QRCodeDetector()
    try:
        data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    except:
        print("Error Detected.")
        return
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
    else:
        print("There was some error")

if __name__ == '__main__':
    main()
    print("Program End.")