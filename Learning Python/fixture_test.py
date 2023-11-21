# # import pytest
# #
# #
# # @pytest.fixture
# # def order():
# #     return []
# #
# #
# # @pytest.fixture
# # def append_first(order):
# #     order.append(1)
# #
# #
# # @pytest.fixture
# # def append_second(order, append_first):
# #     order.extend([2])
# #
# #
# # @pytest.fixture(autouse=True)
# # def append_third(order, append_second):
# #     order += [3]
# #
# #
# # def test_order(order):
# #     assert order == [1, 2, 3]
#
# import pytest
#
#
# @pytest.fixture
# def order():
#     return []
#
#
# @pytest.fixture
# def outer(order, inner):
#     order.append("outer")
#
#
# class TestOne:
#     @pytest.fixture
#     def inner(self, order):
#         order.append("one")
#
#     def test_order(self, order, gouter):
#         assert order == ["one", "outer"]


import pytest

# Arrange
@pytest.fixture
def first_entry():
    return "a"
# Arrange
@pytest.fixture
def order():
    return []
# Act
@pytest.fixture
def append_first(order, first_entry):
    return order.append(first_entry)

def test_append_first(append_first):
    # Assert
    assert append_first == None

def test_string_only(append_first, order, first_entry):
    # Assert
    assert order == [first_entry] # This is because order is executed only once(during append_first,
    # else it should have been overriden by [],
    # but no rule is FIXTURES can be requested more than once per test but return values are
    # cached(not computed at every call).

def test_order(order):
    assert order == []

def test_first_entry(first_entry):
    assert first_entry == "a"

@pytest.fixture(autouse=True)
def append_second(order, first_entry):
    return order.append(first_entry)

def test_string(order, first_entry):
    assert order == [first_entry]

def test_string_and_int(order, first_entry):
    order.append(first_entry)
    assert order == [first_entry, first_entry]

