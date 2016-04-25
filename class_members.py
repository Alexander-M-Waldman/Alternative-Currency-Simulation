
class Members(object):

    def __init__(self, memtype, name):
    
        self.Title = memtype
        self.name =  name
        self.tokens_bought = 0
        self.tokens_sold = 0
        self.tokens_worked = 0
        self.tokens_don_in = 0
        self.tokens_don_out = 0
        self.tokens_held = 0
        self.dollars_in = 0
        self.dollars_out = 0
        self.start_date = 0
        self.disp_inc = 0
        
    def update_accounting(self):
        self.tokens_held = self.tokens_bought + self.tokens_worked + self.tokens_don_in - self.tokens_sold - self.tokens_don_out
        self.disp_inc += (self.dollars_in - self.dollars_out)
