from collections import Counter


def generate_validation_report(valid_games, rejected_games):

    total = len(valid_games) + len(rejected_games)

    # Calculate acceptance and rejection rates
    acceptance_rate = (
        round(len(valid_games) / total * 100, 2)
        if total > 0 else 0
    )

    rejection_rate = (
        round(len(rejected_games) / total * 100, 2)
        if total > 0 else 0
    )

    # Count rejected records by platform
    errors_by_platform = Counter(
        record.get("platform", "Unknown")
        for record in rejected_games
    )

    # Count individual validation errors
    error_types = Counter(
        error
        for record in rejected_games
        for error in record["errors"]
    )

    return {
        "total_records": total,
        "valid_records": len(valid_games),
        "rejected_records": len(rejected_games),
        "acceptance_rate": acceptance_rate,
        "rejection_rate": rejection_rate,
        "rejections_by_platform": dict(errors_by_platform),
        "error_types": dict(error_types)
    }
