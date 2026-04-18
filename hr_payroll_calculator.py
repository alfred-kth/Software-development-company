"""
hr_payroll_calculator.py

A simple HR payroll calculator that estimates:
- Gross monthly pay
- Employer contribution amount
- Tax deduction
- Net annual pay
- Annual payroll cost

This script is intentionally similar in structure to finance_calculator.py
for duplicate-detection demo purposes.

Includes a graph to represent payroll component values.
"""

from dataclasses import dataclass
import matplotlib.pyplot as plt


@dataclass
class PayrollInputs:
    employee_name: str
    monthly_salary: float
    employer_contribution_rate: float   # e.g. 0.12 for 12%
    tax_rate: float                     # e.g. 0.25 for 25%
    fixed_allowance: float              # monthly allowance
    months: int = 12


def validate_non_negative(value: float, field_name: str) -> None:
    if value < 0:
        raise ValueError(f"{field_name} cannot be negative.")


def calculate_employer_contribution(monthly_salary: float, employer_contribution_rate: float, months: int) -> float:
    return (monthly_salary * months) * employer_contribution_rate


def calculate_tax(gross_amount: float, tax_rate: float) -> float:
    return gross_amount * tax_rate


def calculate_gross_monthly_pay(monthly_salary: float, fixed_allowance: float) -> float:
    return monthly_salary + fixed_allowance


def calculate_annual_payroll_cost(gross_monthly_pay: float, employer_contribution: float, months: int) -> float:
    return (gross_monthly_pay * months) + employer_contribution


def calculate_net_annual_pay(monthly_salary: float, fixed_allowance: float, tax_amount: float, months: int) -> float:
    return ((monthly_salary + fixed_allowance) * months) - tax_amount


def plot_payroll_breakdown(monthly_salary: float, fixed_allowance: float, employer_contribution: float, tax_amount: float) -> None:
    labels = ["Salary (Monthly)", "Allowance (Monthly)", "Employer Contribution (Annual)", "Tax (Annual)"]
    values = [monthly_salary, fixed_allowance, employer_contribution, tax_amount]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Payroll Component Breakdown")
    plt.ylabel("Amount")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.show()


def run_payroll_calculator(inputs: PayrollInputs, show_graph: bool = True) -> dict:
    validate_non_negative(inputs.monthly_salary, "monthly_salary")
    validate_non_negative(inputs.employer_contribution_rate, "employer_contribution_rate")
    validate_non_negative(inputs.tax_rate, "tax_rate")
    validate_non_negative(inputs.fixed_allowance, "fixed_allowance")

    gross_monthly_pay = calculate_gross_monthly_pay(inputs.monthly_salary, inputs.fixed_allowance)
    employer_contribution = calculate_employer_contribution(
        inputs.monthly_salary,
        inputs.employer_contribution_rate,
        inputs.months,
    )
    gross_taxable = gross_monthly_pay * inputs.months
    tax_amount = calculate_tax(gross_taxable, inputs.tax_rate)
    annual_payroll_cost = calculate_annual_payroll_cost(
        gross_monthly_pay,
        employer_contribution,
        inputs.months,
    )
    net_annual_pay = calculate_net_annual_pay(
        inputs.monthly_salary,
        inputs.fixed_allowance,
        tax_amount,
        inputs.months,
    )

    if show_graph:
        plot_payroll_breakdown(
            inputs.monthly_salary,
            inputs.fixed_allowance,
            employer_contribution,
            tax_amount,
        )

    return {
        "employee_name": inputs.employee_name,
        "gross_monthly_pay": round(gross_monthly_pay, 2),
        "employer_contribution": round(employer_contribution, 2),
        "tax_amount": round(tax_amount, 2),
        "annual_payroll_cost": round(annual_payroll_cost, 2),
        "net_annual_pay": round(net_annual_pay, 2),
    }


if __name__ == "__main__":
    sample = PayrollInputs(
        employee_name="Alex Morgan",
        monthly_salary=4200.00,
        employer_contribution_rate=0.12,
        tax_rate=0.23,
        fixed_allowance=550.00,
    )

    result = run_payroll_calculator(sample, show_graph=False)

    print("HR PAYROLL CALCULATOR OUTPUT")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
