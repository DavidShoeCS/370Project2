import pyotp
import time
import qrcode
import sys



def generate_qr(totp):

    uri = totp.provisioning_uri("project2@google.com", issuer_name = "370Class")

    qrCode = qrcode.make(uri)
    qrCode.save('QRCode.jpg')
    print("QRCode generated")


    return totp

def get_otp(oneTimePass):

    while True:
        print("Current OTP: " + str(oneTimePass.now()))
        print()
        time.sleep(30)


def main():

    secretKey = "HLNGHBEKFHFKDUEF"

    totp = pyotp.TOTP(secretKey)

    argument = sys.argv[1]


    if argument == "--get-otp":
        get_otp(totp)
    elif argument == "--generate-qr":
        generate_qr(totp)
    else:
        print("Command not recognized, try again.")

if __name__ == "__main__":
    main()
