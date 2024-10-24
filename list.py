#___________List_basic_operation_________________________________________________
#___________Min_Max_Sort_________________________________________________________
numbers=[6,4,2,5,3,8]
print(min(numbers))                  #Output : 2
print(max(numbers))                  #Output : 8
numbers.sort()
print(numbers)                       #Output : [2,3,4,5,6,8]
list1=[]
#__________append()______________________________________________________________
list1.append("Ram")                  #Output  ["Ram"]
list1.append("Shiv")                 #Output  ["Ram","Shiv"]
list1.append(25)                     #Output  ["Ram","Shiv",25]  
list1.append(2.5)                    #Output  ["Ram","Shiv",25,2.5]
#__________insert()_______________________________________________________________
list1.insert(1,"Radhe")              #Output ["Ram","Radhe","Shiv",25,2.5]
list1.insert(3,"Rakesh")             #Output ["Ram","Radhe","Shiv","Rakesh",25,2.5]
#__________pop____________________________________________________________________
list1.pop()                          #output["Ram","Radhe","Shiv","Rakesh",25]
list1.pop(2)                         #ouput["Ram","Radhe","Rakesh",25]
#_________remove__________________________________________________________________
list1.remove("Ram")                  #output["Radhe","Rakesh",25]
#_________Reverse_________________________________________________________________
list1.reverse()                      #Output[25,"Rakesh","Radhe"]
#_________Count___________________________________________________________________
c=list1.count("Rakesh")
print(c)                             #Output : 1
#________extend__________________________________________________________________
numbers.extend(list1)
print(numbers)                       #Output : [2,3,4,5,6,8,25,"Rakesh","Radhe"]
#________clear___________________________________________________________________
list1.clear()
print(list1)                         #Output :[]

