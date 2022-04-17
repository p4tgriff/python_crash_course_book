# Try it yourself, create a guest list that includes 3 people, living or dead that you could invite to dinner.

dinner_list = []
dinner_list.append('Nikola Telsa')
print(dinner_list)

dinner_list.append('George Washington')
print(dinner_list)

dinner_list.append('Jesus')
print(dinner_list)

dinner_list.remove('Jesus')
dinner_list.append('Mark Twain')
print(dinner_list)

dinner_list.insert(0, 'Elon Musk')
print(dinner_list)

del dinner_list[0]
message = "Sorry, you've been uninvited."
print(dinner_list)
print(message)

del dinner_list[0]
message = "Sorry, you've been uninvited."
print(dinner_list)
print(message)

message_invited = "We'll see you two at dinner!"
print(message_invited)

del dinner_list[0]
print(dinner_list)

del dinner_list[0]
print(dinner_list)

print(len(dinner_list))
