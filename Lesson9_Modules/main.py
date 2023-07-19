#import Lesson9_Modules.arithmetics as module
#from Lesson9_Modules import arithmetics
#from Lesson9_Modules.Folder1.Folder2.Folder3.arithmetics import sum as sum1
#from Lesson9_Modules.Folder1.Folder2.Folder3.arithmetics2 import sum as sum2


first_person_salary = 70
second_person_salary = 120
#print(module.sum(first_person_salary, second_person_salary))
#print(sum)
#print(arithmetics.sum(first_person_salary, second_person_salary))


from Lesson9_Modules import sum as sum1
from Lesson9_Modules.Folder1.Folder2.Folder3.arithmetics2 import sum as sum2
print(sum1(first_person_salary, second_person_salary))
print(sum2(first_person_salary, second_person_salary, 500))


import Lesson9_Modules
print(Lesson9_Modules.sum(1, 2))
print(Lesson9_Modules.difference(5000, 2501))


from Lesson9_Modules.New_directory.New_directory1.application1 import summ as new_exellent_sum
print(new_exellent_sum(15, 20))
