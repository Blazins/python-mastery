#Pallet planning

raw_units          = "2437"    # as text from the feed
raw_unit_weight_g  = "462"     # grams per unit, as text from the feed
units_per_carton   = 12
cartons_per_pallet = 40

full_cartons = int(raw_units)//units_per_carton
loose_units = int(raw_units)%units_per_carton
full_pallets = full_cartons//cartons_per_pallet #pallets are counted from the full cartons only
loose_cartons = full_cartons%cartons_per_pallet
total_weight = (int(raw_unit_weight_g) * int(raw_units))/1000 #otal weight covers every unit in the order

print(f"Full cartons:{full_cartons:>5}")
print(f"Loose units:{loose_units:>4}")
print(f"Full pallets:{full_pallets:>3}")
print(f"Loose cartons:{loose_cartons:>2}")
print(f"Total weight:{total_weight:>10,.2f} kg")
