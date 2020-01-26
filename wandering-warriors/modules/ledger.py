from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import pandas as pd


class Ledger(BoxLayout):
    def __init__(self, **kwargs):
        super(Ledger, self).__init__(**kwargs)
        print('[ INIT LEDGER ]')
        self.df = pd.DataFrame(columns=['x', 'y', 'op', 'z'])
        self.col = 'x'
        self.row = 1
        self.new_row()
        self.num_to_cuneiform(59)
        self.clear_button_src = 'assets/graphics/clear.png'

    def select(self, col: str):
        """select column: ['x', 'y', 'z']"""
        if col not in ['x', 'y', 'z']:
            print(f"WARNING: Invalid column: {col}")
            pass
        else:
            self.col = col

    def update(self, n: int, op: str = '='):
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
        print(self.df)
        self.update_ledger()

    def new_row(self):
        """add and select new row at bottom of ledger"""
        index = len(self.df.index) + 1
        self.df.loc[index] = {'x': 0, 'y': 0, 'op': None, 'z': 0}
        self.row = index
        self.col = 'x'
        print(self.df)

    def update_ledger(self):
        """update ledger view with current data"""
        rows = self.df.values.astype('str')
        print(f"ROWS: {rows}")
        print(f"ids: {self.ids}")
        self.rv.data = [
            {'value': row} for row in rows
        ]

    def clear(self):
        self.rv.data = []

    def num_to_cuneiform(self, x):
        x = 74
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