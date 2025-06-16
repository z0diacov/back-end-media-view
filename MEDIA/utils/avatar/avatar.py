from PIL import Image
from config import CONVERT_FORMAT, CONVERT_RESOLUTION, CONVERT_QUALITY, BACKGROUND_COLOR

class AvatarClient:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__initialized'):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        self.__initialized = True

    def convert_to_avatar(self, input_path, output_path):
        with Image.open(input_path) as img:
            if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):

                background = Image.new("RGB", img.size, BACKGROUND_COLOR)

                background.paste(img, mask=img.split()[-1])
                img = background
            else:
                img = img.convert("RGB")

        img = img.resize(CONVERT_RESOLUTION)
        img.save(output_path, format=CONVERT_FORMAT, quality=CONVERT_QUALITY)

avatar_client = AvatarClient()
avatar_client.convert_to_avatar("test.jpg", "photo_converted.jpg")