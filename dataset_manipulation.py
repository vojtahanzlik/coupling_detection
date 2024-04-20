import json
import os
import shutil


def remove_file_extension(filename: str):
    name, _ = os.path.splitext(filename)
    return name


def points_to_yolo_txt(points: list, save_directory: str, img_width=2048, img_height=1536, obj_class=0):
    with open(f"{save_directory}.txt", 'w') as file:
        x_coords = [point[0] for point in points]
        y_coords = [point[1] for point in points]

        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)

        width = max_x - min_x
        height = max_y - min_y

        x_center = (min_x + max_x) / 2
        y_center = (min_y + max_y) / 2

        x_center /= img_width
        y_center /= img_height
        width /= img_width
        height /= img_height
        file.write(f"{obj_class} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")


def json_to_yolo_format(directory: str, save_directory: str):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)

            with open(file_path, 'r') as file:
                filename = remove_file_extension(filename)

                data = json.load(file)
                bb_points = [point for point in data["shapes"][0]["points"]]
                output_path = os.path.join(save_directory, f"{filename}")
                points_to_yolo_txt(bb_points, output_path)


def move_json_if_jpeg_exists(source_dir: str, target_dir: str):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for filename in os.listdir(source_dir):
        if filename.endswith('.json'):
            json_path = os.path.join(source_dir, filename)

            jpeg_filename = os.path.splitext(filename)[0] + '.jpeg'
            jpeg_path = os.path.join(target_dir, jpeg_filename)

            jpg_filename = os.path.splitext(filename)[0] + '.jpg'
            jpg_path = os.path.join(target_dir, jpg_filename)

            if os.path.exists(jpeg_path) or os.path.exists(jpg_path):
                shutil.move(json_path, os.path.join(target_dir, filename))


if __name__ == '__main__':
    json_to_yolo_format("datasets/coupling/validation", "datasets/coupling/validation")
    json_to_yolo_format("datasets/coupling/training", "datasets/coupling/training")
    json_to_yolo_format("datasets/coupling/testing", "datasets/coupling/testing")

    #move_json_if_jpeg_exists("car_coupling_train/v5", "datasets/coupling/training")
    #move_json_if_jpeg_exists("car_coupling_train/v5", "datasets/coupling/testing")
    #move_json_if_jpeg_exists("car_coupling_train/v5", "datasets/coupling/validation")

