from PIL import ImageFilter, ImageDraw, ImageFont

class ImageProcessor():
    def __init__(self, image):
        self.image = image

    def blur_image(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        print("Blur filter applied.")

    def add_text(self):
        draw = ImageDraw.Draw(self.image)
        text = "Вариант 1"
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except OSError:
            font = ImageFont.load_default()
            print("Default font used.")

        # Вычисляем размеры текста
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Определяем положение текста
        image_width, image_height = self.image.size
        position = (image_width - text_width - 10, image_height - text_height - 10)

        # Добавляем текст
        draw.text(position, text, fill=(255, 255, 255), font=font)
        print("Text added.")