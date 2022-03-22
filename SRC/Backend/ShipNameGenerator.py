from Backend.IsAWord import IsAWord

class ShipNameGenerator:
  def __init__(self, Simp1, Simp2):
    self.Simp1 = Simp1
    self.Simp2 = Simp2

  def SplitName(self, Name):
    Vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    FrontNames = []
    BackNames = []
    for i in range(1, len(Name)):
      if Name[i] in Vowels:
        FrontNames.append(Name[:i + 1])
    for i in range(2, len(Name)):
      i = -i
      if Name[i] not in Vowels or Name[i] == 'y':
        BackNames.append(Name[i:])
    return (FrontNames, BackNames)

  def CombNames(self, Front, Back):
    Front = Front[0]
    Back = Back[1]
    GoodNames = []
    for f in Front:
      for b in Back:
        GoodNames.append(f + b)
    
    return GoodNames
  
  def GetShipNames(self):
    self.Simp1 = self.SplitName(self.Simp1)
    self.Simp2 = self.SplitName(self.Simp2)
    self.ShipNames = self.CombNames(self.Simp1, self.Simp2) + self.CombNames(self.Simp2, self.Simp1)
    self.WordShipNames = [x for x in self.ShipNames if IsAWord(x)]
    

if __name__ == '__main__':
  Simp1 = input('Simp1: ').lower()
  Simp2 = input('Simp2: ').lower()
  s = ShipNameGenerator(Simp1, Simp2)
  s.GetShipNames()
  print(s.ShipNames)
  print(s.WordShipNames)