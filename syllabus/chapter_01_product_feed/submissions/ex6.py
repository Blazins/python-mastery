#Exercise 6 - End-of-day till reconciliation

raw_till_total = "1026.86"   # pounds and pence, as text from the till

#Denominations available, in pennies: 5000 (£50), 2000 (£20), 1000 (£10), 500 (£5), 100 (£1), 50, 20, 10, 5, 2, 1.

total_pounds = float(raw_till_total)
total_pennies = total_pounds * 100
pennies = int(round(total_pennies,0))


rest = pennies

pound_50_denominations = rest//5000
rest = rest % 5000

pound_20_denominations = rest//2000
rest = rest % 2000

pound_10_denominations = rest//1000
rest = rest % 1000

pound_5_denominations = rest//500
rest = rest % 500

pound_1_denominations = rest//100
rest = rest % 100

denominations_50_p = rest//50
rest = rest % 50

denominations_20_p = rest//20
rest = rest % 20

denominations_10_p = rest//10
rest = rest % 10

denominations_5_p = rest//5
rest = rest % 5

denominations_2_p = rest//2
rest = rest % 2

denominations_1_p = rest  

print(f"Till total: £{total_pounds:,.2f}")
print(f"Pennies:    {pennies}")
print(f"{'£50':<4} x {pound_50_denominations}")
print(f"{'£20':<4} x {pound_20_denominations}")
print(f"{'£10':<4} x {pound_10_denominations}")
print(f"{'£5':<4} x {pound_5_denominations}")
print(f"{'£1':<4} x {pound_1_denominations}")
print(f"{'50p':<4} x {denominations_50_p}")
print(f"{'20p':<4} x {denominations_20_p}")
print(f"{'10p':<4} x {denominations_10_p}")
print(f"{'5p':<4} x {denominations_5_p}")
print(f"{'2p':<4} x {denominations_2_p}")
print(f"{'1p':<4} x {denominations_1_p}")


