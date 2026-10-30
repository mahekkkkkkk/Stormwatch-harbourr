
import csv
import matplotlib.pyplot as plt

# Read simulation results
results = []

with open("results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        results.append(row)

# Agent policies
policies = ["baseline", "model", "llm"]
names = ["Baseline", "Model-Based", "Mock LLM"]

average_cargo = []
average_knockouts = []

# Calculate average results
for policy in policies:
    group = [
        row for row in results
        if row["policy"] == policy
    ]

    cargo = sum(
        int(row["delivered"]) for row in group
    ) / len(group)

    knockouts = sum(
        int(row["knockouts"]) for row in group
    ) / len(group)

    average_cargo.append(cargo)
    average_knockouts.append(knockouts)


# CHART 1: Average Cargo Delivered
plt.figure(figsize=(8, 5))

bars = plt.bar(
    names,
    average_cargo,
    color=["#e76f51", "#2a9d8f", "#457b9d"]
)

plt.title("Average Cargo Delivered by Agent Policy")
plt.xlabel("Agent Policy")
plt.ylabel("Average Cargo Units")
plt.ylim(0, max(average_cargo) * 1.15)

for bar, value in zip(bars, average_cargo):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 2,
        f"{value:.2f}",
        ha="center"
    )

plt.tight_layout()
plt.savefig("cargo_chart.png", dpi=300)
plt.close()


# CHART 2: Average Storm Knockouts
plt.figure(figsize=(8, 5))

bars = plt.bar(
    names,
    average_knockouts,
    color=["#e76f51", "#2a9d8f", "#457b9d"]
)

plt.title("Average Storm Knockouts by Agent Policy")
plt.xlabel("Agent Policy")
plt.ylabel("Average Knockouts")
plt.ylim(0, max(average_knockouts) + 3)

for bar, value in zip(bars, average_knockouts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.2,
        f"{value:.2f}",
        ha="center"
    )

plt.tight_layout()
plt.savefig("knockouts_chart.png", dpi=300)
plt.close()

print("Both charts generated successfully!")
print("1. cargo_chart.png")
print("2. knockouts_chart.png")
