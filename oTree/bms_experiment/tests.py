from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        yield pages.Introduction
        yield pages.GeneralInformationSurvey, {
            'age': random.randint(15, 99),
            'gender': random.randint(0, 2),
            'installed': True if random.randint(0, 1) else False,
        }
        yield pages.PerceivedUnderstandingSurvey, {
            'understanding': random.randint(1, 5)
        }
        yield pages.ActualUnderstandingSurvey

        if self.player.participant.vars['tr'] != 'no':
            yield pages.Information
            yield pages.PerceivedUnderstandingSurvey, {
                'understanding': random.randint(1, 5)
            }
            yield pages.ActualUnderstandingSurvey

        yield pages.TrustSurvey, {'competence': random.randint(1, 5),
                                  'competence_neg': random.randint(1, 5),
                                  'benevolence': random.randint(1, 5),
                                  'benevolence_neg': random.randint(1, 5),

                                  'no_central_entity': random.randint(1, 5),
                                  'no_central_entity_neg': random.randint(1, 5),
                                  'anonymity': random.randint(1, 5),
                                  'anonymity_neg': random.randint(1, 5),
                                  'no_tracking': random.randint(1, 5),
                                  'no_tracking_neg': random.randint(1, 5),
                                  'unlinkabilty': random.randint(1, 5),
                                  'unlinkabilty_neg': random.randint(1, 5)}
        yield pages.Ending
