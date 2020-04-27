import requests
outputName = input("Enter a output name: ")
inputName = input("Enter the URL to the image: ")

if inputName.endswith(('jpg')) or ".jpg" in inputName:
    f = open(outputName + '.jpg', 'wb')
elif inputName.endswith(('png')) or ".png" in inputName:
    f = open(outputName + '.png', 'wb')
else:
    print("Only *.png and *.jpg images be valid!")

f.write(requests.get(inputName).content)

f.close()
