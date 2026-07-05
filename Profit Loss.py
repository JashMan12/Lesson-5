X=int(input("How much did you spend for your oranges?"))
A=int(input("How much did you sell your oranges for?"))

if X<A:
    print("That means you have profit of" ,A-X)

else:
    print("That mean you have loss of",X-A)