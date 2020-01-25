from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

from modules import Abacus as AbacusBase
from modules import DrawPad, LedgerLayout

# imports for demo
from kivy.core.window import Window
from random import randint


class Calculator(Screen):
    pass


class Settings(Screen):
    pass


class TopMenu(Widget):
    pass


class Abacus(AbacusBase):
    pass


class Ledger(LedgerLayout):
    # https://stackoverflow.com/a/17296090
    def __init__(self, **kwargs):
        super(Ledger, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, _keyboard, keycode, _text, _modifiers):
        if keycode[1] == 'down':
            self.add_cuneiform_from_b10(randint(0, 10**6))

        return True


class OperationsBar(Widget):
    pass


class CuneiformDrawingInput(DrawPad):
    pass


class TopRightButton(Widget):
    pass


class Screen:
    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Calculator(name='calculator'))

    def get_manager(self):
        return self.sm


class CalculatorApp(App):
    def build(self):
        return Screen().get_manager()


if __name__ == "__main__":
    CalculatorApp().run()
