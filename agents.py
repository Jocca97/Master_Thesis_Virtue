import mesa
import numpy as np
from numpy import random


# fixed variables
cost_punish_agent = 1
agent_punishment = 3
fixed_loss = 2


class MoralAgents(mesa.Agent):
    def __init__(self, unique_id, model, agent_type='cooperator' or 'defector'):
        super().__init__(unique_id, model)
        self.public_good_game = model
        self.agent_type = agent_type  # This attribute differentiates agent types
        self.wealth = 20
        self.moral_worth = np.random.normal(5, 3.5)
        self.moral_worth_weight = self.contribution_moral_worth()
        self.neighbors_weight = self.contribution_neighbors()
        self.contribution_amount = self.calculate_contribution_amount()
        self.invest = self.calculate_invest()


    ## Investing Behaviors

    def contribution_neighbors(self):
        """

        A function that defines the probability of contribution according to what an agent's
        neighbors do

        """
        probability_contribution = 0
        fixed_loss = 2 #put it somewhere else after
        neighbors = self.model.grid.get_cell_list_contents([self.pos])
        if self.agent_type == 'coperator':
            for self.agent_type in neighbors:
                if self.calculate_invest() > fixed_loss:
                    probability_contribution += 0.1
                if self.calculate_invest() == fixed_loss:
                    probability_contribution -= 0.1
            return probability_contribution
        else: #defector
            for self.agent_type in neighbors:
                if self.calculate_invest() > fixed_loss:
                    probability_contribution += 0.1
                if self.calculate_invest() == fixed_loss:
                    probability_contribution -= 0.1
            return probability_contribution


    def contribution_moral_worth(self):
        """

        A function that defines the contribution amount according to?

        """
        # Alternatively, I can increase weights instead of actual amount
        probability_contribution = 0
        if self.agent_type == 'cooperator' or 'defector':
            if self.moral_worth == 0:
                probability_contribution =+ 0.2
            elif 1 <= self.moral_worth <= 5:
                probability_contribution =+ 0.2
            elif 6 <= self.moral_worth <= 10:
                probability_contribution =+ 0.6
            elif self.moral_worth >= 11:
                probability_contribution =+ 0.8
            elif self.moral_worth <= 0:
                probability_contribution -= 0.2
        return probability_contribution
     # more instances of negative moral worth should probably be added

##Conversely Cooperators can be distinguished by Defectors how much moral worth affects their decision
###What would be the theorical application of this tho

    def calculate_contribution_amount(self):
        contribution_amount = 0
        if self.agent_type == 'cooperator' or 'defector':
            contribution_amount += 17.7
        return contribution_amount

    def calculate_invest(self):
        """

        A method that defines the investment behaviors of agents

        """
        if self.agent_type == 'cooperator' or 'defector':
            probability_contributing = (self.moral_worth_weight * 0.3) + (self.neighbors_weight * 0.7)
            if probability_contributing >= random.random():
                invest = self.calculate_contribution_amount()
            else:
                invest = fixed_loss

            return invest

    def step(self):
        self.move()
        if self.wealth > 17.7:  # stay like this for now
            self.contribution_neighbors()
            self.contribution_moral_worth()
            self.calculate_contribution_amount()
            self.calculate_invest()
            self.moral_worth_assignment()
            self.altruistic_punishment()
            self.antisocial_punishment_initiator()
        else:
            pass