from cis301.phonebill.phonebill_dumper import PhoneBillDumper
import pickle

class TextDumper(PhoneBillDumper):
    pass

PhoneBillDumper = {1:"6",2:"2",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(PhoneBillDumper, pickle_out)
pickle_out.close()


PhoneCallDumper = {1:"7",2:"8",3:"f"}

pickle_out = open("dict.pickle","wb")
pickle.dump(PhoneCallDumper, pickle_out)
pickle_out.close()
