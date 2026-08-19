#Foreign currency invoice

raw_invoice_eur = "8450.00"    # as text from the supplier's system
eur_to_gbp      = 0.853        # agreed conversion rate
fx_fee_rate     = 0.02         # charged on the converted GBP amount

invoice_eur = float(raw_invoice_eur)
converted_gbp = invoice_eur * eur_to_gbp
fx_fee = converted_gbp * fx_fee_rate
total_gbp = converted_gbp + fx_fee
effective_rate = total_gbp/invoice_eur

print(f"Invoice (EUR):   €{invoice_eur:,.2f}")
print(f"Converted (GBP): £{converted_gbp:,.2f}")
print(f"FX fee:          £{fx_fee:,.2f}")
print(f"Total (GBP):     £{total_gbp:,.2f}")
print(f"Effective rate:  {effective_rate:.4f}")
