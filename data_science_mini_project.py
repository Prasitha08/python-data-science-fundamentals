"""
Mini Project: Student Performance Analysis
Run: python data_science_mini_project.py
The included CSV contains fictional learning data.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("student_scores.csv")

def main():
    # Load the CSV dataset
    data = pd.read_csv(DATA_FILE)

    print("STUDENT PERFORMANCE DATA")
    print("-" * 35)
    print(data.head())
    print("\nDataset shape:", data.shape)
    print("\nColumn information:")
    print(data.info())

    # Calculate each student's average score
    subjects = ["python", "statistics", "data_science"]
    data["average_score"] = data[subjects].mean(axis=1).round(2)
    data["result"] = data["average_score"].apply(
        lambda score: "Pass" if score >= 50 else "Needs Improvement"
    )

    print("\nStudent averages and results:")
    print(data[["name", "average_score", "result"]].to_string(index=False))

    # Summary statistics
    print("\nSummary statistics:")
    print(data[subjects].describe().round(2))

    # Average score by subject
    subject_averages = data[subjects].mean().sort_values(ascending=False)
    print("\nAverage score by subject:")
    print(subject_averages.round(2))

    # Pass and needs-improvement counts
    print("\nResult counts:")
    print(data["result"].value_counts())

    # Save the processed dataset
    output_file = DATA_FILE.with_name("student_performance_summary.csv")
    data.to_csv(output_file, index=False)
    print(f"\nSaved processed data to: {output_file.name}")

    # Visualise subject averages
    plt.figure(figsize=(8, 5))
    subject_averages.plot(kind="bar")
    plt.title("Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average Score")
    plt.ylim(0, 100)
    plt.xticks(rotation=0)
    plt.tight_layout()

    chart_file = DATA_FILE.with_name("subject_average_chart.png")
    plt.savefig(chart_file, dpi=150)
    print(f"Saved chart to: {chart_file.name}")
    plt.show()

    print("\nConclusion:")
    print(
        "In this sample dataset, the subject with the highest average score is "
        f"{subject_averages.index[0]}. These are descriptive findings from "
        "fictional data, not conclusions about real students."
    )

if __name__ == "__main__":
    main()
