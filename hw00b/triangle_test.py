def classify_triangle(a,b,c):
    sides = sorted([a, b, c])
    a, b, c = sides
    if a==b and a==c and b==c:
        return "equilateral"
    else:
        is_right = a**2 + b**2 == c**2
        triangle_type = ""

        if a == b or b == c or a == c:
            triangle_type = "isosceles"
        else:
            triangle_type = "scalene"

        return f"{triangle_type} right triangle" if is_right else triangle_type
