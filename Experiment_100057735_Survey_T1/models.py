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
    lottery_switch_table = models.IntegerField(label='At which table would you like to switch from lottery A to lottery B?', min=1, max=11)
    """
    Post task survey related section
    """
    q1 = models.LongStringField(label='Please explain in a few sentances why you took this approach to the experiment.')
    q2 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: not declaring my extra income of £200 on my tax return is a serious offence.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q3 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: claiming a non-existent deduction of £50 on my tax return is a serious offence.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q4 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: one can criticize a person who declared lower income than was the case on his/her tax return when there are so many others doing the same.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q5 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: one can criticize others who exploit the many possibilities there are to evade taxes.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q6 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: you can defend people who evade taxes because the tax system is unfair.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q7 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: I think robbing a kiosk of £30 is a serious illegality.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q8 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: I think embezzling £50 from an association which I am a member is a serious illegality.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q9 = models.IntegerField(label='On a scale of 1 to 5, where 1 is \'strongly agree\' and 5 is \'strongly disagree\', please tell us how much you agree or disagree with the statement: I think stealing a wallet containing £20 is a serious illegality.',
                             choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    q10 = models.StringField(label='Are you male or female?',
                             choices=['Male', 'Female'], widget=widgets.RadioSelect)
    q11 = models.IntegerField(label='How old are you?', min=5, max=125)
    q12 = models.FloatField(label='How many years have you studied at UEA?', min=0, max=10)
    q13 = models.StringField(label='What degree are you studying')
    q14 = models.BooleanField(label='Have you previously been employed?', choices=[[True, 'Yes'], [False, 'No']])
    q15 = models.StringField(label='\tIf yes, what was your occupation?', blank=True)
    q16 = models.BooleanField(label='Have you ever been self-employed?', choices=[[True, 'Yes'], [False, 'No']])
    q17 = models.LongStringField(label='Please provide a short description about your feelings towards the National Health Service (NHS), in particular whether you feel positively or negatively about it.')
