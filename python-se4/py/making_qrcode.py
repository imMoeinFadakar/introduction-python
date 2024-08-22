import qrcode


username = str(input("enter Your name:"))
password = int(input("Enter your number:"))

content_inside_the_qrcode = username , password


print(content_inside_the_qrcode)

user_qrcode_image = qrcode.make(content_inside_the_qrcode)
user_qrcode_image.save("user_qrcode.png")





