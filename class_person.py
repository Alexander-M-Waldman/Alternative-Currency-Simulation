import class_Fbank as fb, class_members as cm, class_org as co, parameters as param
import numpy as np
import gc, random

class Person(cm.Members):
    _instances = set()
    
    def __init__(self, name):
         cm.Members.__init__(self,"Pers", name)
         self.disp_inc = param.disp_inc
         self.rand_work = param.rand_work
         self.rand_buy_tks = param.rand_buy_tks
         self.rand_sell_tks = param.rand_sell_tks
         #self.get_tokens()
        
    def get_tokens(self):
         if (self.disp_inc < 1000 and self.rand_work > .5):		#later break this out with other decision parameters i.e. awareness
             self.num_tks_exch = int(max(10,np.random.normal(800,400)))
             orgid = self.find_work(self.num_tks_exch)
             if orgid:
                 self.work_tokens(self.num_tks_exch, orgid)
             
         if (self.disp_inc > 100 and self.disp_inc < 1000 and self.rand_buy_tks > .5):		#later break this out with other decision parameters i.e. awareness
             self.num_tks_exch = int(max(10,np.random.normal(30,20)))
             self.buy_tokens(self.num_tks_exch)
             
         if (self.disp_inc > 1000 and self.disp_inc < 10000 and self.rand_buy_tks > .5):		#later break this out with other decision parameters i.e. awareness
             self.num_tks_exch = int(max(10,np.random.normal(350,200)))
             self.buy_tokens(self.num_tks_exch)
             
         if (self.disp_inc > 10000 and self.rand_buy_tks > .6):		#later break this out with other decision parameters i.e. awareness
             self.num_tks_exch = int(max(10,np.random.normal(450,200)))
             self.buy_tokens(self.num_tks_exch)
       

    def buy_tokens(self, numtoks):
        fb.sell_tokens(numtoks, self)
        self.dollars_out = (numtoks * param.token_val)
        self.update_accounting()
        

    def find_work(self,numtoks):
        tks = int(numtoks)
        active_orgs = []
        for obj in gc.get_objects():
            if isinstance(obj, co.Org):
                obj.update_accounting()
                if obj.tokens_held > tks:                
                    active_orgs.append(obj)
                else:
                    #print obj.name
                    obj.req_tkns(tks)
        if active_orgs:
            return random.choice(active_orgs)
        else: 
            pass
            #print "out of cash"
        
         
    def work_tokens(self, numtoks, org):
        self.tokens_worked += numtoks
        org.tokens_sold += numtoks
        self.update_accounting()      
        #print ("Person " + self.name + " has $" + str(self.disp_inc) + " and is working for " + org.name + " for " + str(tks) + " tokens")

    
    def get_dollars(self):  # members (people) get dollars by selling tokens
        if (self.tokens_held > 0 and np.random.normal(0,1) > param.token_selling_threshold):      # adjust to make more realistic
            self.update_accounting()
            self.sell_tokens(min(self.tokens_held, max(0,int(self.tokens_held * np.random.normal(0,1)))))
            
    def sell_tokens(self, numtoks):
        #print (self.name,"selling") 
        self.tokens_sold += numtoks
        self.dollars_in += (numtoks * param.tok_exh_val)
        fb.buy_tokens(numtoks)
        self.update_accounting()
