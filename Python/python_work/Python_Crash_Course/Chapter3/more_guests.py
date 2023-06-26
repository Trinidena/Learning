guest_list = []
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

#Exercise 3.6

print('I found a bigger dining table!')

guest_list.insert(0 , 'Fabian')
guest_list.insert(2, 'Isaac')
guest_list.append('Ian')

print(guest_list)

print(guest_list[0] + ' is invited')
print(guest_list[1] + ' is invited')
print(guest_list[2] + ' is invited')
print(guest_list[3] + ' is invited')
print(guest_list[4] + ' is invited')
print(guest_list[5] + ' is invited')