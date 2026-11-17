"""One possible refactoring of the simple tax calculation exercise."""

# Give the shared rate a name instead of repeating it for each amount.
TAX_RATE = 0.20


def calculate_total_with_tax(amount: float, tax_rate: float) -> float:
    """Return an amount after applying tax."""
    return amount + amount * tax_rate


def main() -> None:
    # Process each amount the same way, without duplicating the print call.
    for amount in (100, 200):
        total = calculate_total_with_tax(amount, TAX_RATE)
        print("Total:", total)


if __name__ == "__main__":
    main()
