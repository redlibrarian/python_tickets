import agent
import ticket

class TicketSystem:

    agents = []
    tickets = []

    def __init__(self):
        print("Creating ticketing system...")

    def get_choice(self):
        print("What would you like to do?")
        print("1: Create Agent\n2: Create Ticket\n3: Assign Ticket\n4: Close/Reopen Ticket\n5: Add Note to Ticket\n6: List Agents\n7: List Tickets\n9: Quit")
        print()
        return int(input("Choice: "))

    def create_agent(self, name=None, department=None):
        print("Create Agent.")
        if not name and not department:
          name = input("Enter agent name: ")
          department = input("Enter agent department: ")
        self.agents.append(agent.Agent(name, department))

    def create_ticket(self, name=None, issue=None ):
        print("Create ticket: ")
        if not name and not issue:
          user = input("User Name: ")
          issue = input("What is the issue? ")
        self.tickets.append(ticket.Ticket(name, issue))

    def list_agents(self):
        print("Agents in system: ")
        return dict((index, agent) for index, agent in enumerate(self.agents))

    def print_agents():
      print("Agents in system: ")
      for index, agent in self.list_agents:
        print(index, agent)

    def list_tickets(self):
       print("Tickets in system: ")
       return dict((index, issue) for index, issue in enumerate(self.tickets))

    def print_tickets():
        print("Tickets in system: ")
        for index, ticket in self.list_tickets:
            print(index, ticket)
    
    def print_system_state():
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

    def run_system():
        option = self.get_choice()

        while option != 9:
            match option:
                case 1:
                    create_agent()
                    option = self.get_choice()
                case 2:
                    create_ticket()
                    option = self.get_choice()
                case 3:
                    assign_ticket()
                    option = self.get_choice()
                case 4:
                    toggle_ticket_status()
                    break
                case 5:
                    add_note_to_ticket()
                    break
                case 6:
                    list_agents()
                    option = self.get_choice()
                case 7: 
                    list_tickets()
                    option = self.get_choice()
                case 9: 
                    break
                case _:
                    print("Invalid choice.")
                    option = self.get_choice()

