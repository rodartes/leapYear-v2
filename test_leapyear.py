import leapyear

def test_leapYear():
  assert leapyear(400) == True

def test_notLeapYear():
  assert leapyear(100) == False