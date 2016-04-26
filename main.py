import parameters as param, class_Fbank as fb, class_person as cp, class_org as co, class_business as cb
import gc
import numpy as np
import matplotlib.pyplot as plt
##################################################

#create Orgs/nfp

memtype = "Org"
for name in param.list_of_orgnames:
    globals()[str(name)] = co.Org(str(name))
    
#create Businesses

memtype = "Bus"
for name in param.list_of_business_names:
    globals()[str(name)] = cb.Business(str(name))
    
#create People

memtype = "Pers"
for name in param.list_of_persnames:
    globals()[str(name)] = cp.Person(str(name))
    
##################################################
        
def update_fbank():
    fb.eval_freserve()
    fb.update_accounting()
    print "dollars held = " + str(fb.dollars_held)
    print "tokens held = " + str(fb.tokens_held)
    print "tkns in circulation = " + str(fb.tokens_circ) 
    print "tkns sold = " + str(fb.tokens_sold)
    print "generated tokens = " + str(fb.tokens_gen)  
    print "tokens donated out = " + str(fb.tokens_don_out)
    print "tokens bought (dollars sold) by bank = " + str(fb.dollars_sold)
    print "dollars donated in = " + str(fb.dollars_don_in)

#########################################################
    
#simulation

##########################################################

year = 0
sim_years = 20

while (year < sim_years):
    year += 1
    update_fbank()

    print "           It is now year " + str(year) + "."
    
    for obj in gc.get_objects():
        if isinstance(obj, cp.Person):
            obj.rand_work = np.random.normal(0,1)     #
            obj.rand_buy_tks = np.random.normal(0,1)
            obj.rand_sell_tks = np.random.normal(0,1)  
            obj.get_tokens()
            obj.get_dollars()
#           print obj.name + " has " + str(obj.tokens_held) + " tokens"
            
    for obj in gc.get_objects():
        if isinstance(obj, co.Org):
            obj.update_accounting()
            print obj.name + " has " + str(obj.tokens_held) + " tokens"
            print obj.name + " has received " + str(obj.tokens_don_in) + " tokens"
            
###########################################################################
    
# data analysis

###########################################################################

    people_held_toks = []
    people_wrkd_toks = []
    people_bought_toks = []    

    for obj in gc.get_objects():

        if isinstance(obj, cp.Person):
            people_held_toks.append(obj.tokens_held)
            people_wrkd_toks.append(obj.tokens_worked)
            people_bought_toks.append(obj.tokens_bought)

    plt.figure(1)
    
    plt.subplot(221)
    plt.hist(people_held_toks)
    plt.title("Tokens Held")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    #plt.show()
            
    plt.subplot(222)
    plt.hist(people_wrkd_toks, color='r')
    plt.title("Tokens Worked")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    #plt.show()
    
    plt.subplot(223)
    plt.hist(people_bought_toks, color='g')
    plt.title("Tokens Bought")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    
    #plt.show()
    plt.tight_layout()
    plt.show()
    
update_fbank()

