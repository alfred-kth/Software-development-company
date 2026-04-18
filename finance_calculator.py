"""
finance_calculator.py

A simple finance calculator that estimates:
- Monthly compensation cost
- Bonus allocation
- Tax withholding
- Total annual cost
- Cost breakdown percentages

This script is intentionally similar in structure to hr_payroll_calculator.py
for duplicate-detection demo purposes.
"""

from dataclasses import dataclass, asdict


@dataclass
class FinanceInputs:
    employee_name: str
    base_salary: float
    bonus_rate: float          # e.g. 0.10 for 10%
    tax_rate: float            # e.g. 0.25 for 25%
    benefits_cost: float       # monthly benefits cost
    months: int = 12


def validate_non_negative(value: float, field_name: str) -> None:
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def calculate_bonus(base_salary: float, bonus_rate: float) -> float:
    return base_salary * bonus_rate


def calculate_tax(gross_amount: float, tax_rate: float) -> float:
    return gross_amount * tax_rate


def calculate_monthly_total(base_salary: float, benefits_cost: float) -> float:
    return base_salary + benefits_cost


def calculate_annual_cost(monthly_total: float, annual_bonus: float, months: int) -> float:
    return (monthly_total * months) + annual_bonus


def calculate_net_after_tax(base_salary: float, annual_bonus: float, tax_amount: float, months: int) -> float:
    return (base_salary * months) + annual_bonus - tax_amount


def calculate_cost_breakdown(base_salary: float, annual_bonus: float, benefits_total: float, annual_total: float) -> dict:
    if annual_total == 0:
        return {"salary_pct": 0.0, "bonus_pct": 0.0, "benefits_pct": 0.0}

    return {
        "salary_pct": round((base_salary * 12 / annual_total) * 100, 2),
        "bonus_pct": round((annual_bonus / annual_total) * 100, 2),
        "benefits_pct": round((benefits_total / annual_total) * 100, 2),
    }


def run_finance_calculator(inputs: FinanceInputs) -> dict:
    validate_non_negative(inputs.base_salary, "base_salary")
    validate_non_negative(inputs.bonus_rate, "bonus_rate")
    validate_non_negative(inputs.tax_rate, "tax_rate")
    validate_non_negative(inputs.benefits_cost, "benefits_cost")

    annual_bonus = calculate_bonus(inputs.base_salary * inputs.months, inputs.bonus_rate)
    gross_taxable = (inputs.base_salary * inputs.months) + annual_bonus
    tax_amount = calculate_tax(gross_taxable, inputs.tax_rate)
    monthly_total = calculate_monthly_total(inputs.base_salary, inputs.benefits_cost)
    annual_total = calculate_annual_cost(monthly_total, annual_bonus, inputs.months)
    net_after_tax = calculate_net_after_tax(inputs.base_salary, annual_bonus, tax_amount, inputs.months)
    breakdown = calculate_cost_breakdown(
        inputs.base_salary,
        annual_bonus,
        inputs.benefits_cost * inputs.months,
        annual_total,
    )

    return {
        "employee_name": inputs.employee_name,
        "monthly_total_cost": round(monthly_total, 2),
        "annual_bonus": round(annual_bonus, 2),
        "tax_amount": round(tax_amount, 2),
        "annual_total_cost": round(annual_total, 2),
        "net_after_tax": round(net_after_tax, 2),
        "cost_breakdown": breakdown,
    }


if __name__ == "__main__":
    sample = FinanceInputs(
        employee_name="Alex Morgan",
        base_salary=4200.00,
        bonus_rate=0.08,
        tax_rate=0.23,
        benefits_cost=550.00,
    )

    result = run_finance_calculator(sample)

    print("FINANCE CALCULATOR OUTPUT")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
