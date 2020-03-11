guest_list=['Emilly', 'Alice' , 'Brianna' ,'Harold']
print(guest_list[0].title())
print(guest_list[1].title())
print(guest_list[2].title())
print(guest_list[3].title())
guest_zero=guest_list.pop(0)
print(f"I would like for you to come to dinner tonight {guest_zero.title()}.")
guest_one=guest_list.pop(0)
print(f"I would like for you to come to dinner tonight {guest_one.title()}.")
guest_two=guest_list.pop(0)
print(f"I would like for you to come to dinner tonight {guest_two.title()}.")
guest_three=guest_list.pop(0)
print(f"I would like for you to come to dinner tonight {guest_three.title()}.")

guest_missing='Harold'
print(guest_missing)
print(f"I am sorry that you can't make it to dinner {guest_missing.title()}.")


message="I just found a bigger dinner table and I am to invite more guests"
print(message)
guest_list=['Emilly','Alice','Brianna']
print(guest_list)
guest_list.insert(0, 'Kerry')
print(guest_list)

print(guest_list)
guest_list.insert(2, 'Bonface')
print(guest_list)
guest_list.append('Hellen')
print(guest_list)
guest_list.append('Mevline')
print(guest_list)

new_guests_one=guest_list.pop(0)
print(f"I would like to invite you to dinner tonight {new_guests_one.title()}.")
new_guests_two=guest_list.pop(0)
print(f"I would like to invite you to dinner tonight {new_guests_two.title()}.")
new_guests_three=guest_list.pop(0)
print(f"I would like to invite you to dinner tonight {new_guests_three.title()}.")
new_guests_four=guest_list.pop(0)
print(f"I would like to invite you to dinner tonight {new_guests_four.title()}.")
new_guests_five=guest_list.pop(0)
print(f"I would like to invite you to dinner tonight {new_guests_five.title()}.")
new_guests_six=guest_list.pop(0)
print(f"I would like to invte you to dinner tonight {new_guests_six.title()}.")

dinner_message_to_guests='Only two guests can attend. I am sorry guests'
print(dinner_message_to_guests)

final_dinners=['Kerry', 'Emilly', 'Bonface', 'Alice', 'Brianna', 'Hellen']
dinner_one=final_dinners.pop()
print(f"You can't attend dinner tonight {dinner_one.title()}.")
dinner_two=final_dinners.pop()
print(f"You can't attend dinner tonight {dinner_two.title()}.")
dinner_three=final_dinners.pop()
print(f"You can't attend dinner tonight {dinner_three.title()}.")
dinner_four=final_dinners.pop()
print(f"You can't attend dinner tonight {dinner_four.title()}.")
print(final_dinners)
final_dinners.insert(0, 'Ruth')
final_dinners.insert(2, 'Charles')
final_dinners.append('Anna')
print(final_dinners)

print(final_dinners[0])
print(final_dinners[1])
print(final_dinners[2])
print(final_dinners[3])
print(final_dinners[4])

finalist_one=final_dinners.pop(0)
print(f"I invite you to dinner tonight {finalist_one.title()}.")
finalist_two=final_dinners.pop(0)
print(f"I invite you to dinner tonight {finalist_two.title()}.")
finalist_three=final_dinners.pop(0)
print(f"I invite you to dinner tonight {finalist_three.title()}.")
finalist_four=final_dinners.pop(0)
print(f"I invite you to dinner tonight {finalist_four.title()}.")
finalist_five=final_dinners.pop(0)
print(f"I invite you to dinner tonight {finalist_five.title()}.")

message="I can only invite two guests since the huge table won't arrive in time. Sorry for the inconvinience"
print(message)
dine=['Ruth', 'Kerry', 'Charles', 'Emilly', 'Anna']
print(dine)
dine_miss_one=dine.pop(0)
print(f"I am sorry you are not invited to dinner tonight {dine_miss_one.title()}.")
dine_miss_two=dine.pop(0)
print(f"I am sorry you are not invited to dinner tonight {dine_miss_two.title()}.")
dine_miss_three=dine.pop(0)
print(f"I am sorry you are not invited to dinner tonight {dine_miss_three.title()}.")
print(dine)
dine_attend_one=dine.pop(0)
print(f"You are still invited to dinner tonight {dine_attend_one.title()}.")
dine_attend_two=dine.pop(0)
print(f"You are still invited to dinner tonight {dine_attend_two.title()}.")
visitors='Emilly', 'Anna','None'

del visitors[0]
print(visitors)