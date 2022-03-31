from datetime import datetime
import numpy as np
import cv2


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background():
    return np.zeros((500, 500))


def generate_time_image_bytes(dt):
    text = convert_time_to_string(dt)
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    textsize = cv2.getTextSize(text, font, 3, 3)[0]
    username = '@n_777_n'
    cv2.putText(image, text, (int((image.shape[1] - textsize[0]) / 2), int((image.shape[0] + textsize[1]) / 2)), font, 3, (255, 255, 0), 3, cv2.LINE_AA)
    cv2.putText(image, username, (int(image.shape[0] * 0.52),int(image.shape[1] * 0.65)), font, 0.7, (255, 255, 0), 1, cv2.LINE_AA)
    cv2.imwrite(f'img.jpg', image)
    return 'img.jpg'