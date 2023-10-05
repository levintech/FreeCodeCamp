def add_time(start, duration, day_of_week=""):
  weekdays = ("monday", "tuesday", "wednesday", "thursday", "friday",
              "saturday", "sunday")

  time, tag = start.split()
  (start_hour, start_min) = map(int, time.split(":"))
  (duration_hour, duration_min) = map(int, duration.split(":"))

  if tag == "PM":
    start_hour += 12

  new_time_min = start_min + duration_min
  new_time_hour = start_hour + duration_hour

  if new_time_min >= 60:
    new_time_min %= 60
    new_time_hour += 1

  days_shift = 0
  if new_time_hour >= 24:
    days_shift = new_time_hour // 24
    new_time_hour %= 24

  tag = "AM"
  if new_time_hour > 12:
    new_time_hour -= 12
    tag = "PM"
  elif new_time_hour == 12:
    tag = "PM"
  elif new_time_hour == 0:
    new_time_hour = 12
    tag = "AM"

  new_time = str(new_time_hour) + \
            ":" + \
            str(new_time_min).rjust(2, "0") + \
            " " + \
            tag

  if day_of_week:
    index = weekdays.index(day_of_week.lower())
    new_index = (index + days_shift) % 7
    new_time += f", {weekdays[new_index].capitalize()}"
  if days_shift > 1:
    new_time += f" ({days_shift} days later)"
  elif days_shift == 1:
    new_time += " (next day)"

  return new_time
