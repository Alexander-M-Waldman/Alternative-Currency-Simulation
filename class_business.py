import class_members as cm
#import class_Fbank as fb, class_person as cp, class_org as co

##############################


class Business(cm.Members):

 def __init__(self, name):
     cm.Members.__init__(self,"Bus", name)
     pass