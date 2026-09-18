
def generate_optimization_recommendations(features):
    """
    Generate RTL optimization recommendations
    based on extracted structural features.
    """

    recommendations = []

    # Register optimization
    if features.get("registers", 0) > 5:
        recommendations.append({
            "area": "Registers",
            "issue": "High register count",
            "recommendation": (
                "Review register usage and remove "
                "unnecessary registers where possible."
            )
        })

    # Arithmetic optimization
    if (
        features.get("adders", 0)
        + features.get("subtractors", 0)
    ) > 3:
        recommendations.append({
            "area": "Arithmetic Logic",
            "issue": "High arithmetic operation count",
            "recommendation": (
                "Review arithmetic operations and "
                "consider resource sharing."
            )
        })

    # Control logic optimization
    if features.get("case_statements", 0) > 2:
        recommendations.append({
            "area": "Control Logic",
            "issue": "Multiple case statements",
            "recommendation": (
                "Review case statements and simplify "
                "control logic where possible."
            )
        })

    # Sequential logic optimization
    if features.get("always_blocks", 0) > 2:
        recommendations.append({
            "area": "Sequential Logic",
            "issue": "Multiple always blocks",
            "recommendation": (
                "Review sequential logic and "
                "simplify the RTL structure."
            )
        })

    # Logic operation optimization
    if (
        features.get("and_operations", 0)
        + features.get("or_operations", 0)
    ) > 5:
        recommendations.append({
            "area": "Logic Operations",
            "issue": "High logic operation count",
            "recommendation": (
                "Review Boolean expressions and "
                "look for redundant logic."
            )
        })

    # Default recommendation
    if not recommendations:
        recommendations.append({
            "area": "General",
            "issue": "No major structural hotspots detected",
            "recommendation": (
                "RTL structure appears relatively simple. "
                "Verify PPA using synthesis."
            )
        })

    return recommendations