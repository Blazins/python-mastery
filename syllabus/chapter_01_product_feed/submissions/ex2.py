#Pallet planning

raw_units          = "2437"    # as text from the feed
raw_unit_weight_g  = "462"     # grams per unit, as text from the feed
units_per_carton   = 12
cartons_per_pallet = 40

units = int(raw_units)
unit_weight_g = int(raw_unit_weight_g)

full_cartons = units//units_per_carton
loose_units = units%units_per_carton
full_pallets = full_cartons//cartons_per_pallet #pallets are counted from the full cartons only
loose_cartons = full_cartons%cartons_per_pallet
total_weight = unit_weight_g * units/1000 #otal weight covers every unit in the order

print(f"{'Full cartons:':<15}{full_cartons}")
print(f"{'Loose units:':<15}{loose_units}")
print(f"{'Full pallets:':<15}{full_pallets}")
print(f"{'Loose cartons:':<15}{loose_cartons}")
print(f"{'Total weight:':<15}{total_weight:,.2f} kg")
