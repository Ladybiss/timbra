class UserResult:
    def __init__(self, morning_work, lunch_break, afternoon_work, out_evening):
        self.morning_work = morning_work
        self.lunch_break = lunch_break
        self.afternoon_work = afternoon_work
        self.out_evening = out_evening

    def __eq__(self, other):
        return (
            other.morning_work == self.morning_work and
            other.lunch_break == self.lunch_break and
            other.afternoon_work == self.afternoon_work and
            other.out_evening == self.out_evening
        )


def calculate(my_user_time):
    morning_work = my_user_time.out_lunch - my_user_time.in_morning
    lunch_break = my_user_time.in_lunch - my_user_time.out_lunch
    afternoon_work = my_user_time.total_hours - morning_work
    min_out_evening = my_user_time.in_morning + morning_work + lunch_break + afternoon_work
    if lunch_break >= my_user_time.min_lunch_length:
        out_evening = min_out_evening
    else:
        out_evening = min_out_evening + (my_user_time.min_lunch_length - lunch_break)
    return UserResult(morning_work, lunch_break, afternoon_work, out_evening)

     #memo coerenza orari/durate





