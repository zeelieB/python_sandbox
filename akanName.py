import datetime
import sys
import re


birthNames = [ ['Kwasí','Akosua'], ['Kwadwó','Adwoa'], ['Kwabená','Abenaa'], ['Kwakú','Akúá'], ['Yaw','Yaa'], ['Kofí','Afua'], ['Kwámè','Ama'] ]

twinBirthNames = [["Atá Pánin", "Ataá Pánin"], ["Atá Kúmaa","Ataá Kúmaa"]]

inDate = input("Please enter a date (eg. DD/MM/YYYY): ")
inGen = input("Please enter a gender binary (M/F): ")

inGenNum = 0
if inGen == 'F':
  inGenNum = 1

inTwin = input("Were you a twin? (Y/N) ")
if inTwin == 'Y':
  twinOrder = int(input("Were you first or second? (1/2) "))
  print("Your Akan name would be: " + twinBirthNames[twinOrder-1][inGenNum])
else:
  workDate = datetime.datetime.strptime(inDate, "%d/%m/%Y").weekday()

  print("You entered " + inDate)
  print("Your Akan name would be: " + birthNames[workDate][inGenNum])
