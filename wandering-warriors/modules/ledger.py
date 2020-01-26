from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from kivy.uix.label import Label


class Ledger(BoxLayout):
    """
    Ledger data structure:
    x: first number in equation (float)
    y: second number in equation (float)
    op: operator ['+', "-", '*', '/'] (str)
    z: result (float)
    """

    def __init__(self, **kwargs):
        super(Ledger, self).__init__(**kwargs)
        self.col = 'x'
        self.row = 1
        self.df = pd.DataFrame(columns=['x', 'y', 'op', 'z'])
        self.df.loc[1] = {'x': 0, 'y': 0, 'op': '', 'z': 0}
        self.clear_button_src = 'assets/graphics/clear.png'

    def select(self, col: str):
        """select active column"""
        if col not in ['x', 'y', 'op', 'z']:
            print(f"[ WARNING ] Invalid column: {col}")
            pass
        else:
            self.col = col

    def update(self, n: int, op: str = '='):
        base_sixty_digits = self.num_to_cuneiform(n)

        """update active cell"""
        if op == '+':
            self.df.at[self.row, self.col] += n
        if op == '-':
            self.df.at[self.row, self.col] -= n
        if op == '*':
            self.df.at[self.row, self.col] *= n
        if op == '/':
            self.df.at[self.row, self.col] /= n
        if op == '=':
            self.df.at[self.row, self.col] = n
        self.refresh_ledger()

    def operation(self, op: str):
        """update operator column of current row and advance selection"""
        if op not in ['+', '-', '*', '/']:
            print(f"[ WARNING ] Invalid operator: {op}")
        print(self.df.at[self.row, 'op'])
        self.df.at[self.row, 'op'] = op
        self.select('y')
        self.refresh_ledger()

    def get_row(self) -> dict:
        """return all values from active row"""
        return self.df.loc[self.row].to_dict()

    def submit_row(self):
        """add and select new row at bottom of ledger"""
        self.col = 'z'
        # TODO: execute equation if possible and store result z
        print(self.df.loc[self.row])
        self.new_row()

    def refresh_ledger(self):
        """refresh ledger view with current data"""
        # TODO: Reincorporate A5's cuneiform translator commented out below (untested)
        rows = self.df.values.astype('str')
        self.rv.data = [
            {'value': row} for row in rows
        ]

    def new_row(self):
        """add and select new row at bottom of ledger"""
        index = len(self.df.index) + 1
        self.df.loc[index] = {'x': 0, 'y': 0, 'op': '', 'z': 0}
        self.row = index
        self.col = 'x'
        self.refresh_ledger()
        self.get_row()

    def clear(self):
        """clear ledger and backing dataframe"""
        self.df = pd.DataFrame(columns=['x', 'y', 'op', 'z'])
        self.new_row()

    def num_to_cuneiform(self, x):
        base_sixty_digits = []
        while x > 0:
            n = x % 60
            base_sixty_digits.insert(0, n % 60)
            x //= 60
        imgs = []
        for n in base_sixty_digits:
            img = Image(source = f'assets/graphics/{n}.svg')
            imgs.append(img)
        return imgs

    def close_help(self):
        self.remove_widget(self.help_label)

    def open_help(self):
        self.help_label = FloatLayout()
        label = Label(
            text='Make tally marks on the sand to record a number.',
            pos=(20, 20),
            size=(180, 100),
            size_hint=(None, None))
        with label.canvas:
            Color(0, 1, 0, 0.25)

        self.help_label.add_widget(label)

        self.add_widget(self.help_label)