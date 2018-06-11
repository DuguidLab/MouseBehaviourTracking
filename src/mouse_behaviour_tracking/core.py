from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class NoddyWidget(Widget):
    def __init__(self, *args, **kwargs):
        super(NoddyWidget, self).__init__()
        with self.canvas:
            Color(1, 1, 0)
            d = 30.
            spos = (self.center_x, self.center_y)
            self.rect = Rectangle(pos=self.center, size=(d, d))

        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos

    def on_touch_down(self, touch):
        print(touch)


class MouseBehaviourTrackingApp(App):
    def build(self):
        return NoddyWidget()


if __name__ == '__main__':
    MouseBehaviourTrackingApp().run()