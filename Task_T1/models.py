from otree.api import (models, widgets, BaseConstants, BaseSubsession,
                       BaseGroup, BasePlayer, Currency as c, currency_range)
from django.db import models as djmodels
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from numpy.random import choice


class Constants(BaseConstants):
    name_in_url = 'Experiment_Task_T1'
    players_per_group = None
    num_rounds = 5
    task_time = 40
    payment_per_correct_answer = 1
    table_pay = c(10)
    tax_rate = 0.25
    max_tables_in_round = 100
    table_rows = 5
    table_columns = 5


def create_table(rows, columns, numbers):
    answer = 0
    table = []
    for row in range(rows):
        row_values = []
        for column in range(columns):
            new_value = choice(numbers)
            row_values.append(new_value)
            answer += new_value
        table.append(row_values)
    return table, answer

class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['tables'] = []
            p.participant.vars['answers'] = []
            for i in range(Constants.max_tables_in_round):
                new_table, new_answer = create_table(Constants.table_rows, Constants.table_columns,
                                                     [0, 1])
                p.participant.vars['tables'].append(new_table)
                p.participant.vars['answers'].append(new_answer)
            #p.participant.vars['tables'] = [1 for i in range(Constants.max_tables_in_round)]
            p.participant.vars['i'] = 0
            if 'payoff' not in p.participant.vars:
                p.participant.vars['payoff'] = 0


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    count = models.IntegerField(min=0, label='How many ones are in the table?')
    correct_counts = models.IntegerField(initial=0)
    counts_submitted = models.IntegerField(initial=0)
    pay_for_round = models.CurrencyField(initial=c(0))
    claimed_earnings = models.CurrencyField(label='Please announce your income in the box, then click next')
    tax_audit = models.BooleanField()
    tax_message = models.StringField()
    tax_on_claimed = models.CurrencyField(initial=c(0))
    post_tax_earnings = models.CurrencyField(initial=c(0))
    final_earnings = models.CurrencyField(initial=c(0))
    
    def check_answer(self):
        self.counts_submitted += 1
        if self.count == self.participant.vars['next_correct_answer']:
            self.correct_counts += 1
            self.pay_for_round += Constants.table_pay
    
    def update_iterator(self):
        self.participant.vars['i'] += 1
        if self.participant.vars['i'] >= Constants.max_tables_in_round:
            self.participant.vars['i'] = 0
    
    def handle_taxes(self):
        self.tax_audit = choice([True, False], p=[0.2, 0.8])
        self.tax_on_claimed = self.claimed_earnings*Constants.tax_rate
        self.post_tax_earnings = self.pay_for_round - self.tax_on_claimed
        if self.tax_audit:
            self.tax_message = 'You have been reviewed. '
            if self.claimed_earnings >= self.pay_for_round:
                self.tax_message = self.tax_message + 'However, you announced all of your earnings, so don\'t face any deductions.'
                self.final_earnings = self.post_tax_earnings
            else:
                not_claimed = self.pay_for_round - self.claimed_earnings
                extra_tax = not_claimed*2*Constants.tax_rate
                self.tax_message = self.tax_message + f'You did not announce {not_claimed} ECU of your earnings. You are deducted {extra_tax} ECU.'
                self.final_earnings = self.post_tax_earnings - extra_tax
        else:
            self.tax_message = 'You have not been reviewed this round.'
            self.final_earnings = self.post_tax_earnings
        self.participant.vars['payoff'] += self.final_earnings
