import sys
import torch

from image_transform import convert_to_grayscale_3ch


def get_x_center(xmin, xmax):
    x_center = (xmin + xmax) / 2
    return x_center


def find_couplings(*image_paths):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='models/my_yolov5m.pt')

    for im in image_paths:
        convert_to_grayscale_3ch(im)
        results = model(im, size=1280)
        pd_res = results.pandas().xyxy[0]
        for detection in pd_res.itertuples():
            print(get_x_center(xmin=detection.xmin, xmax=detection.xmax))


if __name__ == "__main__":
    find_couplings(*sys.argv[1:])
