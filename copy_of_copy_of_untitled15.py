# -*- coding: utf-8 -*-
"""Copy of Copy of Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MTLeLLz4hLflMaU0XXVfn52ndZJgXa6E
"""

# IMPLEMENT YOUR FUNCTIONS IN THIS CODE CELL OR
# IN THE PREVIOUS CODE CELL(S) THAT YOU MAY WANT TO CREATE



def sell_product(products):
  decision = input("Please enter products to sell: ").lower().split("-")
  for kkklaas in decision:
    kkklaas = kkklaas.split("_")

    if kkklaas[0] in products:

      if int(kkklaas[1]) > int(products[kkklaas[0]]) :
        print("There is not enough",kkklaas[0],"in inventory.")


      elif int(kkklaas[1]) == int(products[kkklaas[0]]):
        products.pop(kkklaas[0])
        print(kkklaas[1],kkklaas[0], "sold.")


      elif int(kkklaas[1]) < int(products[kkklaas[0]]) :
        print(kkklaas[1],kkklaas[0], "sold.")
        products[kkklaas[0]] = products[kkklaas[0]] - int(kkklaas[1])
        

    else:
      print(kkklaas[0],"does not exist in inventory.") 

def show_remaining(products):
  if products == {} : 
    print("Inventory is empty!")         
  elif not  products == {}:
    for karakan in products:
      print(karakan,":",products[karakan])



def import_inventory():
  dkka = {}
  falo = open("products.txt","r", encoding="latin-1")
  
  for line in falo:
    line = line.lower().strip().split("-")
    for okalitupus in line:
      okalitupus=okalitupus.split("_")
      if okalitupus[0] not in dkka :  
        dkka[okalitupus[0]] = int(okalitupus[1])
      elif okalitupus[0] in dkka:
        dkka[okalitupus[0]] = dkka[okalitupus[0]]   + int(okalitupus[1]) 



  holla = []
  pola = []
  verisye = {}

  falo.close()
  
  for makar in dkka :
    holla.append(makar)
  holla.sort()
  for okal in holla :
     pola.append(dkka[okal])
  for meb in holla :
    ilt =holla.index(meb)
    verisye[meb] = int(pola[ilt])   





  return verisye

# DO NOT MODIFY THIS CODE CELL, JUST RUN IT

products = import_inventory()
decision = ""
while decision != "3":
  print("*---------------------------")
  print("[1] Sell products")
  print("[2] Show remaining inventory")
  print("[3] Terminate")

  decision = input("Please enter your decision: ")
  print("____________________________")
  if decision == "1":
    sell_product(products)
  elif decision == "2":
    show_remaining(products)
  elif decision == "3":
    print("Terminating...")
  else:
    print("Invalid input!")