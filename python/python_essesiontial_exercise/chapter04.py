# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:18:02 2018

@author: Administrator
"""
##print()
#print(1.23 == 1)
#print(1.0 == 1)
##False
##True
#a = "An enhanced Interactive Python."
#b = "Parent poll failed. "
#c = "ipython-dev@scipy.org"
#
#print(a[-len("apples"):-1]) #从右边开始算起
#apples = ["copyright", "credits" , "license"]
#apples_tree = ["copyright", "credits" , "license","license"]
#print(apples == apples_tree)
#apples_tree =  ["copyright", "credits" , "license"]
#print(apples == apples_tree)
#
#tuesday_breakfasts_sold = {"apple":10,"pear":12,"cherry":20}
#wednesday_breakfasts_sold = {"watermelon":10,"pear":12,"cherry":20}
#print(tuesday_breakfasts_sold == wednesday_breakfasts_sold)
#wednesday_breakfasts_sold = {"apple":10,"cherry":20,"pear":12}
#print(tuesday_breakfasts_sold == wednesday_breakfasts_sold)

#4.2
#print( "credits" >  "creditz")
#print( "credits" ==  "creditS")
#print( "credits".upper() ==  "creditS".upper())
#print( "credits".lower() ==  "creditS".lower())
#a = 5
#print(a is 5)
#print(not a is 5)
#
#if a is 5:
#    print("true")
#else:
#    print("false")

#4.6
#loop = input("how many time would you want:")
#if loop == "no":
#    print("nothing to do ")
#else:
#    i=int(loop)
#    while i > 0:
#        print("index :%d" %(i))
#        i = i -1
#
for food in ("copyright", "credits","license","apple"):
#    if food == "apple":
   print("food:"+food[0:5])
   if food[0:5] == "apple":
       break
   else:
       print(food)

#4.7

#wednesday_breakfasts_sold = {"apple":10,"cherry":20,"pear":12}
#try:
#    if wednesday_breakfasts_sold["water"] > 3:
#        print("sure,  let's have the water");
#except (KeyError) as result:
#        print("woah! there is no %s" % result)
#except (TypeError):
#        pass
    




