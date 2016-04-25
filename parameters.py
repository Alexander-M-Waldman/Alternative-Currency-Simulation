import numpy as np

#set parameters

#bank
starting_cash = 2000
frac_reserve = .7
don_generosity = .1
tok_exh_val = .9
token_val = 1		#dollars:tokens exchange value

#people
numpers = 200   #number of people to start with
list_of_persnames = range(1,numpers)
token_selling_threshold = 0.7
disp_inc = int((np.random.wald(2.82, 3) - 1) * 1000)   #stochasitcally assign disposable income         
rand_work = np.random.normal(0,1)     #
rand_buy_tks = np.random.normal(0,1)
rand_sell_tks = np.random.normal(0,1)

#orgs
list_of_orgnames = ["o1", "o2", "o3", "o4", "o5", "o6"]

#businesses
list_of_business_names = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8"]

