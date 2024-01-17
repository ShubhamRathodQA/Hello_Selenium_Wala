# def test_plus():
#     a = 10
#     b = 20
#     result = a + b
#     assert result == 30
#
#
# def test_plus2():
#     a = 10
#     b = 20
#     result = a + b
#     assert result == 10
#
#
# def test_prog():
#     x = 30
#     y = 60
#     assert x == y
#
# import pytest
#
# @pytest.mark.parametrize("username,password",
#                         [
#                             ('Shubham', '1234'),
#                             ('Robert','downy'),
#                             ('Thor','Hemsworth'),
#                             ('Hulk','Bruce')
#                         ]
#                         )
#
# def test_avenger(username,password):
#     print(f"logging in the AVENGER :\nuser name:{username}, password:{password}")
#     if(username == 'Shubham' and password == '1234'):
#         assert True
#     else:
#         assert False

#=================================================================================================================

# import pytest
# import sys
#
# @pytest.mark.xfail      # it will execute all the time.. based on result it will be either xpassed or xfailed
# def test_t3():
#     x = 10
#     y = 20
#     result = x + y
#     assert result == 30

#=================================================================================================================

# import pytest
#
# @pytest.fixture
# def thisFirst():
#     print("Welcome to addition program")
#     yield
#     print("Thank you")
#
#
# def test_addition(thisFirst):
#     a = 30
#     b = 40
#     assert a == b

# import pytest
#
# @pytest.fixture
# def setup():
#     print("get driver")
#     print("maximize window")
#     yield       ### divide before and after activity
#     print("print title")
#     print("close window")


# def test_facebook_login(setup):
#     print("open facebook url")

#=================================================================================================================


def test_first():
    a = 10
    b = 20
    assert a == b       # assert True : test case pass, assert False : test case fail


def test_second():
    a = 10
    b = 20
    assert a != b       # assert True : test case pass, assert False : test case fail


def Test_third():       ## invalid name # T has to be small
    a = 10
    b = 20
    assert a == b


def four_test():        ## invalid name # start with test
    a = 10
    b = 20
    assert a == b



