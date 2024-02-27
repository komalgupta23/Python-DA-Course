class Human:
    def __init__(self,nm,age,h,w,g,cntry):
        self.name = nm
        self.age = age
        self.height = h
        self.weight = w
        self.gender = g
        self.country = cntry
        
    def show(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')
        print(f'Weight: {self.weight}')
        
#making objects

h1 = Human('Ram', 23, 5.6, 67, 'M', 'Nepal')
h2 = Human('Krishna', 15, 6, 37, 'M', 'Bhutan')
h3 = Human('Komal', 21, 5.2, 50, 'F', 'India')

print(h1)
print(h2)
print(h3)


print(h3.name)
print(h2.name)

h1.show()
print('-'*15)
h3.show()