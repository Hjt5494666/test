from ultralytics import YOLO

if __name__=='__main__':
    model = YOLO("yolo11.yaml")
    model.load('yolo11x.pt')
    model.train(
        data='/data2/hejt/yolov11/ultralytics-main/ultralytics/cfg/datasets/classes.yaml',
        imgsz=640,
        epochs=1,
        batch=16,
        close_mosaic=0,
        workers=4,
        project='runs/train',
        name='exp'
    )