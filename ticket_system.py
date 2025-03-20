import agent
import ticket

# Move all state into the TicketSystem class and all interaction (print, input) out into a mainfile that doesn't have to be a class.

class TicketSystem:

    agents = []
    tickets = []

    def __init__(self):
        print("Creating ticketing system...")

    def create_agent(self, name, department):
        self.agents.append(agent.Agent(name, department))

    def create_ticket(self, name, issue):
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
    
    def print_system_state(self):
        print("Tickets:\n")
        self.list_tickets()
        print()
        print("Agents:\n")
        self.list_agents()

    def assign_ticket(self, agent, ticket):
        self.print_system_state()
        if not agent and not ticket:
            agent = self.agents[int(input("Enter agent #: "))]
            ticket = self.ticket[int(input("Enter ticket #: "))]
        agent.assign_ticket(ticket)
        print("Updated assignments:\n")
        self.print_system_state()

    def toggle_ticket_status():
        print("Changing ticket status to...")

    def add_note_to_ticket():
        print("Adding note to ticket...")

