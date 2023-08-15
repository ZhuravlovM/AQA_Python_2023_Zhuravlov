class MySingleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


instance_1 = MySingleton()
instance_2 = MySingleton()

print(instance_1 is instance_2)
