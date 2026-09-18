
import csv
import random
from pathlib import Path

random.seed(42)

# Number of training samples
NUM_SAMPLES = 200

# Output file
OUTPUT_FILE = Path(__file__).parent / "ppa_dataset.csv"

# RTL feature names
FEATURES = [
    "modules",
    "inputs",
    "outputs",
    "registers",
    "always_blocks",
    "case_statements",
    "adders",
    "subtractors",
    "and_operations",
    "or_operations",
]

# CSV column names
COLUMNS = FEATURES + [
    "estimated_area",
    "estimated_power",
    "estimated_performance",
]


def generate_sample():
    """Generate one synthetic RTL design sample."""

    modules = random.randint(1, 5)
    inputs = random.randint(1, 32)
    outputs = random.randint(1, 16)
    registers = random.randint(0, 32)
    always_blocks = random.randint(1, 8)
    case_statements = random.randint(0, 5)
    adders = random.randint(0, 8)
    subtractors = random.randint(0, 8)
    and_operations = random.randint(0, 15)
    or_operations = random.randint(0, 15)

    # Baseline area formula
    area = (
        modules * 10
        + inputs * 2
        + outputs * 2
        + registers * 5
        + always_blocks * 8
        + case_statements * 4
        + adders * 12
        + subtractors * 12
        + and_operations * 3
        + or_operations * 3
    )

    # Baseline power formula
    power = (
        inputs * 0.5
        + outputs * 0.5
        + registers * 1.5
        + adders * 2
        + subtractors * 2
        + and_operations * 0.5
        + or_operations * 0.5
    )

    # Baseline performance formula
    performance = (
        100
        - registers * 2
        - always_blocks * 3
        - case_statements * 2
        - adders * 4
        - subtractors * 4
    )

    performance = max(performance, 1)

    return {
        "modules": modules,
        "inputs": inputs,
        "outputs": outputs,
        "registers": registers,
        "always_blocks": always_blocks,
        "case_statements": case_statements,
        "adders": adders,
        "subtractors": subtractors,
        "and_operations": and_operations,
        "or_operations": or_operations,
        "estimated_area": round(area, 2),
        "estimated_power": round(power, 2),
        "estimated_performance": round(performance, 2),
    }


def main():
    rows = [generate_sample() for _ in range(NUM_SAMPLES)]

    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Dataset created successfully!")
    print(f"Samples: {NUM_SAMPLES}")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()