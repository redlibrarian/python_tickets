# What does a ticket system need to do

# Create Agent
# Create Ticket
# Assign Ticket
# Close/Reopen Ticket
# Add note to Ticket
# Maintain Ticket Queue
# Send notification on ticket assignment or note addition (to assigned agent, if no assigned agent, error)

# This can be a DOS-tyle menu system for now.

def get_choice():
  print("What would you like to do?")
  print("1: Create Agent 2: Create Ticket 3: Assign Ticket 4: Close/Reopen Ticket 5: Add Note to Ticket 9: Quit")
  return int(input("Choice: "))

def create_agent():
  print("Creating agent...")

def create_ticket():
  print("Creating ticket...")

def assign_ticket():
  print("Assigning ticket...")

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
        break # Just until I've added real logic
      case 2:
        create_ticket()
        break
      case 3:
        assign_ticket()
        break
      case 4:
        toggle_ticket_status()
        break
      case 5:
        add_note_to_ticket()
        break
      case 9: 
        break
      case _:
        print("Invalid choice.")
        option = get_choice()


if __name__ == '__main__':
  main()

