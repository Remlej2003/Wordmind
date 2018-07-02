import random
wordk = ["olifant", "neus", "laptop"]
gword = (random.choice(wordk))
endword = len(gword)*'$'
print('Welkom bij wordmind')
while True:
    print(endword)
    iword = str(input("Geef een woord "))
    