from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import time

class Start_Round(Page):
    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + Constants.task_time +0.2


class Task(Page):
    form_model = 'player'
    form_fields = ['count']

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    
    def is_displayed(self):
        return self.get_timeout_seconds() > 1
    
    def vars_for_template(self):
        i = self.participant.vars['i']
        table = self.participant.vars['tables'][i]
        correct_answer = self.participant.vars['answers'][i]
        self.participant.vars['next_correct_answer'] = correct_answer
        return dict(correct = correct_answer, table_values = table)
    
    def before_next_page(self):
        self.player.check_answer()
        self.player.update_iterator()
        self.participant.vars['expiry'] = self.participant.vars['expiry']
        self.player.count = None


class Tax_Man(Page):
    form_model = 'player'
    form_fields = ['claimed_earnings']
    def vars_for_template(self):
        return dict(tables_correct=self.player.correct_counts,
                    number_of_tables_counted=self.player.counts_submitted,
                    earned_in_round=self.player.pay_for_round)
    
    def before_next_page(self):
        self.player.handle_taxes()


class Post_Tax(Page):
    def vars_for_template(self):
        return dict(audited = self.player.tax_audit,
                    earned = self.player.pay_for_round,
                    claimed_earnings = self.player.claimed_earnings,
                    tax_message = self.player.tax_message,
                    tax_amount = self.player.tax_on_claimed,
                    profit_for_round = self.player.final_earnings,
                    payoff_so_far = self.participant.vars['payoff'])


task_pages = [Task for i in range(Constants.max_tables_in_round)]

page_sequence = [Start_Round, *task_pages, Tax_Man, Post_Tax]
