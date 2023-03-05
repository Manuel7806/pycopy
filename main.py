from PIL import Image
from pytesseract import pytesseract
from glob import glob
import shutil

path_to_pytesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def set_directory(directory: str) -> str:
    """ Sets the directory to where the file will be moved to

    :param directory: The destination directory
    :type directory: str
    :returns: The name of the directory
    :rtype: str
    """
    path = r'{directory}'
    return directory


def get_name(image: Image) -> None:
    """ Get the name of the image

    :param image: The image you want to get the name of
    :type image: Image 
    :returns: The name of the image formatted to have a hyphen (-) in place of spaces
    :rtype: str
    """
    # Open the image
    img = Image.open(image)
    pytesseract.tesseract_cmd = path_to_pytesseract

    # Get the text from the image
    text = pytesseract.image_to_string(img)
    # Split the text by lines
    text = text.splitlines()
    # Get the first line of text and replace spaces with a hyphen (-)
    text = text[0].replace(' ', '-')

    # Prefix the text with a forward slash (\)
    text = f'\{text}.png'
    return text


def get_full_path(directory: str, image: Image) -> str:
    """ Returns the directory path along with the name of the image

    :param directory: The destination directory
    :type directory: str
    :param image: The image you want to get the name of
    :type image: Image
    :returns: The directory path with the image name appended to the end of it EX: (path/to/dst/foo.jpg)
    :rtype: str
    """
    path = set_directory(directory) + get_name(image)
    return path


def copy(src: str, dest: str) -> None:
    """ Copies a file from one destination to another

    :param src: The source directory/file
    :type src: str
    :param dest: The destination directory
    :returns: None
    :rtype: None
    """
    for image in glob(src):
        shutil.copy(image, get_full_path(dest, image))


copy(r'4K\Screenshot*.png', '4K-COPY')
