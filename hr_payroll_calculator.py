import matplotlib.pyplot as plt

def plot_annual_payroll_pie_chart(net_annual_pay: float, tax_amount: float, employer_contribution: float) -> None:
    """
    Plots a pie chart showing the breakdown of the Total Annual Payroll Cost.
    """
    labels = ['Net Annual Pay', 'Taxes (Annual)', 'Employer Contribution (Annual)']
    sizes = [net_annual_pay, tax_amount, employer_contribution]
    colors = ['#4CAF50', '#FF9800', '#2196F3']
    explode = (0.05, 0, 0)  # Slightly separate the net pay slice for emphasis

    plt.figure(figsize=(8, 6))
    plt.pie(
        sizes, 
        explode=explode, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%', 
        shadow=True, 
        startangle=140
    )
    plt.title("Total Annual Payroll Cost Breakdown")
    plt.axis('equal')  # Ensures that the pie is drawn as a perfect circle.
    plt.tight_layout()
    plt.show()
