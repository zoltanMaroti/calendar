import ui
import storage


def main_menu():
    print("""
    Menu:
    (s) schedule a new meeting
    (c) cancel an existing meeting
    (q) quit
    """)


def add_meeting(table, reserved_time_slots, available_time_slots):
    work_start_time = 8
    work_finish_time = 18
    print("Schedule a new meeting.")
    temporary_time_slot = []
    while True:
        try:
            start_time = int(input("Enter start time: "))
            if start_time < work_start_time or start_time >= work_finish_time:
                raise NameError
            duration = int(input("Enter duration in hours (1 or 2): "))
            break
        except ValueError:
            print("Please enter numbers only!")
        except NameError:
            print("ERROR: Meeting is outside of your working hours (8 to 18)!")
    end_time = start_time + duration
    availability_status = ui.is_available(start_time,
                                          available_time_slots, duration)
    if availability_status:
        ui.remove_from_available_time_slots(start_time,
                                            duration, available_time_slots)
        temporary_time_slot.append(start_time)
        temporary_time_slot.append(end_time)
        meeting_title = input("Enter meeting title: ")
        temporary_time_slot.append(meeting_title)
        table.append(temporary_time_slot)
        ui.add_to_reserved_time_slots(duration,
                                      reserved_time_slots, start_time)
        print("Meeting added.")
    else:
        print("Meeting overlaps with existing meeting!")


def cancel_meeting(available_time_slots, reserved_time_slots, table):
    while True:
        try:
            start_time = int(input("Enter the start time: "))
            if start_time in reserved_time_slots:
                ui.remove_from_reserved_time_slots(start_time,
                                                   reserved_time_slots,
                                                   available_time_slots, table)
                ui.add_to_available_time_slots(start_time, table,
                                               available_time_slots)
                for row in table:
                    if row[0] == start_time:
                        table.remove(row)
                print("Meeting canceled.")
                break
            else:
                print("ERROR: There is no meeting starting at that time!")
        except ValueError:
            print("Please enter numbers only!")


def edit_meeting():
    start_time = int(input("Enter the start time: "))
    for item in table:
        if item[0] == start_time:
            start_time = int(input("Please enter the new start time: "))
            new_duration = int(input("Enter new duration in hours (1 or 2): "))
            new_meeting_title = input("Please enter the new meeting title: ")
    pass


def choose(table, reserved_time_slots, available_time_slots):
    answer = input("Your choice: ")
    if answer == 's':
        add_meeting(table, reserved_time_slots, available_time_slots)
    if answer == 'c':
        cancel_meeting(available_time_slots, reserved_time_slots, table)
    # if answer == 'e':
        # edit_meeting()
    if answer == 'q':
        storage.write_table("meetings.txt", table)
        exit()


def main():
    table = storage.get_table("meetings.txt")
    reserved_time_slots = storage.get_reserved_time_slots(table)
    available_time_slots = storage.get_available_time_slots(
                                                    table, reserved_time_slots)
    while True:
        ui.print_schedule(available_time_slots, table)
        main_menu()
        choose(table, reserved_time_slots, available_time_slots)

main()
