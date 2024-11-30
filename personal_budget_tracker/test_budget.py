import pytest
import threading
from collections import defaultdict
from budget import Budget

# Test creating a Budget object


def test_budget_initialization():
    b = Budget()
    assert isinstance(b, Budget)
    assert b.limits == {}
    assert isinstance(b.current_spending, defaultdict)

# Test setting a limit for a valid category


def test_budget_set_limit_valid():
    b = Budget()
    b.set_limit("Food", 500)
    assert b.limits["Food"] == 500

# Test setting a limit for a non-existent category


def test_budget_set_limit_non_existent():
    b = Budget()
    b.set_limit("Travel", 1000)
    assert b.limits["Travel"] == 1000

# Test updating an existing limit


def test_budget_update_limit():
    b = Budget()
    b.set_limit("Food", 500)
    b.set_limit("Food", 800)
    assert b.limits["Food"] == 800

# Test setting a limit with negative values


def test_budget_set_limit_negative():
    b = Budget()
    b.set_limit("Food", -200)
    assert b.limits["Food"] == -200

# Test setting a limit with zero value


def test_budget_set_limit_zero():
    b = Budget()
    b.set_limit("Food", 0)
    assert b.limits["Food"] == 0

# Test setting a limit with very high values


def test_budget_set_limit_high():
    b = Budget()
    b.set_limit("Food", 1e10)
    assert b.limits["Food"] == 1e10

# Test checking limits when spending is below the limit


def test_budget_check_limits_below(capsys):
    b = Budget()
    b.set_limit("Food", 500)
    b.current_spending["Food"] = 400
    b.check_limits()
    assert "Warning" not in capsys.readouterr().out

# Test checking limits when spending is exactly at the limit


def test_budget_check_limits_exact(capsys):
    b = Budget()
    b.set_limit("Food", 500)
    b.current_spending["Food"] = 500
    b.check_limits()
    captured = capsys.readouterr()
    assert "Warning" not in captured.out

# Test checking limits when spending exceeds the limit


def test_budget_check_limits_exceed(capsys):
    b = Budget()
    b.set_limit("Food", 500)
    b.current_spending["Food"] = 600
    b.check_limits()
    captured = capsys.readouterr()
    assert "Warning: Food spending" in captured.out

# Test checking limits for multiple categories


def test_budget_check_limits_multiple(capsys):
    b = Budget()
    b.set_limit("Food", 500)
    b.set_limit("Transport", 300)
    b.current_spending["Food"] = 600
    b.current_spending["Transport"] = 200
    b.check_limits()
    captured = capsys.readouterr()
    assert "Warning: Food spending" in captured.out
    assert "Warning: Transport spending" not in captured.out

# Test checking limits with no categories set


def test_budget_check_limits_no_categories(capsys):
    b = Budget()
    b.check_limits()
    captured = capsys.readouterr()
    assert captured.out == ""

# Test checking limits with negative spending


def test_budget_check_limits_negative_spending(capsys):
    b = Budget()
    b.set_limit("Food", 500)
    b.current_spending["Food"] = -100
    b.check_limits()
    captured = capsys.readouterr()
    assert "Warning" not in captured.out

# Test setting and checking limits with special characters in category names


def test_budget_special_characters_category():
    b = Budget()
    special_category = "Food & Drink!"
    b.set_limit(special_category, 500)
    b.current_spending[special_category] = 600
    b.check_limits()
    assert special_category in b.limits
    assert b.limits[special_category] == 500

# Test setting and checking limits with very long category names


def test_budget_long_category():
    b = Budget()
    long_category = "A" * 256
    b.set_limit(long_category, 500)
    b.current_spending[long_category] = 600
    b.check_limits()
    assert long_category in b.limits
    assert b.limits[long_category] == 500

# Test setting and checking limits with empty category names


def test_budget_empty_category():
    b = Budget()
    b.set_limit("", 500)
    b.current_spending[""] = 600
    b.check_limits()
    assert "" in b.limits
    assert b.limits[""] == 500

# Test checking limits after removing a category


def test_budget_remove_category():
    b = Budget()
    b.set_limit("Food", 500)
    del b.limits["Food"]
    b.check_limits()
    assert "Food" not in b.limits

# ---------------------- other test cases ----------------------


# Test setting limits and checking limits concurrently
def test_budget_concurrent_operations():
    b = Budget()

    def set_limits():
        for i in range(100):
            b.set_limit(f"Category_{i}", 1000)

    def check_limits():
        for i in range(100):
            b.check_limits()

    threads = []
    for _ in range(5):
        t1 = threading.Thread(target=set_limits)
        t2 = threading.Thread(target=check_limits)
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()

    for t in threads:
        t.join()

    # Verify some limits are set (can't ensure all due to race conditions)
    assert len(b.limits) > 0

# Test saving and loading budget limits to/from a file


def test_budget_persistence(tmp_path):
    file_path = tmp_path / "budget_limits.txt"

    b = Budget()
    b.set_limit("Food", 500)
    b.set_limit("Transport", 300)

    # Save to file
    with open(file_path, 'w') as f:
        for category, limit in b.limits.items():
            f.write(f"{category},{limit}\n")

    # Create a new Budget instance and load from file
    b_new = Budget()
    with open(file_path, 'r') as f:
        for line in f:
            category, limit = line.strip().split(',')
            b_new.set_limit(category, float(limit))

    # Verify limits are loaded correctly
    assert b_new.limits["Food"] == 500
    assert b_new.limits["Transport"] == 300

# Test handling of corrupted or incomplete budget files


def test_budget_corrupted_file(tmp_path):
    file_path = tmp_path / "corrupted_budget_limits.txt"

    b = Budget()
    b.set_limit("Food", 500)
    b.set_limit("Transport", 300)

    # Save corrupted data to file
    with open(file_path, 'w') as f:
        f.write("Food,500\n")
        f.write("Transport,invalid_data\n")

    b_new = Budget()
    with pytest.raises(ValueError):
        with open(file_path, 'r') as f:
            for line in f:
                category, limit = line.strip().split(',')
                b_new.set_limit(category, float(limit))

# Test resetting a budget limit for a category


def test_budget_reset_limit():
    b = Budget()
    b.set_limit("Food", 500)
    assert b.limits["Food"] == 500
    b.set_limit("Food", 0)
    assert b.limits["Food"] == 0

# Test resetting current spending for a category


def test_budget_reset_spending():
    b = Budget()
    b.current_spending["Food"] = 500
    assert b.current_spending["Food"] == 500
    b.current_spending["Food"] = 0
    assert b.current_spending["Food"] == 0

# Test performance and correctness with a very large number of categories


def test_budget_large_number_of_categories():
    b = Budget()
    num_categories = 10000
    for i in range(num_categories):
        b.set_limit(f"Category_{i}", 1000)
        b.current_spending[f"Category_{i}"] = 500

    assert len(b.limits) == num_categories
    assert len(b.current_spending) == num_categories
    for i in range(num_categories):
        assert b.limits[f"Category_{i}"] == 1000
        assert b.current_spending[f"Category_{i}"] == 500
