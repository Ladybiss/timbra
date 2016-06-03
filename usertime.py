from datetime import timedelta as td


class UserTime:
    def __init__(self, in_morning, out_lunch, in_lunch, total_hours, min_lunch_length):
        self.in_morning = in_morning
        self.out_lunch = out_lunch
        self.in_lunch = in_lunch
        self.total_hours = total_hours
        self.min_lunch_length = min_lunch_length
        if not self.validate():
            raise ValueError


    def __eq__(self, other):
        return (
            other.in_morning == self.in_morning and
            other.out_lunch == self.out_lunch and
            other.in_lunch == self.in_lunch and
            other.total_hours == self.total_hours and
            other.min_lunch_length == self.min_lunch_length
        )

    def validate(self):
        return (td(hours=1) <= self.total_hours <= td(hours=12)) and (self.in_morning < self.out_lunch < self.in_lunch)




