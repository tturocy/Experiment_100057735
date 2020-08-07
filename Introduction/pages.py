from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    form_model = 'player'
    form_fields = ['do_you_understand']



class PreTestSurvey(Page):
    form_model = 'player'
    form_fields = ['pre_test_question', 'pre_test_question_2', 'pre_test_question_3']

    def vars_for_template(self):
        if self.session.config['tax_framing']:
            return {
                'labels': [
                    "What percentage of declared income will you have to pay in taxes?",
                    "What is the probability that your tax return will be audited?",
                    "If audited and found to be under-declaring, how much will you pay in fines "
                    "for each ECU of under-reported tax?"
                ]
            }
        else:
            return {
                'labels': [
                    "What percentage of announced income will you have to pay in deductions?",
                    "What is the probability that your announcement will be reviewed?",
                    "If reviewed and found to have not announced your full income, "
                    "how much will you pay in additional deductions for each ECU of "
                    "under-announced deductions?"
                ]
            }


page_sequence = [Introduction, PreTestSurvey]
