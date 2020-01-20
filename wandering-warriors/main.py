from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget


class Calculator(Screen):
    pass


class Settings(Screen):
    pass


class TopMenu(Widget):
    pass


class Abacus(Widget):
    MAX_BAR_W = 10
    BORDER_W = 16
    DIVIDER_OFFSET = 0.6
    BEAD_SPACING = 8

    def __init__(self, **kwargs):
        super(Abacus, self).__init__(**kwargs)

        self.n_bars = 8
        self.n_top_beads = 2
        self.n_bottom_beads = 5
        self.bar_w = self.MAX_BAR_W

        with self.canvas:
            Color(1, 1, 1, 1)

            self.border = []

            for i in range(4):
                self.border.append(Rectangle(source='assets/graphics/wood.png'))

            Color(1, 1, 1, 0.2)

            self.border_highlight = [Rectangle(), Rectangle()]

            Color(1, 1, 1, 1)

            self.divider = Rectangle(source='assets/graphics/wood.png')

            Color(1, 1, 1, 0.2)

            self.border_highlight.append(Rectangle())

            self.bar_rects = []
            self.top_beads = []
            self.bottom_beads = []

            Color(0.8, 0.8, 0.8, 1)

            for i in range(self.n_bars):
                self.bar_rects.append([Rectangle(), Rectangle()])

                top_beads = []

                for j in range(self.n_top_beads):
                    top_beads.append(Rectangle(source='assets/graphics/bead.png'))

                self.top_beads.append(top_beads)

                bottom_beads = []

                for j in range(self.n_bottom_beads):
                    bottom_beads.append(Rectangle(source='assets/graphics/bead.png'))

                self.bottom_beads.append(bottom_beads)

        self.bind(pos=self.update, size=self.update)
        self.update()

    def update(self, *args):
        w = max(self.height / 20, self.BORDER_W)

        self.bar_w = self.MAX_BAR_W - (0 if self.width > 800 else (800 - self.width) / 800 * 10)

        print(self.width, (800 - self.width) / 800)

        self.border[0].pos = (self.x, self.y + self.height - w)
        self.border[0].size = (self.width, w)

        self.border[1].pos = self.pos
        self.border[1].size = (self.width, w)

        self.border[2].pos = self.pos
        self.border[2].size = (w, self.height)

        self.border[3].pos = (self.x + self.width - w, self.y)
        self.border[3].size = (w, self.height)

        inner_w = self.width - 2 * w

        self.border_highlight[0].pos = (self.x, self.y + self.height - w / 5)
        self.border_highlight[0].size = (self.width, w / 5)

        self.border_highlight[1].pos = (self.x + w, self.y + 4 * w / 5)
        self.border_highlight[1].size = (inner_w, w / 5)

        self.divider.pos = (self.x + w, self.y + self.height * self.DIVIDER_OFFSET)
        self.divider.size = (inner_w, w)

        self.border_highlight[2].pos = (self.x + w, self.y + 4 * w / 5 + self.height * self.DIVIDER_OFFSET)
        self.border_highlight[2].size = (inner_w, w / 5)

        for i in range(self.n_bars):
            bar = self.bar_rects[i]
            spacing = inner_w / self.n_bars

            x = self.x + w + spacing / 2 + spacing * i - self.bar_w / 2

            bar[0].pos = (x, self.y + w - w / 10)
            bar[0].size = (self.bar_w, self.height - w + w / 10 - self.height * (1 - self.DIVIDER_OFFSET))
            
            bar[1].pos = (x, self.y + self.height * self.DIVIDER_OFFSET + w - w / 10)
            bar[1].size = (self.bar_w, self.height * (1 - self.DIVIDER_OFFSET) - 2 * w + w / 10)

            bead_w = (self.height * self.DIVIDER_OFFSET - self.BORDER_W) / (self.n_bottom_beads + 1) * 2 #spacing - self.BEAD_SPACING
            bead_x = x + self.bar_w / 2 - bead_w / 2

            top_beads = self.top_beads[i]

            for j in range(self.n_top_beads):
                top_beads[j].pos = (bead_x, self.y + self.height - self.BORDER_W - bead_w / 2 - j * bead_w / 2)
                top_beads[j].size = (bead_w, bead_w / 2)

            bottom_beads = self.bottom_beads[i]

            for j in range(self.n_bottom_beads):
                bottom_beads[j].pos = (bead_x, self.y + self.BORDER_W + j * bead_w / 2)
                bottom_beads[j].size = (bead_w, bead_w / 2)


class Ledger(Widget):
    pass


class OperationsBar(Widget):
    pass


class CuneiformDrawingInput(Widget):
    pass


class Screen:
    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Calculator(name='calculator'))

    def get_manager(self):
        return self.sm


class CalculatorApp(App):
    def build(self):
        Builder.load_file("calculator.kv")
        return Screen().get_manager()


if __name__ == "__main__":
    CalculatorApp().run()
