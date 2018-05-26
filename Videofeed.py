import argparse, imutils, time, cv2, sys, numpy, io 
from imutils.video import VideoStream
from PIL import Image

class Videofeed:
    
    def __init__(self, name = "test", index = 0):
        self.index = index
        self.name = name

    def start(self):
        self.vs = VideoStream(self.index).start()
        time.sleep(1.0)
       
    def check_camera_index(self):
        key = cv2.waitKey(1)
        if (key == "n"): 
            self.index += 1 
            self.vs = VideoStream(self.index).start()
            if not self.vs: 
                self.index = 0
                self.vs = VideoStream(self.index).start()
    
    def get_frame(self):
        frame = self.vs.read()
        self.check_camera_index()
        b = io.BytesIO()        
        frame = imutils.resize(frame, width=450)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stream = Image.fromarray(frame)
        stream.save(b, 'jpeg')
        time.sleep(1)
        return b.getvalue()

    def set_frame(self, stream):
        frame = io.BytesIO(stream)
        frame = Image.open(frame)
        frame = cv2.cvtColor(numpy.array(frame), cv2.COLOR_RGB2BGR)
        cv2.imshow(self.name, frame)

if __name__ == "__main__" :
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", "--name", type=str, default="test", help="name of camera")
    ap.add_argument("-w", "--webcam", type=int, default=0, help="index of webcam on system")
    args = vars(ap.parse_args())
    
    client = Videofeed("client", 0)
    server = Videofeed("server", 0)
    client.start()
    while True:
        stream = client.get_frame()
        server.set_frame(stream)

