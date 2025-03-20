from ticket_system import TicketSystem

ts = TicketSystem()

def get_choice():
    print("What would you like to do? ")
    print("1: Create Agent\n2: Create Ticket\n3: Assign Ticket\n4: Close/Reopen Ticket\n5: Add Note to Ticket\n6: List Agents\n7: List Tickets\n9: Quit\n")
    return int(input("Choice: "))

def print_system_state():
    print("Agents:\n")
    print(ts.list_agents())
    print("Tickets:\n")
    print(ts.list_tickets())

def create(ts, object_type):
    print(f"Create {object_type}...")
    name = input("Enter name: ")
    predicate = input("Enter department or issue: ")
    func = getattr(ts, f"create_{object_type}")
    func(name, predicate)
 
def main():
    print("Starting ticket system...")
    option = get_choice()

    while option != 9:
        match option:
            case 1: # Create agent
                create(ts, "agent")
                option = get_choice()
            case 2: # Create ticket
                create(ts, "ticket")
                option = get_choice()
            case 3: # Assign ticket
                print_system_state()
                agent = ts.agents[int(input("Enter agent #: "))]
                ticket = ts.tickets[int(input("Enter ticket #: "))]
                ts.assign_ticket(agent, ticket)
                print("Updated assignments:\n")
                print_system_state()
                option = get_choice()
            case 4: # Close/reopen ticket
                ts.list_tickets()
                ticket = ts.tickets[int(input("Enter ticket #: "))]
                ticket.toggle()
                option = get_choice()
            case 5: # Add note to ticket
                print(ts.list_tickets())
                ticket = int(input("Enter ticket #: "))
                note = input("Enter note: ")
                ts.tickets[ticket].add_note(note)
                print(ts.tickets[ticket].fetch_notes())
                option = get_choice()
            case 6: # List agents
                print("Agents in system: ")
                print(ts.list_agents())
                option = get_choice()
            case 7: # List tickets
                print("Ticket in system: ")
                print(ts.list_tickets())
                option = get_choice()
            case 9: # Exit
                break
            case _:
                print("Invalid choice.")
                option = get_choice()

if __name__ =="__main__":
    main()
