def study_schedule(permanence_period, target_time):
    counter_study = 0
    if not isinstance(target_time, int):
        return None
    for [period_start, period_end] in permanence_period:
        if type(period_start) != int or type(period_end) != int:
            return None
        if period_start <= target_time and period_end >= target_time:
            counter_study += 1
    return counter_study
