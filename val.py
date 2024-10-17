import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp17/weights/best.pt')
    model.val(data='dataset/my_ssdd.yaml',
              split='val',
              imgsz=640,
              batch=4,
              # rect=False,
              save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )