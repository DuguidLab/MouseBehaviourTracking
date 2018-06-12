from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

class NoddyWidget(Widget):
    def __init__(self, **kwargs):
        super(NoddyWidget, self).__init__(**kwargs)

        # Get window size in pixels
        self.size = Window.size
        root = self

        # Draw rectangle at center of screen
        with self.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(pos=(self.center_x, 0), size=(30, self.height))

    def on_touch_down(self, touch):
        sound = SoundLoader.load('')  # Add sound file to repo
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
