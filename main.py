# Case-study #3
# Developers: Ekin Viacheslaw, Amat Tolkochokov, Ilya Sokolov, Askar Gazizov
#
import ru_local as ru


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