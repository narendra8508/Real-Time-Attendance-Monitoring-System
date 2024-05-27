import cv2
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize

def cvtransform(piltransform): 
    return Compose([
        _convert_image_to_rgb,
        ToTensor(),
        piltransform[0],
        piltransform[1],
        piltransform[4],
    ])

def _convert_image_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)