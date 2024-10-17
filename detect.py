import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp44/weights/best.pt') # select your model.pt path
    model.predict(source='dataset/SSDD/images/val',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                  # conf=0.2,
                  # visualize=True # visualize model features maps
                )