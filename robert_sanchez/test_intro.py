# Introducing unit tests with pytest



#pytest is a library -- import it
import pytest

def greeting(first_name, last_name):
    return f'hi, {first_name, last_name}'



    # make a pytest test for the greeting function
'''
When we write tests using pytest
-each test is ITSELF a function
-instead of running python... we run pytest
'''

# check that the ACTUAL output matches the EXPECTED
def test_greet_yusuf():
    # get actual output of function
    actual = greeting('Yusuf', 'Boldem')

    #we TELL pythest what we EXPECT the output to be 
    expected = 'Hi, Usuf Boldem'

    assert actual == expected, 'Greeting should work for yusuf'

    def test_greet_mia():
        expected = 'Hi, Mia Jackson'
        actual = greeting ('Mia', 'Jackson')
        assert actual == expected, 'Greeting should work for mia jackson'





