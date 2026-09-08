def get_season(month):
    seasons = ("winter", "spring", "summer", "autumn")
    if month <= 0 or month > 12:
        print(f"You entered: {month}")
        print("Please enter a number between 1 and 12.")
        return

    if month in (12, 1, 2):
        season = seasons[0]
    elif month in (3, 4, 5):
        season = seasons[1]
    elif month in (6, 7, 8):
        season = seasons[2]
    else:
        season = seasons[3]

    print(f"You entered: {month}")
    print(f"The season is {season}.")

month = int(input("Enter the number of a month (1-12): "))
get_season(month)