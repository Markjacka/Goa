a = True
b = False

# and ლოგიკური ოპერატორი
result_and = a and b
print("and შედეგი:", result_and)  # ელბალი False

# or ლოგიკური ოპერატორი
result_or = a or b
print("or შედეგი:", result_or)  # ჭეშმარიტი True

# შემოწმება 2: ლოგიკური შედარების ოპერატორები

x = 5
y = 10

# ტოლობა: x ნაკრების დადებით იარებს y ნაკრებს
result_gt = x > y
print("x > y შედეგი:", result_gt)  # ელბალია False

# ტოლობა: x ნაკრების ნაკრებთან ტოლობა
result_eq = x == y
print("x == y შედეგი:", result_eq)  # ელბალია False

# ტოლობა: x ნაკრების მეტია ან ტოლობა y ნაკრების ნაკრებთან
result_geq_or = x > y or x == y
print("x > y or x == y შედეგი:", result_geq_or)  # ჭეშმარიტი True

# ტოლობა: x ნაკრების მეტია დადებით და ტოლობა y ნაკრების ნაკრებთან
result_geq_and = x > y and x == y
print("x > y and x == y შედეგი:", result_geq_and)  # ელბალია False