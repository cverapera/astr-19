class Animal:
    def __init__(self, name, arm_length, leg_length, num_eyes, has_tail, is_furry):
        self.name = name
        self.arm_length = arm_length       # in centimeters (float)
        self.leg_length = leg_length       # in centimeters (float)
        self.num_eyes = num_eyes           # integer
        self.has_tail = has_tail           # boolean
        self.is_furry = is_furry           # boolean

    def describe(self):
        print(f"Animal: {self.name}")
        print(f"Arm Length: {self.arm_length} cm")
        print(f"Leg Length: {self.leg_length} cm")
        print(f"Number of Eyes: {self.num_eyes}")
        print(f"Has Tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is Furry: {'Yes' if self.is_furry else 'No'}")


# Create an instance of the class for a cat
cat = Animal(
    name="Cat",
    arm_length=25.0,   # average front leg length
    leg_length=30.0,   # average back leg length
    num_eyes=2,
    has_tail=True,
    is_furry=True
)

# Describe the cat
cat.describe()