try:
  from bs4 import BeautifulSoup
  import requests
  import re
except:
  import os
  os.system("pip3 install bs4")

  raise SystemExit("\n\n Installed prerequisites, restart app again\n\n")

class LoveCalculator:

  URL = "https://www.lovecalculator.com/love.php?name1=__SIMP1__&name2=__SIMP2__"
  
  def __init__(self, Simp1, Simp2):
    self.Simp1 = Simp1
    self.Simp2 = Simp2

  def GetLoveCalculation(self) -> tuple:
    WebContent = requests.get(LoveCalculator.URL.replace("__SIMP1__", str(self.Simp1.encode("UTF-8"))).replace("__SIMP2__", str(self.Simp2.encode("UTF-8")))).content

    Soup = BeautifulSoup(WebContent, "html.parser")
    
    Percent = Soup.find(class_="result__score").text.strip()

    Lecture = Soup.find(class_="result-text").text.replace("\n", "").replace("b'", "'")

    Lecture = " ".join(Lecture.split())
    
    return (Percent, Lecture)

if __name__ == "__main__":
  print(LoveCalculator("%20", ".                        ").GetLoveCalculation())
