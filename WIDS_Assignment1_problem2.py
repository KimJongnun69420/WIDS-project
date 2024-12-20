import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class ExpenseTracker:
    def __init__(self, file="C:\\Users\\vipul\\Downloads\\monthly_expenses.csv"):
        self.file = file
        try:
            self.data = pd.read_csv(self.file)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["Date", "Cat", "Amt", "Desc"])
            self.data.to_csv(self.file, index=False)

    def add_expense(self, date, cat, amt, desc=""):
        new_row = {"Date": date, "Cat": cat, "Amt": amt, "Desc": desc}
        self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)
        self.data.to_csv(self.file, index=False)

    def view_expenses(self):
        print(self.data)

    def get_expenses_by_cat(self):
        return self.data.groupby("Cat")["Amt"].sum()

    def gen_monthly_report(self):
        self.data["Month"] = pd.to_datetime(self.data["Date"]).dt.to_period("M")
        return self.data.groupby("Month")["Amt"].sum()

    def visualize_expenses(self):
        exp_by_cat = self.get_expenses_by_cat()
        exp_by_cat.plot.pie(autopct="%1.1f%%", figsize=(8, 6), title="Expenses by Category")
        plt.ylabel("")
        plt.show()

    def visualize_monthly_trends(self):
        monthly_report = self.gen_monthly_report()
        monthly_report = monthly_report.reset_index()
        monthly_report["Month"] = monthly_report["Month"].astype(str)
        monthly_report.plot(x="Month", y="Amt", kind="line", marker="o", figsize=(10, 6), title="Monthly Spending Trends")
        plt.xlabel("Month")
        plt.ylabel("Total Spending")
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    et = ExpenseTracker()
    et.add_expense("2024-12-01", "Food", 20.5, "Lunch")
    et.add_expense("2024-12-05", "Trans", 15.0, "Bus ticket")
    et.add_expense("2024-12-10", "Ent", 50.0, "Movie ticket")
    print("\nAll Expenses:")
    et.view_expenses()
    print("\nExpenses by Category:")
    print(et.get_expenses_by_cat())
    print("\nMonthly Report:")
    print(et.gen_monthly_report())
    print("\nVisualizing Expenses:")
    et.visualize_expenses()
    print("\nVisualizing Monthly Trends:")
    et.visualize_monthly_trends()
#i have used some chatgpt for some part of it but I have understood what it said 
