import re
import sys

#!/usr/bin/env python3
# app2.py
# Simple Austria net salary estimator: input gross monthly pay, computes net monthly and yearly (x14).
# Note: This is an approximation (uses a flat employee social security rate and 2023-ish progressive tax brackets).
# Use for estimates only.
# This app has been "vibe-coded" with AI

SOCIAL_RATE = 0.1812  # approximate employee social security contribution (18.12%)
# By default handle special payments (13th/14th) with a reduced flat tax rate.
SPECIAL_PAYMENT_TAX_RATE = 0.06  # 6% flat tax on special payments (configurable)
# Austrian progressive income tax brackets (annual taxable income) - marginal rates
BRACKETS = [
    (11000, 0.00),
    (18000, 0.20),
    (31000, 0.35),
    (60000, 0.42),
    (90000, 0.48),
    (1_000_000, 0.50),
    (float("inf"), 0.55),
]

def parse_amount(s: str) -> float:
    s = s.strip()
    s = s.replace(".", "")           # remove thousand separators like "3.000"
    s = s.replace(",", ".")          # allow commas as decimal separators
    s = re.sub(r"[^\d\.\-]", "", s)  # remove any non-numeric except dot/minus
    if not s:
        raise ValueError("No numeric input found")
    return float(s)

def progressive_tax(taxable: float) -> float:
    tax = 0.0
    lower = 0.0
    for upper, rate in BRACKETS:
        if taxable <= lower:
            break
        taxed_amount = min(taxable, upper) - lower
        if taxed_amount > 0:
            tax += taxed_amount * rate
        lower = upper
    return tax

def format_eur(x: float) -> str:
    return f"€{x:,.2f}"

def main():
    try:
        raw = input("Paste gross monthly income (e.g. 3000 or 3.000,00 €): ")
        gross_monthly = parse_amount(raw)
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)

    gross_annual = gross_monthly * 14
    # split into regular (12x) and special (2x)
    gross_regular = gross_monthly * 12
    gross_special = gross_monthly * 2

    # social contributions typically apply to the whole gross; keep that behavior
    social_annual = gross_annual * SOCIAL_RATE

    # Taxable amounts: assume social contributions reduce taxable base proportionally
    taxable_regular = max(0.0, gross_regular - (social_annual * (gross_regular / gross_annual)))
    taxable_special = max(0.0, gross_special - (social_annual * (gross_special / gross_annual)))

    # Progressive tax applies to regular income, special payments taxed at flat rate
    income_tax_regular = progressive_tax(taxable_regular)
    income_tax_special = taxable_special * SPECIAL_PAYMENT_TAX_RATE
    income_tax = income_tax_regular + income_tax_special

    net_annual = gross_annual - social_annual - income_tax
    net_monthly_14 = net_annual / 14

    print()
    print("Gross monthly:        ", format_eur(gross_monthly))
    print("Gross annual (x14):   ", format_eur(gross_annual))
    print()
    print("Net monthly (per paid month, x14):", format_eur(net_monthly_14))
    print("Net annual (x14):                ", format_eur(net_annual))
    print()
    print("Note: This is an approximation. Social security rates, allowances and exact tax rules may vary.")
    print("Special payments are taxed at a flat rate of", f"{SPECIAL_PAYMENT_TAX_RATE*100:.1f}% by default.")
    print("Change SPECIAL_PAYMENT_TAX_RATE in the script to adjust.")

if __name__ == "__main__":
    main()