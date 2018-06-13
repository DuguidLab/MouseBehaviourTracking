"""
App entry point
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle, Point, GraphicException
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.animation import Animation
from kivy import metrics
from plyer import vibrator
import pickle
import time



class NoddyWidget(Widget):
    """Main App widget"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Get window size in pixels
        self.size = Window.size
        root = self
        self.dragcoords = []
    
    def on_touch_down(self, touch):
        sound = SoundLoader.load('../res/sound.wav')  # Add sound file to repo
        print(touch)
        for child in self.children[:]:
            print(child)
            if child.collide_point(*touch.pos):
                print("HIT")
                child.animate(child)
            else:
                print("MISS")

        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            Rectangle(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            if sound:
                try:
                    sound.play()
                except FileNotFoundError:
                    print('Sound file not located.')
            try:
                vibrator.vibrate(1)
            except NotImplementedError:
                print('Vibration not supported on this platform')

    def on_touch_move(self, touch):
        if touch.is_touch:
            try:
                self.dragcoords.append(touch.pos)
            except Exception:
                print("Could not find position!")

    def on_touch_up(self, touch):
        print("Paw released!")
        print(self.dragcoords)
        with open(('{}.pkl').format(str(time.time())), 'wb') as f:
            pickle.dump(self.dragcoords, f)
        self.dragcoords.clear()


class Target(Widget):
    """Target bar for behaviour"""
    def __init__(self, **kwargs):
        super(Target, self).__init__(**kwargs)
        self.size = (30, Window.height)
        self.pos = (Window.width / 2, 0)
        self.update_canvas()
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)

    def animate(self, instance):
        animation = Animation(pos=(0, 0), t='linear')
        animation.start(instance)

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color(1, 1, 1)
            Rectangle(pos=self.pos, size=self.size)


class MouseBehaviourTrackingApp(App):
    """App entry point"""
    def build(self):
        parent = NoddyWidget()
        target = Target()
        parent.add_widget(target)
        return parent
        
if __name__ == '__main__':
    MouseBehaviourTrackingApp().run()
