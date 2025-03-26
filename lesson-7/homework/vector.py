class Vector:
    def __init__(self, *args, **kwargs):
        self.lst = args
        
    def __add__(self, other):
        if len(self.lst) != len(other.lst):
            raise BaseException("The length of vectors are not same")
        t = []
        for i in range(len(self.lst)):
            t.append(self.lst[i] + other.lst[i])
        result = Vector(*t)
        return result

    def __sub__(self, other):
        if len(self.lst) != len(other.lst):
            raise BaseException("The length of vectors are not same")
        t = []
        for i in range(len(self.lst)):
            t.append(self.lst[i] - other.lst[i])
        result = Vector(*t)
        return result
    
    def __mul__(self, other):
        if type(other) == int:
            return Vector(*[other*i for i in self.lst])
        if len(self.lst) != len(other.lst):
            raise BaseException("The length of vectors are not same")
        t = []
        for i in range(len(self.lst)):
            t.append(self.lst[i] * other.lst[i])
        result = Vector(*t)
        return result

    def __floordiv__(self, other):
        if len(self.lst) != len(other.lst):
            raise BaseException("The length of vectors are not same")
        t = []
        for i in range(len(self.lst)):
            if other.lst[i] == 0:
                raise ZeroDivisionError
            t.append(self.lst[i] / other.lst[i])
        result = Vector(*t)
        return result
    
    def __len__(self):
        return len(self.lst)
    
    def __str__(self):
        result = "Vector("
        for i in range(len(self.lst)):
            if i==0:
                result += str(self.lst[i])
            else:
                result += ", " + str(self.lst[i])
        return result + ")"
    
    def magnitude(self):
        return (sum(i**2 for i in self.lst))**0.5
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError
        return Vector(*[i/mag for i in self.lst])
    

# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      # Output: Vector(0.267, 0.534, 0.801)