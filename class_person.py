import class_Fbank as fb, class_members as cm, class_org as co
import numpy as np
import gc, random

class Person(cm.Members):
    _instances = set()
    
    def __init__(self, name):
         cm.Members.__init__(self,"Pers", name)
         self.disp_inc = int((np.random.wald(2.82, 3) - 1) * 1000)   #stochasitcally assign disposable income         
         self.rand_work = np.random.normal(0,1)     #
         self.rand_buy_tks = np.random.normal(0,1)
         self.rand_sell_tks = np.random.normal(0,1)  
         self.get_tokens()
        
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

     
    def sell_tokens(self, numtoks):
        print (self.name,"selling") 
        self.tokens_sold += numtoks
        self.update_accounting()
     
