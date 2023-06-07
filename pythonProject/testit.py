import sum_dig_pow

@test.describe("Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!")
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        test.assert_equals(sum_dig_pow(10, 89),  [89])
        test.assert_equals(sum_dig_pow(10, 100),  [89])
        test.assert_equals(sum_dig_pow(90, 100), [])
        test.assert_equals(sum_dig_pow(89, 135), [89, 135])