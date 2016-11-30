import re


def is_audio(file_name):
    """
    extensions to check .mp3, .flac, .alac, or .aac.
    :param file_name:
    :return:
    """
    return True if re.match('^[A-Za-z]+((.flac)|(.mp3)|(.alac)|(.aac))$', file_name) else False


def is_img(file_name):
    """
    Extensions to check -> .jpg, .jpeg, .png, .bmp, or .gif.
    :param file_name:
    :return:
    """
    return True if re.match('^[A-Za-z]+((.jpg)|(.jpeg)|(.png)|(.bmp)|(.gif))$', file_name) else False


def is_audio_2(file_name):
    return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))


def is_img_2(file_name):
    return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))
