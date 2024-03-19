# Case-study #3
# Developers: Ekin Viacheslaw, Amat Tolkochokov, Ilya Sokolov, Askar Gazizov
#
import ru_local as ru

def det_protection(protectionism):
    '''
    The function returns true or false, depending on whether the country is pursuing
    a protectionist policyThe function returns true or false, depending on whether the country
    is pursuing a protectionist policy
    '''
    return protectionism == "no"


def medium_candy_shops(people, candy_shops):
    '''
    The function returns true if the number of factories per 100,000 people
    does not exceed the number of factories
    already built, and False on the contrary.
    '''
    if people % 100000 == 0:
        return candy_shops < (people // 100000)
    return candy_shops < (people // 100000) + 1


def need_shops(people, candy_shops):
    '''
    The function determines how many
    factories need to be built in the country
    '''
    if people % 100000 == 0:
        return (people // 100000) - candy_shops
    return ((people // 100000) + 1) - candy_shops


def analysis(n):
    '''
    the function returns true if the number of people
     who love sweets is greater than or equal to 6
    '''
    match n:
        case 0 | 1 | 2 | 3 | 4 | 5:
            return False
        case 6 | 7 | 8 | 9 | 10:
            return True
        case _:
            return False
def main():
    countries = []
    protectionism = []
    population = []
    factories = []
    love_candy = []
    amount = 0

    while True:
        countries.append(input(ru.COUNTRY_NAME))
        protectionism.append(input(ru.PROTECTIONISM).lower())
        population.append(int(input(ru.PEOPLE)))
        factories.append(int(input(ru.FABRICS)))
        love_candy.append(int(input(ru.LOVE)))
        vote = input(ru.CHOOSE).lower()
        print()
        if vote == 'yes':
            pass
        elif vote == 'no':
            break
    for index in range(len(countries)):

        if (det_protection(protectionism[index]) and medium_candy_shops(population[index], factories[index])
                and analysis(love_candy[index])):
            need_fabrics = need_shops(population[index], factories[index])
            amount += need_fabrics

            print(f"{ru.COUNTRY} - {countries[index]}. {ru.NEED}: {need_fabrics}")
        else:
            print(f"{ru.COUNTRY} - {countries[index]}. {ru.NOT_GO}!")

    print(f"\n{ru.ALL}: {amount}")



if __name__ == '__main__':
    main()
