from kivy.app import App
from kivy.uix.video import Video
#import ffmpeg


class SimpleApp(App):
    def build(self):
 
        #s = Video(source="vids/x.mp4", play=True)
        s = Video(source="rtsp://192.168.1.13:8554", play=True)
        #s = Video(source="http://192.168.1.11:8081", play=True)
        return s
 
 
if __name__ == "__main__":
    SimpleApp().run()
    


