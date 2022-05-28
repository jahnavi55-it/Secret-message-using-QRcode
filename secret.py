# Importing library
import qrcode

# Data to be encoded
data = "Hello Asha How are You?"

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save("Secret.png")
