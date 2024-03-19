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


if __name__ == '__main__':
    main()
