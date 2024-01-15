#import lesson09_modules.arithmetics as module
#from lesson09_modules import arithmetics
#from lesson09_modules.folder1.folder2.folder3.arithmetics import sum as sum1
#from lesson09_modules.folder1.folder2.folder3.arithmetics2 import sum as sum2


first_person_salary = 70
second_person_salary = 120
#print(module.sum(first_person_salary, second_person_salary))
#print(sum)
#print(arithmetics.sum(first_person_salary, second_person_salary))


from lesson09_modules import sum as sum1
from lesson09_modules.folder1.folder2.folder3.arithmetics2 import sum as sum2
print(sum1(first_person_salary, second_person_salary))
print(sum2(first_person_salary, second_person_salary, 500))


import lesson09_modules
print(lesson09_modules.sum(1, 2))
print(lesson09_modules.difference(5000, 2501))


from lesson09_modules.new_directory.new_directory1.application1 import summ as new_exellent_sum
print(new_exellent_sum(15, 20))
