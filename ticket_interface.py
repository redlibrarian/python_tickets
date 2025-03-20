from ticket_system import TicketSystem

ts = TicketSystem()

def get_choice():
    print("What would you like to do? ")
    print("1: Create Agent\n2: Create Ticket\n3: Assign Ticket\n4: Close/Reopen Ticket\n5: Add Note to Ticket\n6: List Agents\n7: List Tickets\n9: Quit\n")
    return int(input("Choice: "))

 
def main():
    print("Starting ticket system...")
    option = get_choice()

    while option != 9:
        match option:
            case 1:
                print("Create Agent:")
                name = input("Enter agent name: ")
                department = input("Enter agent department: ")
                ts.create_agent(name, department)
                option = get_choice()
            case 2:
                print("Creat Ticket:")
                name = input("Enter user name: ")
                issue = input("What is the issue? ")
                ts.create_ticket(name, issue)
                option = get_choice()
            case 3:
                ts.assign_ticket()
                option = get_choice()
            case 4:
                ts.toggle_ticket_status()
                break
            case 5:
                ts.add_note_to_ticket()
                break
            case 6:
                ts.list_agents()
                option = get_choice()
            case 7: 
                ts.list_tickets()
                option = get_choice()
            case 9: 
                break
            case _:
                print("Invalid choice.")
                option = get_choice()

if __name__ =="__main__":
    main()
