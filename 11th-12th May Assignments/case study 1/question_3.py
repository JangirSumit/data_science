# 3. Weather forecasting organization wants to show is it day or night.
# So, write a program for such organization to find whether is it dark outside or not.
# Hint: Use time module.

from datetime import datetime


def get_part_of_day(hour):
    return (
        "light" if 5 <= hour <= 18
        else
        "dark"
    )


h = datetime.now().hour

print(f"Its {get_part_of_day(h)}  right now.")
