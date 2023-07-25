age = int(input("შეიყვანეთ თქვენი ასაკი: "))
is_under_18 = age < 18
print(is_under_18)


father_age = int(input("შეიყვანეთ მამისის ასაკი: "))
user_age = int(input("შეიყვანეთ თქვენი ასაკი: "))

father_over_60 = father_age > 60
user_over_60 = user_age > 60

print("მამისი არის 60 წელზე მეტი:", father_over_60)
print("თქვენი არის 60 წელზე მეტი:", user_over_60)
