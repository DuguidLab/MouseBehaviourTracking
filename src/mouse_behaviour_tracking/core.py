from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader

class NoddyWidget(Widget):

sound = SoundLoader.load('')  # Add sound file to repo

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Rectangle(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            if sound:
                sound.play()



class MouseBehaviourTrackingApp(App):
    def build(self):
        return NoddyWidget()


if __name__ == '__main__':
    MouseBehaviourTrackingApp().run()
