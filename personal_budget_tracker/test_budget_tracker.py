import pytest
from datetime import datetime
from os import path
from budget_tracker import BudgetTracker
from transaction import Transaction

# Test creating a BudgetTracker object


def test_budget_tracker_initialization():
    bt = BudgetTracker()
    assert isinstance(bt, BudgetTracker)
    assert bt.transactions == []

# Test adding a valid transaction


def test_add_transaction_valid():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.date == "2023-04-05"
    assert t.category == "Food"
    assert t.amount == 25.50
    assert t.description == "Lunch"

# Test adding a transaction with an invalid date format


@pytest.mark.parametrize("invalid_date", ["2023-13-01", "2023-02-30", "04-05-2023"])
def test_add_transaction_invalid_date(invalid_date):
    bt = BudgetTracker()
    with pytest.raises(ValueError):
        bt.add_transaction(invalid_date, "Food", 25.50, "Lunch")

# Test adding a transaction with a negative amount


def test_add_transaction_negative_amount():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", -25.50, "Lunch")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.amount == -25.50

# Test adding a transaction with zero amount


def test_add_transaction_zero_amount():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 0.00, "Lunch")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.amount == 0.00

# Test adding a transaction with special characters in the description


def test_add_transaction_special_chars_description():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch @ Cafe!")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.description == "Lunch @ Cafe!"

# Test adding a transaction with an empty category


def test_add_transaction_empty_category():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "", 25.50, "Lunch")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.category == ""

# Test adding a transaction with a very large amount


def test_add_transaction_large_amount():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 1e10, "Expensive Meal")
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.amount == 1e10

# Test viewing transactions when there are no transactions


def test_view_transactions_empty(capsys):
    bt = BudgetTracker()
    bt.view_transactions()
    captured = capsys.readouterr()
    assert captured.out == ""

# Test viewing transactions when there are multiple transactions


def test_view_transactions_multiple(capsys):
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
    bt.add_transaction("2023-04-06", "Transport", 10.00, "Bus ticket")
    bt.view_transactions()
    captured = capsys.readouterr()
    assert "Lunch" in captured.out
    assert "Bus ticket" in captured.out


# # Test saving transactions to a file
# def test_save_to_file(tmp_path):
#     bt = BudgetTracker()
#     bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
#     file_path = tmp_path / "budget.csv"
#     bt.save_to_file(file_path)
#     assert file_path.exists()
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         assert len(lines) == 2  # Header + 1 transaction

# Test saving transactions to a file

# Test saving transactions to a file in the current directory
def test_save_to_file():
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
    bt.save_to_file()
    file_path = path.join(path.dirname(__file__), 'budget.csv')
    assert path.exists(file_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 2  # Header + 1 transaction


# def test_save_to_file(tmp_path):
#     bt = BudgetTracker()
#     bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
#     file_path = tmp_path / "budget.csv"
#     bt.save_to_file()
#     assert file_path.exists()
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         assert len(lines) == 2  # Header + 1 transaction

# Test handling file write errors


def test_save_to_file_write_error(monkeypatch):
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")

    def mock_open(*args, **kwargs):
        raise IOError("Mocked IOError")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(IOError):
        bt.save_to_file()

# Test loading transactions from a file


def test_load_from_file(tmp_path):
    file_path = tmp_path / "budget.csv"
    with open(file_path, 'w') as file:
        file.write("Date,Category,Amount,Description\n")
        file.write("2023-04-05,Food,25.50,Lunch\n")

    bt = BudgetTracker()
    bt.load_from_file()
    assert len(bt.transactions) == 1
    t = bt.transactions[0]
    assert t.date == "2023-04-05"
    assert t.category == "Food"
    assert t.amount == 25.50
    assert t.description == "Lunch"

# Test handling file read errors


def test_load_from_file_read_error(monkeypatch):
    bt = BudgetTracker()

    def mock_open(*args, **kwargs):
        raise OSError("Mocked OSError")

    monkeypatch.setattr("builtins.open", mock_open)
    with pytest.raises(OSError):
        bt.load_from_file()

# Test loading from a corrupted or incomplete file

# Test loading from a corrupted or incomplete file


def test_load_from_corrupted_file(tmp_path):
    file_path = path.join(path.dirname(__file__), 'budget.csv')
    with open(file_path, 'w') as file:
        file.write("Date,Category,Amount,Description\n")
        file.write("2023-04-05,Food,invalid,Lunch\n")

    bt = BudgetTracker()
    with pytest.raises(ValueError):
        bt.load_from_file()


# Test generating a category summary with no transactions


def test_category_summary_empty(capsys):
    bt = BudgetTracker()
    bt.category_summary()
    captured = capsys.readouterr()
    assert captured.out == "\nCategory Summary:\n"

# Test generating a category summary with multiple transactions


def test_category_summary_multiple(capsys):
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
    bt.add_transaction("2023-04-06", "Transport", 10.00, "Bus ticket")
    bt.category_summary()
    captured = capsys.readouterr()
    assert "Food: $25.50" in captured.out
    assert "Transport: $10.00" in captured.out

# Test generating a monthly report for a month with no transactions


def test_monthly_report_empty(capsys):
    bt = BudgetTracker()
    bt.monthly_report("2023", "04")
    captured = capsys.readouterr()
    assert captured.out == "\nTransactions for 2023-04\nTotal: $0.00\n"

# Test generating a monthly report for a month with multiple transactions

# Test generating a monthly report for a month with multiple transactions


def test_monthly_report_multiple(capsys):
    bt = BudgetTracker()
    bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
    bt.add_transaction("2023-04-06", "Transport", 10.00, "Bus ticket")
    bt.monthly_report("2023", "04")
    captured = capsys.readouterr()
    assert "- Lunch: $25.50" in captured.out
    assert "- Bus ticket: $10.00" in captured.out
    assert "Total: $35.50" in captured.out

# Test loading from a corrupted or incomplete file
# def test_load_from_corrupted_file(tmp_path):
#     file_path = tmp_path / "budget.csv"
#     with open(file_path, 'w') as file:
#         file.write("Date,Category,Amount,Description\n")
#         file.write("2023-04-05,Food,invalid,Lunch\n")

#     bt = BudgetTracker()
#     with pytest.raises(ValueError):
#         bt.load_from_file()
# def test_monthly_report_multiple(capsys):
#     bt = BudgetTracker()
#     bt.add_transaction("2023-04-05", "Food", 25.50, "Lunch")
#     bt.add_transaction("2023-04-06", "Transport", 10.00, "Bus ticket")
#     bt.monthly_report("2023", "04")
#     captured = capsys.readouterr()
#     assert "- Lunch: $25.50" in captured.out
#     assert "- Bus ticket: $10.00" in captured.out
#     assert "Total: $35.50" in captured.out
