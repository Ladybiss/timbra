from datetime import datetime as dt
from datetime import timedelta as td
from ..usertime import UserTime
from ..timbra import UserResult, calculate


def test_create_correct_usertime_obj():
    in_morning = dt(2016, 6, 2, 9, 1)
    out_lunch = dt(2016, 6, 2, 13, 2)
    in_lunch = dt(2016, 6, 2, 13, 35)
    total_hours = td(hours=8)
    min_lunch_length = td(minutes=30)
    myobj = UserTime(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)
    assert myobj.in_morning == in_morning
    assert myobj.out_lunch == out_lunch
    assert myobj.in_lunch == in_lunch
    assert myobj.total_hours == total_hours
    assert myobj.min_lunch_length == min_lunch_length


def test_create_correct_userresult_obj():
    morning_work = td(hours=4)
    lunch_break = td(minutes=33)
    afternoon_work = td(hours=4, minutes=30)
    out_evening = dt(2016, 6, 2, 17, 32)
    myobj = UserResult(morning_work, lunch_break, afternoon_work, out_evening)
    assert myobj.morning_work == morning_work
    assert myobj.lunch_break == lunch_break
    assert myobj.afternoon_work == afternoon_work
    assert myobj.out_evening == out_evening


def test_equality_for_usertime():
    in_morning = dt(2016, 6, 2, 9, 1)
    out_lunch = dt(2016, 6, 2, 13, 2)
    in_lunch = dt(2016, 6, 2, 13, 35)
    total_hours = td(hours=8)
    min_lunch_length = td(minutes=30)
    myobj1 = UserTime(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)
    myobj2 = UserTime(in_morning, out_lunch, in_lunch, total_hours, min_lunch_length)

    assert myobj1 == myobj2


def test_inequality_for_usertime():
    in_morning = dt(2016, 6, 2, 9, 1)
    out_lunch = dt(2016, 6, 2, 13, 2)
    in_lunch = dt(2016, 6, 2, 13, 35)
    total_hours = td(hours=8)
    myobj1 = UserTime(in_morning, out_lunch, in_lunch, total_hours, td(minutes=30))
    myobj2 = UserTime(in_morning, out_lunch, in_lunch, total_hours, td(minutes=29))

    assert myobj1 != myobj2


def test_equality_for_userresult():
    morning_work = td(hours=4)
    lunch_break = td(minutes=33)
    afternoon_work = td(hours=4, minutes=30)
    out_evening = dt(2016, 6, 2, 17, 32)
    myobj1 = UserResult(morning_work, lunch_break, afternoon_work, out_evening)
    myobj2 = UserResult(morning_work, lunch_break, afternoon_work, out_evening)

    assert myobj1 == myobj2


def test_inequality_for_userresult():
    lunch_break = td(minutes=33)
    afternoon_work = td(hours=4, minutes=30)
    out_evening = dt(2016, 6, 2, 17, 32)
    myobj1 = UserResult(td(hours=4), lunch_break, afternoon_work, out_evening)
    myobj2 = UserResult(td(hours=4, minutes=1), lunch_break, afternoon_work, out_evening)

    assert myobj1 != myobj2


def test_calculate_with_lunch_longer_than_min_lunch():
    my_user_time = UserTime(dt(2016, 6, 2, 9, 0), dt(2016, 6, 2, 13, 0), dt(2016, 6, 2, 13, 35), td(hours=8), td(minutes=30))
    expected_user_result = UserResult(td(hours=4), td(minutes=35), td(hours=4), dt(2016, 6, 2, 17, 35))
    #this assert is working for __eq__ method in UserResult
    assert calculate(my_user_time) == expected_user_result


def test_calculate_with_lunch_shorter_than_min_lunch():
    my_user_time = UserTime(dt(2016, 6, 2, 9, 0), dt(2016, 6, 2, 13, 0), dt(2016, 6, 2, 13, 25), td(hours=8), td(minutes=30))
    expected_user_result = UserResult(td(hours=4), td(minutes=25), td(hours=4), dt(2016, 6, 2, 17, 30))
    #this assert is working for __eq__ method in UserResult
    assert calculate(my_user_time) == expected_user_result

