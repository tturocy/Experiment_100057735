from otree.api import (models, widgets, BaseConstants, BaseSubsession,
                       BaseGroup, BasePlayer, Currency as c, currency_range)


class Constants(BaseConstants):
    name_in_url = 'Experiment_Introduction_T2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    """
    Pre task related section
    """
    pre_test_question = models.StringField(label='What percentage of declared income will you have to pay in taxes?', choices=['20%', '25%', '50%'])
    def pre_test_question_error_message(self, value):
        if value == '20%':
            return 'That\'s incorrect. The correct answer is 25%. Correct your answer in order to continue.'
        if value == '50%':
            return 'That\'s incorrect. The correct answer is 25%. Correct your answer in order to continue.'
    pre_test_question_2 = models.StringField(label='What is the probability that your tax return will be audited?', choices=['20%', '25%', '50%'])
    def pre_test_question_2_error_message(self, value):
        if value == '25%':
            return 'That\'s incorrect. The correct answer is 20%. Correct your answer in order to continue.'
        if value == '50%':
            return 'That\'s incorrect. The correct answer is 20%. Correct your answer in order to continue.'
    pre_test_question_3 = models.StringField(label='If audited and found to be under declaring, how much will you pay in fines', choices=['20%', '25%', '50%'])
    def pre_test_question_3_error_message(self, value):
        if value == '20%':
            return 'That\'s incorrect. The correct answer is 50%. Correct your answer in order to continue.'
        if value == '25%':
            return 'That\'s incorrect. The correct answer is 50%. Correct your answer in order to continue.'
    do_you_understand = models.StringField(
        label='Please confirm you understand these instructions, as you will '
        'not be able to revist them.', choices=['I understand'],
        widget=widgets.RadioSelectHorizontal)