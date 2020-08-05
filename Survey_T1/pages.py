from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Lottery(Page):
    form_model = 'player'
    form_fields = ['lottery_switch_table']

class PostTestSurvey(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
                   'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17']


page_sequence = [Lottery, PostTestSurvey]
