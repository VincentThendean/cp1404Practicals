from silver_service_taxi import SilverServiceTaxi


def main():
    test_taxi = SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)

    print(test_taxi)
    print(test_taxi.get_fare())
    test_taxi.drive(50)
    print(test_taxi.get_fare())

    test_taxi_2 = SilverServiceTaxi(name="Corolla", fuel=200, fanciness=2)
    print("\n18 km trip Corolla with 2 fanciness")
    test_taxi_2.drive(18)
    print(test_taxi_2.get_fare())


main()
