import os
from PIL import Image
from torchvision import transforms

import torch


def convert_to_grayscale_3ch(filename: str):
    image = Image.open(filename)
    grayscale_transform = transforms.Grayscale(num_output_channels=3)
    grayscale_image = grayscale_transform(image)
    return grayscale_image



def convert_dir_to_grayscale_3ch(directory: str, save_directory: str):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            path = os.path.join(directory, filename)
            grayscale_image = convert_to_grayscale_3ch(path)
            grayscale_path = os.path.join(save_directory, f"{filename}")
            grayscale_image.save(grayscale_path)


if __name__ == '__main__':
    # convert_dir_to_grayscale_3ch("datasets/coupling/validation", "datasets/coupling/validation")
    # convert_dir_to_grayscale_3ch("datasets/coupling/testing", "datasets/coupling/testing")
    # convert_dir_to_grayscale_3ch("datasets/coupling/training", "datasets/coupling/training")

    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))
