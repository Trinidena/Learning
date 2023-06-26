#Exercise 3.5

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