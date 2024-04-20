
# Training cmds:
1) git clone https://github.com/ultralytics/yolov5.git
2) cd yolov5
3) pip3 install -r requirements.txt
3) WINDOWS: pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
4) LINUX: pip3 install torch torchvision torchaudio

5) python train.py --img 1280 --epochs 80 --batch 8 --data ../dataset.yaml --weights yolov5m.pt --device 0


# Running find_couplings.py
1) pip3 install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt
2) pip3 install -r requirements.txt
3) python find_couplings.py path/to/img path/to/img2 ...


