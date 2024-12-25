from imag.imageHandler import ImageHandler
from imag.imageProcessor import ImageProcessor

def main():
    image_path = input("Введите путь к изображению (Images\\image.jpg): ")
    handler = ImageHandler(image_path)

    handler.resize_image()
    handler.save_image()

    processor = ImageProcessor(handler.process_image())
    processor.blur_image()
    processor.add_text()

    processor.image.show()
    processor.image.save("processed_image.png")
    print("Обработанное изображение, сохраненное как 'processed_image.png'.")

if __name__ == "__main__":
    main()