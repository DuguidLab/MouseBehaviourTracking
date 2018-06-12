from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy import metrics
from plyer import vibrator

class NoddyWidget(Widget):
    def __init__(self, **kwargs):
        super(NoddyWidget, self).__init__(**kwargs)
        # Get window size in pixels
        self.size = Window.size
        root = self

    
    def on_touch_down(self, touch):
        sound = SoundLoader.load('../res/sound.wav')  # Add sound file to repo
        print(touch)
        for child in self.children[:]:
            print(child)
            print(child.collide_point(*touch.pos))
            print(self.collide_widget(child))

        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Rectangle(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            if sound:
                sound.play()
            try:
                vibrator.vibrate(1)
            except NotImplementedError:
                print('Vibration not supported on this platform')

class Target(Widget):
    def __init__(self, **kwargs):
        super(Target, self).__init__(**kwargs)
        self.size = (30, Window.height)
        self.pos = (Window.width / 2 , 0)
        with self.canvas:
            Color(1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)

class MouseBehaviourTrackingApp(App):
    def build(self):
        parent = NoddyWidget()
        parent.add_widget(Target())
        return parent


if __name__ == '__main__':
    MouseBehaviourTrackingApp().run()
