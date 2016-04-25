import parameters as param
import gc
import class_business as cb, class_org as co, class_person as cp
import numpy as np
#from scipy import stats
#from itertools import count


#tok_gen_amt = 0.1   #fraction of tkns gen per tkns purchased
token_val = 1		#dollars:tokens exchange value
tokens_gen = 0      #from tok_gen_amt during bank transactions
tokens_bought = 0       #tokens taken in from buying back
tokens_sold = 0
tokens_circ = 0
tokens_don_in = 0
tokens_don_out = 0
tokens_held = 0 #tokens_held = (tokens_bought + tokens_gen - tokens_don - toksconv2dols)
tokens_net = 0  #tokens_net = (tokens_bought + tokens_gen + (dollars_conv * tok_exh_val) - tokens_sold - tokens_don)
#to
dollars_sold = 0
dollars_bought = param.starting_cash
dollars_don_in = param.starting_cash # [num_donations, total amount]
dollars_don_out = 0 # [num_donations, total amount]
dollars_held = param.starting_cash
tok_exh_val = .9
frac_reserve = param.frac_reserve   #minimum amount of net dollars + tokens kept by bank (as ratio to tokens in circulation)
active_members = 0
members_joined = 0
members_left = 0
members_ids = []
req_don = 0
don_generosity = param.don_generosity

##############################################################################################

def gen_toks(numtoks):   #generate some number of new tokens
    global tokens_gen
    tokens_gen += numtoks
    #print "Fbank generated " + str(numtoks) + " tokens"

def sell_tokens(numtoks, member):
    eval_freserve()
    update_accounting()  
    global dollars_bought
    global tokens_sold
    global tokens_gen  
    if (tokens_held > numtoks):
        member.tokens_bought += int(numtoks)
        dollars_bought += (numtoks * token_val)
        tokens_sold += numtoks  
    else:        
        tokens_gen += numtoks
        tokens_sold += numtoks
        dollars_bought += (numtoks * token_val)
        member.tokens_bought += int(numtoks)
    update_accounting()  
    #tokens_gen += float(numtoks)* tok_gen_amt

def buy_tokens(tokens):
    global tokens_bought
    global dollars_sold    
    tokens_bought += tokens
    dollars_sold += int(tok_exh_val * tokens)
    update_accounting()
 
def donate_tokens(tokens,member):   
    global tokens_don_out    
    tokens_don_out += tokens
    member.rec_tkns(tokens)
    update_accounting()
    print "Fbank donated " + str(tokens) + " to " + member.name
    
def donate_dollars(dollars,member):
    pass

###############################################################################
#
# Handle Fbank donation requests and donations 
#
##################################################################################

def req_donation(dollars):  #FBank requests donations (expand this, i.e. initalize fundraiser...)
    global req_don
    req_don = 1
    try_donation(dollars)

def rec_donation(dollars):    #Fbank receives donations (in dollars)
    global dollars_don_in  
    global req_don    
    dollars_don_in += dollars
    req_don = 0
    print "Fbank recieved $" + str(dollars) + " in donations"
    update_accounting()

def try_donation(dollars):
    if (req_don == 1):
        if (np.random.normal(0,1) > (1 - don_generosity)):
            rec_donation(dollars)
            
###############################################################################
#
# Request Handling
#
###############################################################################
            
def rec_req(tokens, member):    #receive request from org for donations (in tokens)
    pot_don = eval_req(tokens)
    if (pot_don > 0):
        donate_tokens(tokens, member)
    else:
        req_donation(tokens * tok_exh_val)
    
def eval_req(tokens):       # fix so donations are split among requesters for each time step(i.e. year), or incorporate a selection method   
    global req_don    
    update_accounting()
    if tokens_held > tokens:
        req_don = 0 #not requesting donations        
        return tokens
    else:
        req_don = 1
        return 0

################################################################################
# 
# Accounting
#       
###############################################

def eval_freserve():
    update_accounting()
    pot_toks_gen = (dollars_held / frac_reserve) - tokens_held - tokens_circ
    #print "pot_toks_gen = " + str(pot_toks_gen)
    if (pot_toks_gen < 0):
        req_donation(abs(pot_toks_gen))
    elif (pot_toks_gen == 0):
        pass
    else:
        gen_toks(pot_toks_gen)
        

def get_net_tokens():
    global tokens_held 
    tokens_held = (tokens_bought + tokens_gen + tokens_don_in - tokens_don_out - tokens_sold)
    
def get_net_dollars():
    global dollars_held    
    dollars_held = (dollars_bought + dollars_don_in - dollars_sold - dollars_don_out)
    return dollars_held
    

def count_toks_circulating():   #perhaps modify to take memeber types to consider
    global tokens_circ
    tokens_circ = 0    
    for obj in gc.get_objects():
        if isinstance(obj, cp.Person) or isinstance(obj, co.Org) or isinstance(obj, cb.Business):
            tokens_circ += obj.tokens_held
    return tokens_circ
    
def update_accounting():  
    get_net_tokens()   
    get_net_dollars()
    count_toks_circulating() 