from pip import main

from cis301.project3.phonebill import PhoneBill
from cis301.project3.phonecall import PhoneCall

def test_project3():
     phonebill = PhoneBill("Trey")
     assert phonebill.get_customer() is "Trey"
     phonecall = PhoneCall

def test_project3():
    phonecall = PhoneCall("Sam")
    assert phonecall.get_caller() is "Sam"

def test_main():
    eval (main())

