import agent
import ticket

agents = []
tickets = []

def get_choice():
  print("What would you like to do?")
  print("1: Create Agent\n2: Create Ticket\n3: Assign Ticket\n4: Close/Reopen Ticket\n5: Add Note to Ticket\n6: List Agents\n7: List Tickets\n9: Quit")
  print()
  return int(input("Choice: "))

def create_agent():
  print("Create Agent.")
  name = input("Enter agent name: ")
  department = input("Enter agent department: ")
  agents.append(agent.Agent(name, department))

def list_agents():
  print("Agents in system: ")
  for index, agent in enumerate(agents):
    print(index, agent)

def list_tickets():
  print("Tickets in system: ")
  for index, ticket in enumerate(tickets):
    print(index, ticket)

def create_ticket():
  print("Create ticket: ")
  user = input("Uset Name: ")
  issue = input("What is the issue? ")
  tickets.append(ticket.Ticket(user, issue))

def display_system_state():
  print("Tickets:\n")
  list_tickets()
  print()
  print("Agents:\n")
  list_agents()

def assign_ticket():
  display_system_state()
  ticket = int(input("Enter ticket #: "))
  agent = int(input("Enter agent #: "))
  agents[agent].assign_ticket(tickets[ticket])
  print("Updated assignments:\n")
  display_system_state()

def toggle_ticket_status():
  print("Changing ticket status to...")

def add_note_to_ticket():
  print("Adding note to ticket...")

def main():
  option = get_choice()

  while option != 9:
    match option:
      case 1:
        create_agent()
        option = get_choice()
      case 2:
        create_ticket()
        option = get_choice()
      case 3:
        assign_ticket()
        break
      case 4:
        toggle_ticket_status()
        break
      case 5:
        add_note_to_ticket()
        break
      case 6:
        list_agents()
        option = get_choice()
      case 7: 
        list_tickets()
        option = get_choice()
      case 9: 
        break
      case _:
        print("Invalid choice.")
        option = get_choice()


if __name__ == '__main__':
  main()
