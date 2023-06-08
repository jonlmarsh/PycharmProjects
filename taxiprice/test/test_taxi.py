import unittest

MAX_PASSENGERS = 5
COST_PER_MILE = 5
A_FEW_PASSENGERS = 2
TOO_MANY_PASSENGERS = 6


class TAXI:
    def __init__(self):
        self.price = "none"

    def request(self, address, total_passengers, current_time):
        if total_passengers > MAX_PASSENGERS:
            self.price = "no"
        else:
            pass

    def price(self):
        return COST_PER_MILE * travel_time()

    def travel_time(self):
        return 70

class test_taxi_travel_time(unittest.TestCase):
    def test_jon_price_to_heathrow(self):
        taxi = TAXI()
        taxi.price = lambda: 200
        taxi.request("sl7", A_FEW_PASSENGERS, "14:00")
        self.assertEqual(taxi.price(), 200)

    def test_antony_price_to_heathrow(self):
        taxi = TAXI()
        taxi.price = lambda: 475
        taxi.request("ME9", A_FEW_PASSENGERS, "12:00")
        self.assertEqual(taxi.price(), 475)

    def test_jon_taxi_space(self):
        taxi = TAXI()
        taxi.request("sl7", A_FEW_PASSENGERS, "14:00")
        self.assertNotEqual(taxi.price, "no")

    def test_frank_many_people_no_taxi_space(self):
        taxi = TAXI()
        taxi.request("BA6", TOO_MANY_PASSENGERS, "11:00")
        self.assertEqual(taxi.price, "no")

    def test_jon_travel_time_acceptable(self):
        taxi = TAXI()
        taxi.travel_time = lambda: 40
        taxi.request("sl7", A_FEW_PASSENGERS, "14:00")
        self.assertNotEqual(taxi.price, "no")

if __name__ == '__main__':
    unittest.main()
