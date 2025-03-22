def _convert_cel_to_far():
    cs=float(input("Enter a temperature in degrees F:"))
    F = cs * 9/5 + 32
    print(f"{cs} degrees F = {F} degrees C")
_convert_cel_to_far





def _convert_far_to_cel():
    fs=float(input("Enter a temperature in degrees C:"))
    C = (fs - 32) * 5/9
    print(f"{fs} degrees C = {C} degrees F") 
_convert_far_to_cel