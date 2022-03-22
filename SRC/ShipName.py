from Backend.LoveCalculator import LoveCalculator
from Backend.ShipNameGenerator import ShipNameGenerator

if __name__ == '__main__':
  Simp1 = input('Simp (who simps so hard): ').lower().strip()
  Simp2 = input('Crush (who will reject the simp): ').lower().strip()
  s = ShipNameGenerator(Simp1, Simp2)
  s.GetShipNames()
  if s.ShipNames == []:
    raise NameError('Input some real simps and I can give you some real ship names you idiot')
  print(s.ShipNames)
  print(s.WordShipNames)

  l = LoveCalculator(Simp1, Simp2)

  print(l.GetLoveCalculation())
  #Insert love calc here