def print_schedule(available_time_slots, table):
    # print("Available time slots: ", available_time_slots)
    print("Your schedule for the day:")
    if len(table) == 0:
        print("(empty)")
    else:
        for row in table:
            print(row[0], "-", row[1], row[2])
    hours = count_meeting_hours(table)
    print(f"Total meeting hours: {hours}")


def is_available(start_time, available_time_slots, duration):
    """ Checks if starting time and ending time is available or not.

    Args:
        start_time: start time of meeting by user input
        available_time_slots: list of available times
        duration: lenght of meeting by user input (1 or 2 hours)

    Returns:
        True if available, else returns False.

    """
    if start_time in available_time_slots and duration == 1:
        return True
    if start_time in available_time_slots and duration == 2:
        ending_time = start_time + 1
        if ending_time in available_time_slots:
            return True
        else:
            return False
    else:
        return False


def remove_from_available_time_slots(start_time,
                                     duration, available_time_slots):
    if duration == 1:
        available_time_slots.remove(start_time)
    if duration == 2:
        available_time_slots.remove(start_time)
        available_time_slots.remove(start_time + 1)
    return available_time_slots


def remove_from_reserved_time_slots(start_time, reserved_time_slots,
                                    available_time_slots, table):
    ending_time = start_time + 1
    for line in table:
        if line[0] == start_time:
            if line[1] - line[0] == 2:
                reserved_time_slots.remove(start_time)
                reserved_time_slots.remove(ending_time)
            else:
                reserved_time_slots.remove(start_time)


def add_to_reserved_time_slots(duration, reserved_time_slots, start_time):
    if duration == 2:
            reserved_time_slots.append(int(start_time))
            reserved_time_slots.append(int(start_time + 1))
    else:
        reserved_time_slots.append(int(start_time))


def add_to_available_time_slots(start_time, table, available_time_slots):
    ending_time = start_time + 1
    for line in table:
        if line[0] == start_time:
            if line[1] - line[0] == 2:
                available_time_slots.append(start_time)
                available_time_slots.append(ending_time)
            else:
                available_time_slots.append(start_time)


def count_meeting_hours(table):
    hours = []
    for item in table:
        if item[1] - item[0] == 2:
            hours.append(2)
        else:
            hours.append(1)
    total_hours = sum(hours)
    return total_hours
