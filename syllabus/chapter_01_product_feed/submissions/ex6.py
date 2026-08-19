#Exercise 6 - End-of-day till reconciliation

raw_till_total = "1026.86"   # pounds and pence, as text from the till

#Denominations available, in pennies: 5000 (£50), 2000 (£20), 1000 (£10), 500 (£5), 100 (£1), 50, 20, 10, 5, 2, 1.

total_pounds = float(raw_till_total)
total_pennies = total_pounds * 100
pennies = int(round(total_pennies,0))

denomination_label_50 = "£50"
denomination_label_20 = "£20"
denomination_label_10 = "£10"
denomination_label_5 = "£5"
denomination_label_1 = "£1"
denomination_label_50p = "50p"
denomination_label_20p = "20p"
denomination_label_10p = "10p"
denomination_label_5p = "5p"
denomination_label_2p = "2p"
denomination_label_1p = "1p"

pounds = pennies//100
pound_50_denominations = pounds//50
pound_20_denominations = (pounds%50)//20
pound_10_denominations = ((pounds%50)%20)//10
pound_5_denominations = (((pounds%50)%20)%10)//5
pound_1_denominations = ((((pounds%50)%20)%10)%5)//1
remaining_pounds = ((((pounds%50)%20)%10)%5)%1
denominations_50_p = pennies%100//50
denominations_20_p = (pennies%100%50)//20
denominations_10_p = ((pennies%100%50)%20)//10
denominations_5_p = (((pennies%100%50)%20)%10)//5
denominations_2_p = ((((pennies%100%50)%20)%10)%5)//2
denominations_1_p = (((((pennies%100%50)%20)%10)%5)%2)//1

  
#print(denominations_50_p)
#print(pound_1_denominations)

print(f"Till total: £{total_pounds:,}")
print(f"Pennies:    {pennies}")
print(f"{denomination_label_50:<4} x {pound_50_denominations}")
print(f"{denomination_label_20:<4} x {pound_20_denominations}")
print(f"{denomination_label_10:<4} x {pound_10_denominations}")
print(f"{denomination_label_5:<4} x {pound_5_denominations}")
print(f"{denomination_label_1:<4} x {pound_1_denominations}")
print(f"{denomination_label_50p:<4} x {denominations_50_p}")
print(f"{denomination_label_20p:<4} x {denominations_20_p}")
print(f"{denomination_label_10p:<4} x {denominations_10_p}")
print(f"{denomination_label_5p:<4} x {denominations_5_p}")
print(f"{denomination_label_2p:<4} x {denominations_2_p}")
print(f"{denomination_label_1p:<4} x {denominations_1_p}")


