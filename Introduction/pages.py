from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    form_model = 'player'
    form_fields = ['do_you_understand']



class PreTestSurvey(Page):
    form_model = 'player'
    form_fields = ['pre_test_question', 'pre_test_question_2', 'pre_test_question_3']


page_sequence = [Introduction, PreTestSurvey]
