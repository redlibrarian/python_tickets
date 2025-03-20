import agent
import ticket

class TicketSystem:

    agents = []
    tickets = []

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
    
    def assign_ticket(self, agent, ticket):
        agent.assign_ticket(ticket)

    def toggle_ticket_status():
        print("Changing ticket status to...")

    def add_note_to_ticket():
        print("Adding note to ticket...")

