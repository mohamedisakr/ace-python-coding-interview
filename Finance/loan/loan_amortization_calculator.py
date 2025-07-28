import math


def calculate_loan_amortization(principal, annual_interest_rate, loan_term_years, payments_per_year):
    """
    Calculates and prints the amortization schedule for a loan.

    Args:
        principal (float): The initial amount of the loan.
        annual_interest_rate (float): The yearly interest rate as a decimal (e.g., 0.05 for 5%).
        loan_term_years (int): The total number of years to repay the loan.
        payments_per_year (int): How often payments are made (e.g., 12 for monthly, 4 for quarterly).

    Returns:
        list: A list of dictionaries, where each dictionary represents a payment
              and contains 'payment_number', 'starting_balance', 'payment_amount',
              'interest_paid', 'principal_paid', and 'ending_balance'.
    """

    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate cannot be negative.")
    if loan_term_years <= 0:
        raise ValueError("Loan term in years must be greater than zero.")
    if payments_per_year <= 0:
        raise ValueError("Payments per year must be greater than zero.")

    # 1. Calculate the Periodic Interest Rate
    periodic_interest_rate = annual_interest_rate / payments_per_year

    # 2. Calculate the Total Number of Payments
    total_payments = loan_term_years * payments_per_year

    # 3. Calculate the Periodic Payment (Monthly Payment if payments_per_year is 12)
    if periodic_interest_rate == 0:
        # Handle zero interest rate case to avoid division by zero
        periodic_payment = principal / total_payments
    else:
        # Standard amortization formula
        periodic_payment = principal * (
            (periodic_interest_rate * (1 + periodic_interest_rate)**total_payments) /
            ((1 + periodic_interest_rate)**total_payments - 1)
        )

    print(f"\n--- Loan Amortization Schedule ---")
    print(f"Loan Principal: ${principal:,.2f}")
    print(f"Annual Interest Rate: {annual_interest_rate:.2%}")
    print(f"Loan Term: {loan_term_years} years")
    print(f"Payments Per Year: {payments_per_year}")
    print(f"Total Payments: {total_payments}")
    print(f"Calculated Periodic Payment: ${periodic_payment:,.2f}")
    print("-" * 40)

    amortization_schedule = []
    current_balance = principal
    total_interest_paid = 0

    # Generate the Amortization Schedule
    print(f"{'Payment #':<12} {'Starting Balance':<20} {'Payment':<15} {'Interest Paid':<15} {'Principal Paid':<15} {'Ending Balance':<20}")
    print("-" * 110)

    for i in range(1, total_payments + 1):
        interest_paid = current_balance * periodic_interest_rate
        principal_paid = periodic_payment - interest_paid

        # Adjust the last payment to ensure balance goes to exactly zero
        if i == total_payments:
            principal_paid = current_balance  # Pay off remaining balance
            periodic_payment = interest_paid + principal_paid  # Adjust last payment amount
            ending_balance = 0.0
        else:
            ending_balance = current_balance - principal_paid
            # Ensure ending balance doesn't go negative due to minor floating point inaccuracies
            # Check if it's a tiny negative
            if ending_balance < 0 and abs(ending_balance) < 0.01:
                ending_balance = 0.0
                principal_paid = current_balance  # Force principal paid to clear remaining balance
                periodic_payment = interest_paid + principal_paid  # Adjust last payment

        total_interest_paid += interest_paid
        current_balance = ending_balance

        payment_details = {
            'payment_number': i,
            'starting_balance': principal if i == 1 else amortization_schedule[-1]['ending_balance'],
            'payment_amount': periodic_payment,
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'ending_balance': ending_balance
        }
        amortization_schedule.append(payment_details)

        print(f"{i:<12} ${payment_details['starting_balance']:<19.2f} ${payment_details['payment_amount']:<14.2f} ${payment_details['interest_paid']:<14.2f} ${payment_details['principal_paid']:<14.2f} ${payment_details['ending_balance']:<19.2f}")

    print("-" * 110)
    print(f"Total Interest Paid Over Loan Term: ${total_interest_paid:,.2f}")
    print(
        f"Total Paid (Principal + Interest): ${principal + total_interest_paid:,.2f}")
    print("-" * 40)

    return amortization_schedule


# --- Example Usage ---
if __name__ == "__main__":
    try:
        # Example 1: Standard Home Loan
        print("Calculating a standard 30-year mortgage...")
        schedule1 = calculate_loan_amortization(
            principal=300000,
            annual_interest_rate=0.045,  # 4.5%
            loan_term_years=30,
            payments_per_year=12  # Monthly payments
        )

        # Example 2: Car Loan
        print("\nCalculating a 5-year car loan...")
        schedule2 = calculate_loan_amortization(
            principal=25000,
            annual_interest_rate=0.06,  # 6%
            loan_term_years=5,
            payments_per_year=12  # Monthly payments
        )

        # Example 3: Short-term, high-interest loan
        print("\nCalculating a 1-year personal loan...")
        schedule3 = calculate_loan_amortization(
            principal=5000,
            annual_interest_rate=0.10,  # 10%
            loan_term_years=1,
            payments_per_year=12  # Monthly payments
        )

        # Example 4: Loan with quarterly payments
        print("\nCalculating a 10-year loan with quarterly payments...")
        schedule4 = calculate_loan_amortization(
            principal=100000,
            annual_interest_rate=0.03,  # 3%
            loan_term_years=10,
            payments_per_year=4  # Quarterly payments
        )

        # Example 5: Zero interest loan (for testing edge case)
        print("\nCalculating a 2-year interest-free loan...")
        schedule5 = calculate_loan_amortization(
            principal=12000,
            annual_interest_rate=0.0,  # 0% interest
            loan_term_years=2,
            payments_per_year=12  # Monthly payments
        )

        # Example of handling an invalid input
        # print("\nAttempting to calculate with invalid input...")
        # schedule_invalid = calculate_loan_amortization(
        #     principal=-1000,
        #     annual_interest_rate=0.05,
        #     loan_term_years=10,
        #     payments_per_year=12
        # )

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
