from step import Step

class Piece():
    def __init__(self, name):
        self.name = name
        self.step = self.configure_step()

    def configure_step(self):
        if self.name.lower() == 'knight':
            s = Step().set('knight')
            return s.get()