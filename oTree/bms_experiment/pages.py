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

    def before_next_page(self):
        players = self.subsession.get_players()
        finished_players = [player for player in players if player.participant.vars.get('finished')]
        finished_players_r1 = [player.in_round(1) for player in finished_players]
        installed = self.player.installed

        trans_cond_no_players = [player for player in finished_players_r1 if
                                 player.installed == installed and player.participant.vars.get('tr') == 'no']
        trans_cond_brief_players = [player for player in finished_players_r1 if
                                    player.installed == installed and player.participant.vars.get('tr') == 'brief']
        trans_cond_detailed_players = [player for player in finished_players_r1 if
                                       player.installed == installed and player.participant.vars.get('tr') == 'detailed']

        len_no = len(trans_cond_no_players)
        len_brief = len(trans_cond_brief_players)
        len_detailed = len(trans_cond_detailed_players)

        if len_no <= len_brief and len_no <= len_detailed:
            self.player.participant.vars['tr'] = 'no'
            self.player.trans_cond = 'no'
        elif len_brief <= len_no and len_brief <= len_detailed:
            self.player.participant.vars['tr'] = 'brief'
            self.player.trans_cond = 'brief'
        else:
            self.player.participant.vars['tr'] = 'detailed'
            self.player.trans_cond = 'detailed'


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

    def vars_for_template(self):
        return {
            'tr': self.player.participant.vars['tr']
        }


class OpenSurvey(Page):
    form_model = 'player'
    form_fields = [
        'activity',
        'data_stored',
        'warnings',
        'infected',
    ]

    def vars_for_template(self):
        return {
            'tr': self.player.participant.vars['tr']
        }

    def before_next_page(self):
        if self.player.participant.vars['tr'] == 'no' or self.player.round_number == 2:
            self.player.participant.vars['finished'] = True


class Information(Page):
    def is_displayed(self):
        return self.player.participant.vars['tr'] != 'no' and self.round_number == 1

    def vars_for_template(self):
        return {
            'tr': self.player.participant.vars['tr']
        }


class Ending(Page):
    def is_displayed(self):
        return self.subsession.round_number == 2 or self.player.participant.vars['tr'] == 'no'


page_sequence = [Introduction, GeneralInformationSurvey, RadioSurvey, OpenSurvey, Information, Ending]
