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
list_of_orgnames = ["Bymyside", "NKFC", "circle_thrift", "NKCDC", "Adaire", "Hackett"]

#businesses
list_of_business_names = ["Mycopolitan", "Soup Kitchen", "Philly Bagel", "Rocket Cat", "PBC", "Rowhouse Spirits", "Heffe", "Record Exchange"]

