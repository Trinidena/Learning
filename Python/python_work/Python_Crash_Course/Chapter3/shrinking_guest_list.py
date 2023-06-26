guest_list = []                 #Excercise 3.7 Arrays
print(guest_list)
guest_list.append('Jesus')
print(guest_list)
guest_list.append('Edwin')
print(guest_list)
guest_list.append('Miguel')
print(guest_list)

print(guest_list[0] + ' is invited')
print(guest_list[1] + ' is invited')
print(guest_list[2] + ' is invited')

print('Jesus can\'t make it')
del guest_list[0]
guest_list.insert(0 , 'Joshua')
print(guest_list)

print(guest_list[0] + ' is invited')
print(guest_list[1] + ' is invited')
print(guest_list[2] + ' is invited')

print('I found a bigger dining table!')

guest_list.insert(0 , 'Fabian')
guest_list.insert(2, 'Isaac')
guest_list.append('Ian')

print(guest_list) #

print(guest_list[0] + ' is invited')
print(guest_list[1] + ' is invited')
print(guest_list[2] + ' is invited')
print(guest_list[3] + ' is invited')
print(guest_list[4] + ' is invited')
print(guest_list[5] + ' is invited')

print('I can only invite two people for dinner, the table is arriving late.')

uninvited_guest1 = guest_list.pop()
print('I\'m sorry I can\'t invite you, ' + uninvited_guest1 + '.')
uninvited_guest1 = guest_list.pop(0)
print('I\'m sorry I can\'t invite you, ' + uninvited_guest1 + '.')
uninvited_guest1 = guest_list.pop(1)
print('I\'m sorry I can\'t invite you, ' + uninvited_guest1 + '.')
uninvited_guest1 = guest_list.pop(2)
print('I\'m sorry I can\'t invite you, ' + uninvited_guest1 + '.')

print(guest_list)
print('You are still invited, ' + guest_list[0] + ' and ' + guest_list[1])
