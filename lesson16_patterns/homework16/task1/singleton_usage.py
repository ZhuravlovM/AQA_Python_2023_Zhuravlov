from lesson16_patterns.homework16.task1.my_singleton import MySingleton

singleton_1 = MySingleton()
singleton_2 = MySingleton()

print("Check that singleton is valid:", singleton_1 is singleton_2)

singleton_1.value = input("Input value for singleton_1: ")

print("Check value in singleton_2:", singleton_2.value)
