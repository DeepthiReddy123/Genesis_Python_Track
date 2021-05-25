import pytest
import sys
import warnings
import main
from main import Sum ,main ,Admin ,user ,bookingdetails ,record , status ,adminroom,roomtypefunction ,acavailability , nonacavailability , splacavailability

def test_no1():
    a=4
    b=5
    assert Sum(a,b)==9

def test_no10():
    password="Admin123"
    passwd=password
    assert Admin()==status()

def test_main():
    b=1
    assert main()==Admin()

def test_main2():
    b=2
    assert main()==user()  

def test_main3():
    b=3
    assert None == bookingdetails()

def test_main4():
    b=4  
    assert main()==record()       

def test_add():
   a=2
   b=9
   assert Sum(a,b) == 11

def test_no5():
    romty=1
    assert roomtypefunction()==nonacavailability()

def test_no6():
    romty=2
    assert roomtypefunction()==acavailability()

def test_no7():
    romty=3
    assert roomtypefunction()==nonacavailability()

def test_no8():
    romty=0
    assert roomtypefunction()==main()

def test_no9():
    z=1
    assert status()==adminroom()        

