import os
import sys

def main():

  args = sys.argv
  if os.path.exists(str(args[1])):
    PATH = str(args[1])
  else:
    return print("Wrong Path!!!")

  for root, dirs, files in os.walk(PATH, topdown=False):
    existFileCounter = 1
    for name in dirs:

      try:
        newFolderName = name[:-32]
        os.rename(os.path.join(root, name), os.path.join(root, newFolderName))
      except FileExistsError:
        newFolderName = name[:-32] + " (" + str(existFileCounter) + ")"
        existFileCounter += 1

  for root, dirs, files in os.walk(PATH, topdown=False):
    existFileCounter = 1
    for name in files:
      if name == os.path.basename(__file__): continue
      if ".png" in name: continue

      dotIndex = name.find(".", -5, -1)

      try:
        newFileName = name[:dotIndex][:-33] + name[dotIndex:]
        os.rename(os.path.join(root, name), os.path.join(root, newFileName))
      except FileExistsError:
        newFileName = name[:dotIndex][:-33] + " (" + str(existFileCounter)+ ")" + name[dotIndex:]
        os.rename(os.path.join(root, name), os.path.join(root, newFileName))
        existFileCounter += 1

if __name__ == "__main__":
  main()
