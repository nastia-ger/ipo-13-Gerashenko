from PIL import Image

class ImageHandler():
    def __init__(self, image):
        self.image = image

    def resize_image(self, size=(300, 300)):
        self.image = Image.open('image_1.jpg')
        self.image = self.image.resize(size)
        print(f"Image resized to {size[0]}x{size[1]} pixels.")

    def save_image(self, filename="output.png"):
        self.image.save(filename, "PNG")
        print(f"Image saved as {filename}.")

    def process_image(self):
        return self.image