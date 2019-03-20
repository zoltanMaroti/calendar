def write_table(filename, table):
    # sorted(table, key=lambda x: x[0])
    with open(filename, "r+") as file:
        file.truncate()
        for line in table:
            line[0] = str(line[0])
            line[1] = str(line[1])
        for row in table:
            line = ",".join(row)
            file.write(line+"\n")


def get_table(filename):
    table = []
    with open(filename, "r+") as file:
        for item in file:
            line = item.strip("\n")
            row = line.split(",")
            table.append(row)
        for line in table:
            line[0] = int(line[0])
            line[1] = int(line[1])
        return table


def get_reserved_time_slots(table):
    reserved_time_slots = []
    for line in table:
        if line[1] - line[0] == 2:
            reserved_time_slots.append(line[0])
            reserved_time_slots.append(line[0] + 1)
        else:
            reserved_time_slots.append(line[0])
    return reserved_time_slots


def get_available_time_slots(table, reserved_time_slots):
    available_time_slots = []
    time_slots = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    for number in time_slots:
        if number not in reserved_time_slots:
            available_time_slots.append(number)
    return available_time_slots
