import os

PreloadedWords = []

with open(os.path.dirname(os.path.realpath(__file__)) + "/Words.txt", "r") as f:
  PreloadedWords = [x.replace("\n", "") for x in f.readlines()[:10000]]

def IsAWord(Word):
  return Word in PreloadedWords

if __name__ == "__main__":
  print(IsAWord("porn"))