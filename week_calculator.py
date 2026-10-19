term_week = 5
print(f"it is Term 4, Week {term_week}.")
week = int(input("What week is it?"))
print(f"You are currently in Week {week}.")
if week <= 3:
    print("Still early in the term.")
elif week <= 7:
    print("Mid-term grind")
else:
    print("Almost done!")
