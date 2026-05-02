# Author: Vassey Konneh and Leocalis Quezada
# Date: 04/10/2026
# Description: Tkinter graphical user interface for ASPOS.

import tkinter as tk
from tkinter import messagebox, scrolledtext

import matplotlib.pyplot as plt
from Analytics import Analytics


class ASPOSGUI:
    """Main GUI for the Adaptive Study and Performance Optimization System."""

    def __init__(self, root, file_name):
        """Create the GUI and load analytics data."""
        self.root = root
        self.root.title("ASPOS - Adaptive Study and Performance Optimization System")
        self.root.geometry("1100x780")
        self.root.configure(bg="#f4f6f8")

        self.bg_color = "#f4f6f8"
        self.panel_color = "#ffffff"
        self.title_color = "#1f2937"
        self.text_color = "#374151"

        try:
            self.analytics = Analytics(file_name)
        except Exception as error:
            messagebox.showerror("Load Error", str(error))


        title_label = tk.Label(
            self.root,
            text="ASPOS - Adaptive Study and Performance Optimization System",
            font=("Arial", 20, "bold"),
            fg=self.title_color,
            bg=self.bg_color
        )
        title_label.pack(pady=(14, 6))

        description_label = tk.Label(
            self.root,
            text=(
                "Use the controls below to explore student study habits, performance trends, "
                "attendance, and risk indicators from the CSV dataset."
            ),
            wraplength=940,
            justify="center",
            font=("Arial", 11),
            fg=self.text_color,
            bg=self.bg_color
        )
        description_label.pack(pady=(0, 12))

        main_panel = tk.Frame(
            self.root,
            bg=self.panel_color,
            relief="raised",
            bd=2
        )
        main_panel.pack(padx=24, pady=10, fill="both", expand=True)

        input_frame = tk.Frame(main_panel, bg=self.panel_color)
        input_frame.pack(pady=(18, 10))

        tk.Label(
            input_frame,
            text="Week:",
            font=("Arial", 11),
            fg=self.text_color,
            bg=self.panel_color
        ).grid(row=0, column=0, padx=6, pady=5)

        self.week_entry = tk.Entry(
            input_frame,
            width=14,
            font=("Arial", 11),
            justify="center",
            relief="solid",
            bd=1
        )
        self.week_entry.grid(row=0, column=1, padx=6, pady=5)

        tk.Label(
            input_frame,
            text="Student ID:",
            font=("Arial", 11),
            fg=self.text_color,
            bg=self.panel_color
        ).grid(row=0, column=2, padx=12, pady=5)

        self.student_id_entry = tk.Entry(
            input_frame,
            width=14,
            font=("Arial", 11),
            justify="center",
            relief="solid",
            bd=1
        )
        self.student_id_entry.grid(row=0, column=3, padx=6, pady=5)

        section_label = tk.Label(
            main_panel,
            text="Analytics & Controls",
            font=("Arial", 13, "bold"),
            fg="#1f2937",
            bg=self.panel_color
        )
        section_label.pack(anchor="w", padx=20, pady=(10, 5))

        button_frame = tk.Frame(main_panel, bg=self.panel_color)
        button_frame.pack(pady=10)

        self.styleButton(button_frame, "View Dataset", self.viewDataset).grid(row=0, column=0, padx=10, pady=6)
        self.styleButton(button_frame, "Average Performance", self.showAveragePerformance).grid(row=0, column=1, padx=10, pady=6)
        self.styleButton(button_frame, "Average Study Hours", self.showAverageStudyHours).grid(row=0, column=2, padx=10, pady=6)

        self.styleButton(button_frame, "Weekly Trends", self.showWeeklyTrends).grid(row=1, column=0, padx=10, pady=6)
        self.styleButton(button_frame, "At-Risk Students", self.showAtRiskStudents).grid(row=1, column=1, padx=10, pady=6)
        self.styleButton(button_frame, "Top Performers", self.showTopPerformers).grid(row=1, column=2, padx=10, pady=6)

        self.styleButton(button_frame, "Filter By Week", self.filterByWeek).grid(row=2, column=0, padx=10, pady=6)
        self.styleButton(button_frame, "Filter By Student ID", self.filterByStudentID).grid(row=2, column=1, padx=10, pady=6)
        self.styleButton(button_frame, "Summary Statistics", self.showSummaryStatistics).grid(row=2, column=2, padx=10, pady=6)

        self.styleButton(button_frame, "Clear Output", self.clearOutput).grid(row=3, column=0, padx=10, pady=6)
        self.styleButton(button_frame, "Exit Program", self.root.destroy).grid(row=3, column=1, padx=10, pady=6)
        self.styleButton(button_frame, "Risk Summary", self.showRiskSummary, primary=True).grid(row=3, column=2,
        padx=10, pady=6)

        self.styleButton(button_frame, "Risk Factor Comparison", self.showTopRiskFactors, primary=True).grid(row=4,
        column=1, padx=10, pady=(8, 6))


        chart_label = tk.Label(
            main_panel,
            text="Visualizations",
            font=("Arial", 13, "bold"),
            fg="#1f2937",
            bg=self.panel_color
        )
        chart_label.pack(anchor="w", padx=20, pady=(10, 5))

        chart_frame = tk.Frame(main_panel, bg=self.panel_color)
        chart_frame.pack(pady=(8, 12))

        self.styleButton(chart_frame, "Performance Chart", self.show_performance_chart).grid(row=0, column=0, padx=10, pady=6)
        self.styleButton(chart_frame, "Study vs Performance", self.show_study_vs_performance).grid(row=0, column=1, padx=10, pady=6)
        self.styleButton(chart_frame, "Attendance vs Performance", self.show_attendance_vs_performance).grid(row=0, column=2, padx=10, pady=6)
        self.styleButton(chart_frame, "Performance Trend", self.show_performance_trend).grid(row=1, column=1, padx=10, pady=6)

        output_label = tk.Label(
            main_panel,
            text="Output",
            font=("Arial", 12, "bold"),
            fg="#1f2937",
            bg=self.panel_color
        )
        output_label.pack(anchor="w", padx=20, pady=(8, 2))

        output_frame = tk.Frame(main_panel, bg=self.panel_color, relief="solid", bd=1)
        output_frame.pack(padx=22, pady=(0, 22), fill="both", expand=True)

        self.output_area = scrolledtext.ScrolledText(
            output_frame,
            width=120,
            height=16,
            font=("Courier New", 11),
            bg="white",
            fg="#111827",
            relief="flat",
            bd=0,
            wrap="none"
        )
        self.output_area.pack(fill="both", expand=True, padx=8, pady=4)

    def styleButton(self, parent, text, command, primary=False):
        return tk.Button(
            parent,
            text=text,
            width=26,
            height=2,
            command=command,
            font=("Arial", 11, "bold"),
            bg="#e5e7eb",
            fg="#111827",
            activebackground="#d1d5db",
            activeforeground="#111827",
            relief="flat",
            bd=0,
            cursor="hand2",
            highlightthickness=0
        )

    def clearOutput(self):
        """Clear the output text area."""
        self.output_area.delete("1.0", tk.END)

    def displayDataFrame(self, dataframe, include_index=False):
        """Display a pandas DataFrame inside the output box."""
        self.clearOutput()
        if dataframe.empty:
            self.output_area.insert(tk.END, "No matching records found.\n")
        else:
            self.output_area.insert(tk.END, dataframe.to_string(index=include_index))
            self.output_area.insert(tk.END, "\n")

    def viewDataset(self):
        """Display the full dataset."""
        self.displayDataFrame(self.analytics.getDataset())

    def showAveragePerformance(self):
        """Display the average performance index."""
        self.clearOutput()
        average_value = self.analytics.getAveragePerformance()
        self.output_area.insert(tk.END, f"Average Performance Index: {average_value:.2f}\n")

    def showAverageStudyHours(self):
        """Display the average study hours."""
        self.clearOutput()
        average_value = self.analytics.getAverageStudyHours()
        self.output_area.insert(tk.END, f"Average Study Hours: {average_value:.2f}\n")

    def showWeeklyTrends(self):
        """Display weekly average trends."""
        self.displayDataFrame(self.analytics.getWeeklyTrends(), include_index=True)

    def showAtRiskStudents(self):
        """Display rows that indicate students may be at risk."""
        self.displayDataFrame(self.analytics.getAtRiskStudents())

    def showTopPerformers(self):
        """Display the highest performing rows."""
        self.displayDataFrame(self.analytics.getTopPerformers())

    def filterByWeek(self):
        """Display rows for the week entered by the user."""
        try:
            week_value = int(self.week_entry.get().strip())
            self.displayDataFrame(self.analytics.filterByWeek(week_value))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid week number.")

    def filterByStudentID(self):
        """Display all rows for the student ID entered by the user."""
        try:
            student_id_value = int(self.student_id_entry.get().strip())
            self.displayDataFrame(self.analytics.filterByStudentID(student_id_value))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid student ID number.")

    def showSummaryStatistics(self):
        """Display descriptive statistics for key variables."""
        self.displayDataFrame(self.analytics.getSummaryStatistics(), include_index=True)

    def showRiskSummary(self):
        """Display record-level and student-level risk summary."""
        self.clearOutput()

        df = self.analytics.getDataset()
        at_risk = self.analytics.getAtRiskStudents()

        total_records = len(df)
        total_students = df["student_id"].nunique()

        risk_counts = at_risk["student_id"].value_counts()
        frequent_risk_students = risk_counts[risk_counts >= 3]
        at_risk_students = len(frequent_risk_students)

        record_percent = (len(at_risk) / total_records) * 100 if total_records > 0 else 0
        student_percent = (at_risk_students / total_students) * 100 if total_students > 0 else 0

        self.output_area.insert(
            tk.END,
            f"At-Risk Records: {len(at_risk)}\n"
            f"Total Records: {total_records}\n"
            f"Record Risk Percentage: {record_percent:.2f}%\n\n"
            f"Consistently At-Risk Students (3+ weeks): {at_risk_students}\n"
            f"Total Unique Students: {total_students}\n"
            f"Student Risk Percentage: {student_percent:.2f}%\n"
        )

        self.output_area.insert(
            tk.END,
            "\nInsight: Nearly half of the students show repeated risk patterns, indicating a need for sustained academic support.\n"
        )

    def showTopRiskFactors(self):
        """Compare factor averages between all records and at-risk records."""
        self.clearOutput()

        df = self.analytics.getDataset().copy()
        at_risk = self.analytics.getAtRiskStudents().copy()

        if at_risk.empty:
            self.output_area.insert(tk.END, "No at-risk records were found.\n")
            return

        factors = [
            "study_hours",
            "sleep_hours",
            "stress_level",
            "attendance_rate",
            "screen_time_hours",
            "caffeine_intake",
            "learning_efficiency",
            "fatigue_index"
        ]

        results = []

        for factor in factors:
            overall_avg = df[factor].mean()
            at_risk_avg = at_risk[factor].mean()
            difference = at_risk_avg - overall_avg
            results.append((factor, overall_avg, at_risk_avg, difference, abs(difference)))

        results.sort(key=lambda item: item[4], reverse=True)

        self.output_area.insert(tk.END, "Risk Factor Comparison\n")
        self.output_area.insert(tk.END, "-" * 60 + "\n")

        for factor, overall_avg, at_risk_avg, difference, _ in results:
            self.output_area.insert(tk.END, f"{factor}\n")
            self.output_area.insert(tk.END, f"  Overall Average: {overall_avg:.2f}\n")
            self.output_area.insert(tk.END, f"  At-Risk Average: {at_risk_avg:.2f}\n")
            self.output_area.insert(tk.END, f"  Difference: {difference:.2f}\n\n")

        top_factor = results[0][0]

        self.output_area.insert(
            tk.END,
            f"\nInsight: {top_factor} shows the strongest separation between at-risk and overall records, making it the most influential indicator in the current rule-based model.\n"
        )

    def show_performance_chart(self):
        """Display average performance by week as a line chart."""
        self.clearOutput()

        try:
            data = self.analytics.getWeeklyTrends()

            if data.empty:
                messagebox.showinfo("No Data", "No weekly trend data is available.")
                return

            if "performance_index" not in data.columns:
                messagebox.showerror(
                    "Chart Error",
                    "The weekly trends data does not contain a 'performance_index' column."
                )
                return

            x_values = data.index
            if "week" in data.columns:
                x_values = data["week"]

            plt.figure(figsize=(8, 5))
            plt.plot(x_values, data["performance_index"], marker="o")
            plt.title("Average Performance by Week")
            plt.xlabel("Week")
            plt.ylabel("Performance Index")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except Exception as error:
            messagebox.showerror("Chart Error", f"Could not display performance chart.\n{error}")

    def show_study_vs_performance(self):
        """Display study hours versus performance as a scatter plot."""
        self.clearOutput()

        try:
            df = self.analytics.getDataset()

            required_columns = ["study_hours", "performance_index"]
            for column in required_columns:
                if column not in df.columns:
                    messagebox.showerror(
                        "Chart Error",
                        f"The dataset does not contain the required column: '{column}'."
                    )
                    return

            plt.figure(figsize=(8, 5))
            # plot relationship between study hours and performance
            plt.scatter(df["study_hours"], df["performance_index"])
            plt.title("Study Hours vs Performance")
            plt.xlabel("Study Hours")
            plt.ylabel("Performance Index")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except Exception as error:
            messagebox.showerror("Chart Error", f"Could not display study vs performance chart.\n{error}")

    def show_attendance_vs_performance(self):
        """Display attendance rate versus performance as a scatter plot."""
        self.clearOutput()

        try:
            df = self.analytics.getDataset()

            required_columns = ["attendance_rate", "performance_index"]
            for column in required_columns:
                if column not in df.columns:
                    messagebox.showerror(
                        "Chart Error",
                        f"The dataset does not contain the required column: '{column}'."
                    )
                    return

            plt.figure(figsize=(8, 5))
            # plot relationship between attendance and performance
            plt.scatter(df["attendance_rate"], df["performance_index"])
            plt.title("Attendance Rate vs Performance")
            plt.xlabel("Attendance Rate")
            plt.ylabel("Performance Index")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        except Exception as error:
            messagebox.showerror("Chart Error", f"Could not display attendance vs performance chart.\n{error}")

    def show_performance_trend(self):
        """Display average performance by week."""
        self.clearOutput()

        try:
            df = self.analytics.getDataset()

            grouped = df.groupby("week")["performance_index"].mean()

            plt.figure(figsize=(8, 5))
            # plot average performance over time
            grouped.plot(marker='o', linewidth=2)
            plt.title("Average Performance by Week")
            plt.xlabel("Week")
            plt.ylabel("Performance Index")
            plt.grid(True)
            plt.tight_layout()
            plt.show()


        except Exception as error:
            messagebox.showerror("Chart Error", str(error))

