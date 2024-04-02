age = input("How old are you in years?\n")

avg_yrs_remaining = 90 - int(age)
avg_wks_remaining = avg_yrs_remaining * 52

print(f"You have roughly {avg_wks_remaining} weeks left.")