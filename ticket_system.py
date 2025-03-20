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
        return dict((index, agent) for index, agent in enumerate(self.agents))

    def list_tickets(self):
       return dict((index, issue) for index, issue in enumerate(self.tickets))

    def assign_ticket(self, agent, ticket):
        agent.assign_ticket(ticket)



