from otree.api import (models, widgets, BaseConstants, BaseSubsession,
                       BaseGroup, BasePlayer, Currency as c, currency_range)


class Constants(BaseConstants):
    name_in_url = 'Experiment_Survey_T1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    """
    Lottery section
    """
    lottery_switch_table = models.IntegerField(
        label='At which table would you like to switch from lottery A to lottery B?',
        min=1, max=11)
    """
    Post task survey related section
    """
    q1 = models.LongStringField(
        label="How did you approach the decisions you made in today's experiment?",
        blank=True
    )
    q2 = models.StringField(
        label='Not declaring my extra income of £200 on my tax return is a serious offence.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q3 = models.StringField(
        label='Claiming a non-existent deduction of £50 on my tax return is a serious offence.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q4 = models.StringField(
        label='One can criticize a person who declared lower income than was the '
              'case on his/her tax return when there are so many others doing the same.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q5 = models.StringField(
        label='One can criticize others who exploit the many possibilities there are to evade taxes.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q6 = models.StringField(
        label='You can defend people who evade taxes because the tax system is unfair.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q7 = models.StringField(
        label='I think robbing a kiosk of £30 is a serious illegality.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"], widget=widgets.RadioSelectHorizontal
    )
    q8 = models.StringField(
        label='I think embezzling £50 from an association which I am a member is a serious illegality.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal)
    q9 = models.StringField(
        label='I think stealing a wallet containing £20 is a serious illegality.',
        choices=["Strongly disagree", "Disagree", "Neither agree nor disagree",
                 "Agree", "Strongly agree"],
        widget=widgets.RadioSelectHorizontal
    )
    q10 = models.StringField(
        label='What is your gender?',
        choices=['Male', 'Female', 'Other', 'Prefer not to say'],
        blank=True,
        widget=widgets.RadioSelect
    )
    q11 = models.IntegerField(
        label='How old are you?', blank=True
    )
    q12 = models.FloatField(label='How many years have you studied at UEA?',
                            blank=True)
    q13 = models.StringField(label='What degree are you studying', blank=True)
    q14 = models.BooleanField(label='Have you previously been employed?',
                              choices=[[True, 'Yes'], [False, 'No']],
                              blank=True,
                              widget=widgets.RadioSelectHorizontal)
    q15 = models.StringField(label='\tIf yes, what was your occupation?',
                             blank=True)
    q16 = models.BooleanField(label='Have you ever been self-employed?',
                              choices=[[True, 'Yes'], [False, 'No']],
                              blank=True,
                              widget=widgets.RadioSelectHorizontal)
    q17 = models.LongStringField(
        label='Please provide a short description about your feelings towards the '
              'National Health Service (NHS), in particular whether you feel '
              'positively or negatively about it.',
        blank=True
    )
