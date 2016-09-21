# Tea types for Tea timer app
# Jonathan Clede 2016
# Designed for Python 3

class Tea(object):
    """Class for specific types of tea."""
    
    def __init__(self, name, brew_dur, temp=None, qty=None ):
        self.name = name
        self.brew_dur = brew_dur
        self.temp = temp
        self.qty = qty

# A set of basic teas to get started.
base_teatimes = [('White', 2),  ('Green', 3),  ('Black', 4), ('Darjeeling', 3),
                 ('Oolong', 4), ('Herbal', 6), ('Pu-Erh', 4) ]

tea_list = [Tea(name, dur) for name, dur in base_teatimes]
