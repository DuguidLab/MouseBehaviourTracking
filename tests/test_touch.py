import unittest
from kivy.tests.common import GraphicUnitTest, UnitTestTouch


class GraphicsTestCase(GraphicUnitTest):

    def test_render(self):
    from kivy.uix.button import Button

    button = Button()
    self.render(button)

    # get your Window instance safely
    from kivy.base import EventLoop
    EventLoop.ensure_window()
    window = EventLoop.window

    touch = UnitTestTouch(
        *[s / 2.0 for s in window.size]
    )

    button.bind(
        on_release=lambda instance: setattr(
            instance, 'test_released', True
        )
    )

    touch.touch_down()
    touch.touch_up()
    self.assertTrue(button.test_released)


class TouchTestCase(unittest.TestCase):

    def setUp(self):
        pass

if __name__ == '__main__':
unittest.main()
