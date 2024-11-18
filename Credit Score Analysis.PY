def calculate_credit_score(income, debt, payment_history):
    """
    Calculates a simple credit score based on income, debt, and payment history.
    """
    base_score = 300
    income_factor = min(income / 1000, 100)  # Limit income contribution to 100 points
    debt_factor = max(0, 50 - debt / 1000)   # Debt decreases score, max impact 50 points
    payment_factor = payment_history * 100  # Payment history contributes 0-100 points

    # Total score
    credit_score = base_score + income_factor + debt_factor + payment_factor
    return min(850, max(300, round(credit_score)))  # Credit score capped between 300-850


# User inputs
print("Enter the following details for credit score calculation:")
income = float(input("Monthly income (in $): "))
debt = float(input("Total debt (in $): "))
payment_history = float(input("Payment history (fraction of on-time payments, 0 to 1): "))

# Calculate and display credit score
score = calculate_credit_score(income, debt, payment_history)
print(f"Your estimated credit score is: {score}")
