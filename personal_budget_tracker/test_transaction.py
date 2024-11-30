import pytest
from transaction import Transaction

# Test creating a Transaction with valid data


def test_transaction_initialization_valid():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=25.50, description="Lunch")
    assert t.date == "2023-04-05"
    assert t.category == "Food"
    assert t.amount == 25.50
    assert t.description == "Lunch"

# Test creating a Transaction with invalid date formats


@pytest.mark.parametrize("invalid_date", ["2023-13-01", "2023-02-30", "04-05-2023"])
def test_transaction_initialization_invalid_date(invalid_date):
    with pytest.raises(ValueError):
        Transaction(date=invalid_date, category="Food",
                    amount=25.50, description="Lunch")

# @pytest.mark.parametrize("invalid_date", ["2023-13-01", "2023-02-30", "04-05-2023"])
# def test_transaction_initialization_invalid_date(invalid_date):
#     with pytest.raises(ValueError):
#         Transaction(date=invalid_date, category="Food",
#                     amount=25.50, description="Lunch")

# Test creating a Transaction with negative amounts


def test_transaction_initialization_negative_amount():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=-25.50, description="Lunch")
    assert t.amount == -25.50

# Test creating a Transaction with zero amount


def test_transaction_initialization_zero_amount():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=0.00, description="Lunch")
    assert t.amount == 0.00

# Test with very large amount values


def test_transaction_initialization_large_amount():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=1e10, description="Lunch")
    assert t.amount == 1e10

# Test with special characters in the description


def test_transaction_initialization_special_chars_description():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=25.50, description="Lunch @ Cafe!")
    assert t.description == "Lunch @ Cafe!"

# Test with empty string values for description and category


def test_transaction_initialization_empty_description():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=25.50, description="")
    assert t.description == ""


def test_transaction_initialization_empty_category():
    t = Transaction(date="2023-04-05", category="",
                    amount=25.50, description="Lunch")
    assert t.category == ""

# Test with boundary dates (e.g., leap year dates, end of month)


@pytest.mark.parametrize("boundary_date", ["2024-02-29", "2023-12-31"])
def test_transaction_initialization_boundary_dates(boundary_date):
    t = Transaction(date=boundary_date, category="Food",
                    amount=25.50, description="Lunch")
    assert t.date == boundary_date

# ------------------------- other test cases -------------------------


# Test with maximum float value for amount
def test_transaction_initialization_max_float():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=float('inf'), description="Expensive Meal")
    assert t.amount == float('inf')

# Test with smallest positive float value for amount


def test_transaction_initialization_min_float():
    t = Transaction(date="2023-04-05", category="Food",
                    amount=float('1e-10'), description="Tiny Amount")
    assert t.amount == float('1e-10')

# Test with different valid date formats if supported


# "05-04-2023", "04/05/2023"])
@pytest.mark.parametrize("valid_date", ["2023-04-05"])  # , "2023/04/05"
def test_transaction_initialization_valid_date_formats(valid_date):
    t = Transaction(date=valid_date, category="Food",
                    amount=25.50, description="Lunch")
    assert t.date == valid_date

# Test creating a Transaction with future dates


def test_transaction_initialization_future_date():
    t = Transaction(date="2025-12-31", category="Food",
                    amount=25.50, description="Future Lunch")
    assert t.date == "2025-12-31"

# Test creating a Transaction with past dates


def test_transaction_initialization_past_date():
    t = Transaction(date="2000-01-01", category="Food",
                    amount=25.50, description="Past Lunch")
    assert t.date == "2000-01-01"

# Test creating a Transaction with a very long category name


def test_transaction_initialization_long_category():
    long_category = "A" * 256
    t = Transaction(date="2023-04-05", category=long_category,
                    amount=25.50, description="Lunch")
    assert t.category == long_category

# Test creating a Transaction with numeric category names or special characters


@ pytest.mark.parametrize("special_category", ["123", "@#$%", "Food & Drink"])
def test_transaction_initialization_special_category(special_category):
    t = Transaction(date="2023-04-05", category=special_category,
                    amount=25.50, description="Lunch")
    assert t.category == special_category

# Test creating a Transaction with a very long description


def test_transaction_initialization_long_description():
    long_description = "A" * 1024
    t = Transaction(date="2023-04-05", category="Food",
                    amount=25.50, description=long_description)
    assert t.description == long_description
