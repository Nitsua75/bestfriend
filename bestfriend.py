first_name = input("what is your name? ")
print(f"Hello {first_name}",)
best = input("Who is the best? ")
print(f"NO! {best} is not the best, I am the best!")
while True:

    if best == first_name:
        print("You Are thes best as well!!!")
        break
    else:
        first_name = input("what is your name? ")
        print(f"Hello {first_name}",)
        best = input("Who is the best? ")
        print(f"NO! {best} is not the best, I am the best!")