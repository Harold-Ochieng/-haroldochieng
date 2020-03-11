#LISTING ELEMENTS
family=['dad','mum','harold','mevline','venesa','kerry']
print(family) #this prints the whole list of family members
family[2]='alice'
print(family)#alice is added and replaces character two
family[0]='brianna'
print(family)#brianna is added and replaces character zero

#ADDING MEMBERS
#in case you want to add members to a list without affecting the already existing one, use .append() as shown below
family=['dad','mum','harold','mevline','venesa','kerry']
print(family)
family.append('alice') #adds alice at the end of the list
print(family)
family.append('brianna')#adds brianna at the end of the list after brianna
print(family)

#INSERTING MEMBERS
#initialise with a no. e.g motorcyles.insert(0, 'bajaj')
family=['dad','mum','harold','mevline','venesa','kerry']
print(family)
family.insert(3, 'alice')#inserts alice as character 3 in the list
print(family)
family.insert(7, 'brianna')#inserts brianna as character 7 in the list
print(family)

#REMOVING MEMBERS FROM LIST
#initialize with del example del motorcycle(0)
del family[0]#deletes character 0 from the list
print(family)

#pop( ) command-removes last item on a list and uses it later or replaces it
install=['sudo','su','apt','get']
print(install)
popped_install=install.pop()
print(install)
print(f"I don't need {popped_install.lower()}.")

laptops=['acer','toshiba','dell','lenovo','hp']
last_owned=laptops.pop()
print(f"The last laptop I owned was a {last_owned.title().upper()}.")

#removing an item by value
names=['harold','ochieng','otieno']
print(names)
names.remove('otieno')#removes the item otieno form the list of names
print(names)