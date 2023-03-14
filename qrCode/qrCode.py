import qrcode

code = qrcode.make(input("Ce doresti sa fie afisat? "))
code.save("qrrrrrr.jpg")
