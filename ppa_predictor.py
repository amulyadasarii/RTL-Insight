
def predict_ppa(features):
    """
    Baseline PPA estimation using RTL features.

    These are illustrative estimates, not
    actual synthesis measurements.
    """

    modules = features.get("modules", 0)
    inputs = features.get("inputs", 0)
    outputs = features.get("outputs", 0)
    registers = features.get("registers", 0)
    always_blocks = features.get("always_blocks", 0)
    case_statements = features.get("case_statements", 0)
    adders = features.get("adders", 0)
    subtractors = features.get("subtractors", 0)
    and_operations = features.get("and_operations", 0)
    or_operations = features.get("or_operations", 0)

    # Illustrative baseline formulas
    estimated_area = (
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

    estimated_power = (
        inputs * 0.5
        + outputs * 0.5
        + registers * 1.5
        + adders * 2
        + subtractors * 2
        + and_operations * 0.5
        + or_operations * 0.5
    )

    estimated_performance = (
        100
        - registers * 2
        - always_blocks * 3
        - case_statements * 2
        - adders * 4
        - subtractors * 4
    )

    estimated_performance = max(
        estimated_performance, 1
    )

    return {
        "estimated_area": round(estimated_area, 2),
        "estimated_power": round(estimated_power, 2),
        "estimated_performance": round(
            estimated_performance, 2
        )
    }