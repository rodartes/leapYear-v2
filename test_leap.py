import leap

def test_leapYear():
  assert leap.leapyear(400) == True
  assert leap.leapyear(4) == True
  assert leap.leapyear(2000) == True
  assert leap.leapyear(2020) == True

def test_notLeapYear():
  assert leap.leapyear(100) == False
  assert leap.leapyear(2019) == False
  assert leap.leapyear(2018) == False
  assert leap.leapyear(2017) == False