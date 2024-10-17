import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    #model = YOLO('ultralytics/cfg/models/v8/yolov8-RCSOSA+TADDH+AIFI+SPDConv1cpca+ADown.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPDConvxia-RCSOSAxia.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-RCSOSA+TADDH+AIFI+SPDConv12cpca.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-ADown-dyhead.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPPF-LSKA.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPPF-LSKA+dyhead.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPDConv-RCSOSA.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPDConv-RCSOSA-AIFI.yaml')
    #model = YOLO('ultralytics/cfg/models/v8/yolov8n-SPPF-LSKA+slimneck.yaml')
    model = YOLO('ultralytics/cfg/models/v8/yolov8n-slimneck+dyhead.yaml')
    #model.load('runs/train/exp33/weights/best_rep.pt') # loading pretrain weights
    model.train(data='dataset/my_ssdd.yaml',
                cache=False,
                imgsz=640,
                epochs=150,
                batch=16,
                close_mosaic=10,
                workers=0,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
    