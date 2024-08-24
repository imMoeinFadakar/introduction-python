# this one will make a chess table

def chess_border_maker(n: int , m: int):
    for row in range(1,n+1):
        print("#*", end=" ")
        for col in range(1,m):
            print("#*",end=" ")
        print()


# this one will create a multiply table

def multiply_table(n, m):

    for i in range(1, m+1):
        print(f"{i:>3}", end="")
    for _ in range(1, m+1):
        print()
    for i in range(1, n+1):
        print(f"{i:>3}|", end="")
        for j in range(1, m+1):
            print(f"{i*j:>3}", end=" ")
        print()

#  this One will create Diamond

def diamond(n):
    print("Diamond Pattern")
    for a1 in range(1, (n+1)//2 + 1): # this will print The First Half
        for a2 in range((n+1)//2 - a1):
            print(" ", end = "")
        for a3 in range((a1*2)-1):
            print("*", end = "")
        print()

    for a1 in range((n+1)//2 + 1, n + 1): # This will print The second half
        for a2 in range(a1 - (n+1)//2):
            print(" ", end = "")
        for a3 in range((n+1 - a1)*2 - 1):
            print("*", end = "")
        print()

# this is pascal triangle

def generate_pascal_triangle(num_rows):
    pascal_triangle = []

    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = pascal_triangle[i-1][j-1] + pascal_triangle[i-1][j]
        pascal_triangle.append(row)

    return print(pascal_triangle)



# this will check The user number for being INTEGER or not

def is_it_integer(args):
    if type(args) != int:
        return print(f" {args} not int")
    else:
        return args


#this will say "bye bye" to user

def bye():
    return print("bye bye")


