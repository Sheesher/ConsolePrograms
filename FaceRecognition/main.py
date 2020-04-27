import face_recognition as fc
from PIL import Image

image = fc.load_image_file("test.jpg")
face_locations = fc.face_locations(image)

print("found {}".format(len(face_locations)))

for i in face_locations:
    top, right, bottom,left = i

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()
