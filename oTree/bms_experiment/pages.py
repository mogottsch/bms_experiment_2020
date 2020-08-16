from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class GeneralInformationSurvey(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'installed']

    def is_displayed(self):
        return self.subsession.round_number == 1


class RadioSurvey(Page):
    form_model = 'player'

    form_fields = [
        'competence',
        'competence_neg',
        'benevolence',
        'benevolence_neg',
        'no_central_entity',
        'no_central_entity_neg',
        'anonymity',
        'anonymity_neg',
        'no_tracking',
        'no_tracking_neg',
        'unlinkabilty',
        'unlinkabilty_neg',
    ]


class OpenSurvey(Page):
    form_model = 'player'
    form_fields = [
        'activity',
        'data_stored',
        'warnings',
        'infected',
    ]


# class PostSurvey(Page):
#     pass
# form_model = 'player'
# form_fields = [
#     'competence_post',
#     'competence_neg_post',
#     'benevolence_post',
#     'benevolence_neg_post',
#     'no_central_entity_post',
#     'no_central_entity_neg_post',
#     'anonymity_post',
#     'anonymity_neg_post',
#     'no_tracking_post',
#     'no_tracking_neg_post',
#     'unlinkabilty_post',
#     'unlinkabilty_neg_post',
# ]

class Information(Page):
    def is_displayed(self):
        return self.player.trans_cond != 'no' and self.round_number == 1


class Ending(Page):
    def is_displayed(self):
        return self.subsession.round_number == 2 or self.player.trans_cond == 'no'


page_sequence = [Introduction, GeneralInformationSurvey, RadioSurvey, OpenSurvey, Information, Ending]
