import class_Fbank as fb, class_members as cm
import numpy as np

################################################# 

class Org(cm.Members):
    
    def __init__(self, name):
        cm.Members.__init__(self,"Org", name)
        self.req_threshold = 100
        self.def_req_amt = 500
        self.disp_inc = (np.random.wald(2.82, 3)) * 1000
        self.reqtkns = 0    #binary switch - requesting when function of tokens_net, disp_inc, etc. is satisfied
        self.fbank_tkns_rec = 0
        self.fbank_dol_rec = 0        
        if (self.tokens_held < self.req_threshold):
            self.req_tkns(self.def_req_amt)
        self.update_accounting()
    
    def req_tkns(self, tokens): #request more tokens from fbank
        self.reqtkns = 1
        fb.rec_req(tokens,self)
        #print self.name + " is requesting a donation"
                 
    def rec_tkns(self, tokens): #receive tokens from fbank
        self.tokens_don_in += tokens
        self.reqtkns = 0
        self.fbank_tkns_rec += tokens
        self.update_accounting()
        print self.name + " received donation of " + str(tokens) + " tokens"

    def pay_tkns(self, tokens):  #pay tokens for work
        self.tokens_sold += tokens   
        self.update_accounting(tokens)