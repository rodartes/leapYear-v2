import leap
import pytest

def test_leapYear():
  assert leap.leapyear(400) == True

def test_notLeapYear():
  assert leap.leapyear(100) == False