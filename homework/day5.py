a = True
b = False


result_and = a and b
print("and result:", result_and)  

# or ლოგიკური ოპერატორი
result_or = a or b
print("or result:", result_or) 

x = 5
y = 10


result_gt = x > y
print("x > y result:", result_gt) 

result_eq = x == y
print("x == y result:", result_eq)  


result_geq_or = x > y or x == y
print("x > y or x == y result:", result_geq_or)  # ჭეშმარიტი True


result_geq_and = x > y and x == y
print("x > y and x == y result:", result_geq_and)  