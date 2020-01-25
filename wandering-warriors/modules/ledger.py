from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from typing import List
from pathlib import Path
import math
import functools

BLANK_ROW = functools.partial(Widget)
ROWS_IN_LEDGER = 10  # TODO: make this dependent on height
GENERATED_PATH = Path('.') / 'assets' / 'graphics' / 'generated'


class LedgerLayout(BoxLayout):
    child_widgets: list

    def __init__(self, **kwargs):
        super(LedgerLayout, self).__init__(
            orientation='vertical',
            **kwargs
        )

        self.child_widgets = []

        # initialize with blank rows
        for _ in range(ROWS_IN_LEDGER):
            self.add_widget(BLANK_ROW())

    def add_widget(self, widget, *args, **kwargs):
        if ROWS_IN_LEDGER == len(self.child_widgets):
            super(LedgerLayout, self).remove_widget(self.child_widgets[0])
            self.child_widgets = self.child_widgets[1:]

        super(LedgerLayout, self).add_widget(widget, *args, **kwargs)
        self.child_widgets.append(widget)

    def add_text(self, text: str) -> None:
        """Helper function to add text to the layout."""
        if not isinstance(text, str):
            text = str(text)

        self.add_widget(Label(text=text))

    def add_cuneiform_from_b10(self, b10_number: int) -> None:
        """Converts input then adds as unicode cuneiform."""
        # this function just converts to b60, another function displays
        if b10_number == 0:
            return self.add_cuneiform([])

        upper_limit = int(math.log(b10_number, 60)) + 1
        b60_number = []

        for i in range(upper_limit - 1, -1, -1):
            b60_number.append(b10_number // 60 ** i)
            b10_number %= 60 ** i

        return self.add_cuneiform(b60_number)

    def add_cuneiform(self, b60_number: List[int]) -> None:
        layout = BoxLayout()

        for b10_number in b60_number:
            tens = (b10_number // 10) * 10
            tens = 'blank' if not tens else tens
            ones = (b10_number % 10)
            ones = 'blank' if not ones else ones

            layout.add_widget(Image(
                source=str((GENERATED_PATH / f'{tens}.png').resolve())
            ))
            layout.add_widget(Image(
                source=str((GENERATED_PATH / f'{ones}.png').resolve())
            ))

        layout.padding = 0

        self.add_widget(layout)

    # def click(self):
    #     print('click')
    #
    # def buttonImage(self):
    #     return 'assets/graphics/clay.png'
