"""
Business rules translated from legacy PL/SQL logic.
Decision trace added for explainability.
"""

def evaluate_eligibility(customer) -> dict:
    decisions = []
    eligible = True

    if customer.monthly_usage > 600:
        eligible = False
        decisions.append("Rejected: monthly usage above 600")

    if customer.customer_type == "VIP":
        eligible = True
        decisions.append("Override: VIP customer")

    if customer.debt_amount > 1000:
        eligible = False
        decisions.append("Rejected: outstanding debt above 1000")

    return {
        "eligible": eligible,
        "decision_trace": decisions
    }
