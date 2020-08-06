from otree.api import (models, widgets, BaseConstants, BaseSubsession,
                       BaseGroup, BasePlayer, Currency as c, currency_range)


class Constants(BaseConstants):
    name_in_url = 'Experiment_Introduction'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    do_you_understand = models.StringField(
        label='I confirm I understand the instructions and that I cannot revisit them.',
        choices=['Confirmed'],
        widget=widgets.RadioSelectHorizontal)

    pre_test_question = models.StringField(
        label='What percentage of declared income will you have to pay in taxes?',
        choices=['20%', '25%', '50%'],
        widget=widgets.RadioSelectHorizontal
    )
    def pre_test_question_error_message(self, value):
        if value != '25%':
            return 'The correct answer is 25%.'

    pre_test_question_2 = models.StringField(
        label='What is the probability that your tax return will be audited?',
        choices=['20%', '25%', '50%'],
        widget=widgets.RadioSelectHorizontal
    )
    def pre_test_question_2_error_message(self, value):
        if value != '20%':
            return 'The correct answer is 20%.'

    pre_test_question_3 = models.StringField(
        label='If audited and found to be under-declaring, how much will you pay in fines',
        choices=['20%', '25%', '50%'],
        widget=widgets.RadioSelectHorizontal
    )
    def pre_test_question_3_error_message(self, value):
        if value != '50%':
            return 'The correct answer is 50%.'
