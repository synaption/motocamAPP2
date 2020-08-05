# Sample Python application demonstrating the working of AnchorLayout in Kivy

 

# Module imports

from kivy.app import App

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.video import Video
 
from kivy.graphics import Color, Rectangle

import paho.mqtt.publish as publish


# A Kivy app demonstrating the working of anchor layout

class AnchorLayoutDemo(App):
        
    def build(self):
        # Anchor Layout1
        anchorLayout1       = AnchorLayout(anchor_x='left', anchor_y='bottom')
        button1             = Button(text='test', size_hint = (0.3, 0.3))
        def callback(instance):
            print('The button <%s> is being pressed' % instance.text)
            publish.single("test", hostname="192.168.1.11")
        button1.bind(on_press=callback)
        anchorLayout1.add_widget(button1)

        # Anchor Layout2
        anchorLayout2    = AnchorLayout()
        anchorLayout2.anchor_x = 'right'
        anchorLayout2.anchor_y = 'top'
       
        # Add the anchor layouts to a box layout    
        vid = Video(source="http://192.168.1.11:8081/", play=True)
        anchorLayout2.add_widget(vid)       

        # Create a box layout
        boxLayout = BoxLayout()

        # Add both the anchor layouts to the box layout
        boxLayout.add_widget(anchorLayout1)
        boxLayout.add_widget(anchorLayout2)
 
        # Return the boxlayout widget
        return boxLayout



    

 

# Run the Kivy app
if __name__ == '__main__':
    AnchorLayoutDemo().run()
    
    
    
    
    
    
    
    
