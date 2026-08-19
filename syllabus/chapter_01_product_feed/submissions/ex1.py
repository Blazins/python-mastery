raw_unit_cost      = "12.75"   # GBP ex-VAT, as text from the feed
raw_units          = "340"     # as text from the feed
bulk_discount_rate = 0.08      # applied to wholesale cost first
markup_rate        = 0.45      # applied after the discount
vat_rate           = 0.20      # applied last

wholesale_cost = float(raw_unit_cost) #converting the string to float values
effective_unit_cost = wholesale_cost - (wholesale_cost * bulk_discount_rate) #wholesale cost after the bulk discount
retail_ex_vat = effective_unit_cost * (1 + markup_rate) #effective unit cost plus markup.
retail_inc_vat = retail_ex_vat * (1 + vat_rate) #retail ex VAT plus VAT
order_cost = effective_unit_cost * int(raw_units) #what we pay: effective unit cost × units.
projected_revenue = retail_inc_vat * int(raw_units)#what customers pay: retail inc VAT × units

print(f"Effective unit cost: £{effective_unit_cost:<10,.2f}")
print(f"Retail ex VAT:       £{retail_ex_vat:,.2f}")
print(f"Retail inc VAT:      £{retail_inc_vat:,.2f}")
print(f"Order cost:          £{order_cost :,.2f}")
print(f"Projected revenue:   £{projected_revenue:>,.2f}")
