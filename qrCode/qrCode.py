import qrcode

code = qrcode.make(input("What do you want to share? "))
code.save("qrrrrrr.jpg")
