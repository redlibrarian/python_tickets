import agent
import ticket

# What does a ticket system need to do

# Create Agent
# Create Ticket
# Assign Ticket
# Close/Reopen Ticket
# Add note to Ticket
# Maintain Ticket Queue
# Send notification on ticket assignment or note addition (to assigned agent, if no assigned agent, error)

# List agents
# List tickets

# This can be a DOS-tyle menu system for now.

agents = []
tickets = []

def get_choice():
  print("What would you like to do?")
  print("1: Create Agent 2: Create Ticket 3: Assign Ticket 4: Close/Reopen Ticket 5: Add Note to Ticket 6: List Agents 7: List Tickets 9: Quit")
  return int(input("Choice: "))

def create_agent():
  print("Create Agent.")
  name = input("Enter agent name: ")
  department = input("Enter agent department: ")
  agents.append(agent.Agent(name, department))

def list_agents():
  print("Agents in system: ")
  for agent in agents:
    print(agent)

def list_tickets():
  print("Tickets in system: ")
  for ticket in tickets:
    print(ticket)

def create_ticket():
  print("Create ticket: ")
  user = input("Uset Name: ")
  issue = input("What is the issue? ")
  tickets.append(ticket.Ticket(user, issue))

def assign_ticket():
  # display agent list
  # display ticket list
  # with agent name and ticket ID how to I assign a ticket to the agent's queue?
  # list_tickets should display the assigned agent.

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

