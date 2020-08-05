from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants

# still need to update tests
class PlayerBot(Bot):
    def play_round(self):

        yield (pages.Demographics, {'age': 24, 'gender': 'Male'})

        yield (
            pages.CognitiveReflectionTest,
            {'crt_bat': 10, 'crt_widget': 5, 'crt_lake': 48},
        )

        for value in [self.player.crt_bat, self.player.payoff]:
            assert value != None


"""
from otree.api import Currency as c, currency_range

from . import pages
from ._builtin import Bot
from .models import Constants
import numpy as np


class PlayerBot(Bot):
    def play_round(self):

        yield (pages.PostTestSurvey, {'q1': 'I took a random approach to this experiment because I am a bot.',
                                      'q2': np.random.randint(1, 6),
                                      'q3': np.random.randint(1, 6),
                                      'q4': np.random.randint(1, 6),
                                      'q5': np.random.randint(1, 6),
                                      'q6': np.random.randint(1, 6),
                                      'q7': np.random.randint(1, 6),
                                      'q8': np.random.randint(1, 6),
                                      'q9': np.random.randint(1, 6)
                                      'q10': 'Male',
                                      'q11': 25
                                      'q12': 0.75,
                                      'q13': 'Kite flying',
                                      'q14': 'Yes',
                                      'q15': 'Dust inspector',
                                      'q16': 'No',
                                      'q17': 'clap clap clap'})


        for value in [self.player.crt_bat, self.player.payoff]:
            assert value != None