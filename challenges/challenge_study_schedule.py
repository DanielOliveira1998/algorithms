def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    active_students = 0
    if target_time is None:
        return None
    for student in permanence_period:
        if not isinstance(student[0], int) or not isinstance(student[1], int):
            return None
        if (student[0] <= target_time) and (student[1] >= target_time):
            active_students += 1
    return active_students
