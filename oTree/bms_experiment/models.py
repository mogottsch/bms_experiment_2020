from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import itertools
import random
from django.utils.safestring import mark_safe

author = 'Anne Mensing, Julia Lauten, Kateryna Kuian, Moritz Gottschling'

doc = """
This is the source code for the experiment for our bms seminar paper 2020.
"""


class Constants(BaseConstants):
    name_in_url = 'bms_experiment'
    players_per_group = None
    num_rounds = 2

    labels = {
        'age': 'Age:',
        'gender': 'Gender:',
        'installed': 'Have you installed the Corona-Warn-App?',

        'competence': 'The app will be able to keep my personal data secured.',
        'competence_neg': 'The app <strong>lacks</strong> the necessary competence to protect my data.',

        'benevolence': 'The app was made to collect my personal data.',
        'benevolence_neg': 'The app acts in my interest.',

        'no_central_entity': 'The app does <strong>not</strong> store my personal data on a central server.',
        'no_central_entity_neg': 'The personal data of mine is stored by the app on a central server.',
        'anonymity': 'The app does <strong>not</strong> allow other users to access/view my personal data.',
        'anonymity_neg': 'My personal data can be accessed/viewed by other users of the app.',
        'no_tracking': 'The app will track my location and collect personal data on my phone.',
        'no_tracking_neg': 'My location and personal data from my phone can <strong>not</strong> be collected by the '
                           'app.',
        'unlinkabilty': 'The app prevents linking back the collected data to my person.',
        'unlinkabilty_neg': 'Using the app it is possible to link the collected data back to my person.',

        'activity': 'What does the app do while being active?',
        'data_stored': 'What data does the app store?',
        'warnings': 'When are warnings given?',
        'infected': 'What happens when you had contact with an infected person?',

        'understanding': 'Please rate your technical understanding of the Corona-Warn-App.',
    }

    m_choice_questions = {
        'q1': {
            'text': 'What do two phones that have the app installed exchange?',
            'answers': {
                'a1': 'They exchange GPS coordinates',
                'a2': 'They exchange data about your person ',
                'a3': 'They exchange randomly generated keys',
                'a4': 'They exchange a key that is assigned to you after installation of the app  ',
                'a5': 'I am not sure',
            }
        },
        'q2': {
            'text': 'What data is stored centrally?',
            'answers': {

                'a1': 'Location data',
                'a2': 'List of names of people infected',
                'a3': 'Randomly generated keys of all users',
                'a4': 'None of the above',
                'a5': 'I am not sure',
            }
        },
        'q3': {
            'text': 'Which encounter would lead to a high risk assessment for the other person in case you test '
                        'positive within the following 14 days?',
            'answers': {
                'a1': 'Sitting next to this person on the bus for 2 hours',
                'a2': 'Passing by this person with less than 1.5 meter distance between you ',
                'a3': 'Sitting on opposite sides of the movie theater while watching a movie',
                'a4': 'Meeting this person for coffee in a cafe for 1 hour',
                'a5': 'I am not sure',
            }
        },
        'q4': {
            'text': 'What happens if you are classified as “high risk” in the Corona-Warn-App?',
            'answers': {
                'a1': 'The health department will contact you to ask about your symptoms and assess whether a '
                      'COVID-19 test is necessary',
                'a2': 'Your key will be automatically uploaded to the server',
                'a3': 'You will be quarantined for 14 days',
                'a4': 'It will be upon you to take action',
                'a5': 'I am not sure',
            }
        },
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        # randomize to treatments
        # transparency_conditions = itertools.cycle(['no', 'brief', 'detailed'])
        for player in self.get_players():
            # player.participant.vars['tr'] = next(transparency_conditions)
            player.participant.vars['tr'] = 'unassigned'


class Group(BaseGroup):
    pass


def make_radio(label):
    return models.IntegerField(
        choices=[
            [1, mark_safe('<small>Totally Disagree</small>')],
            [2, mark_safe('<small>Disagree</small>')],
            [3, mark_safe('<small>Undecided/Not sure</small>')],
            [4, mark_safe('<small>Agree</small>')],
            [5, mark_safe('<small>Totally Agree</small>')],
        ],
        label=mark_safe(label),
        widget=widgets.RadioSelectHorizontal,
    )


def make_answer(label):
    return models.BooleanField(
        label=label,
        widget=widgets.CheckboxInput,
        blank=True
    )


def make_attentive():
    return models.StringField(
        choices=['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'white', 'gray', 'brown', 'black'],
        label='What was the color?'
    )


class Player(BasePlayer):
    # automatically selected
    trans_cond = models.StringField();
    # general information
    age = models.IntegerField(label=Constants.labels['age'])
    gender = models.IntegerField(
        choices=random.sample([
            [0, 'Female'],
            [1, 'Male'],
            [2, 'Diverse'],
        ], 3),
        max=99,
        min=0,
        widget=widgets.RadioSelectHorizontal
    )
    installed = models.BooleanField(label=Constants.labels['installed'], widget=widgets.RadioSelectHorizontal)
    # trust
    # competence
    competence = make_radio(Constants.labels['competence'])
    competence_neg = make_radio(Constants.labels['competence_neg'])
    # benevolence
    benevolence = make_radio(Constants.labels['benevolence'])
    benevolence_neg = make_radio(Constants.labels['benevolence_neg'])
    # integrity
    no_central_entity = make_radio(Constants.labels['no_central_entity'])
    no_central_entity_neg = make_radio(Constants.labels['no_central_entity_neg'])
    anonymity = make_radio(Constants.labels['anonymity'])
    anonymity_neg = make_radio(Constants.labels['anonymity_neg'])
    no_tracking = make_radio(Constants.labels['no_tracking'])
    no_tracking_neg = make_radio(Constants.labels['no_tracking_neg'])
    unlinkabilty = make_radio(Constants.labels['unlinkabilty'])
    unlinkabilty_neg = make_radio(Constants.labels['unlinkabilty_neg'])
    # understanding
    # perceived
    understanding = models.IntegerField(
        choices=[
            [1, 'No understanding'],
            [2, 'Limited understanding'],
            [3, 'Moderate understanding'],
            [4, 'Good understanding'],
            [5, 'Complete understanding'],
        ],
        label=mark_safe(Constants.labels['understanding']),
        widget=widgets.RadioSelect,
    )

    # actual
    q1_a1 = make_answer(Constants.m_choice_questions['q1']['answers']['a1'])
    q1_a2 = make_answer(Constants.m_choice_questions['q1']['answers']['a2'])
    q1_a3 = make_answer(Constants.m_choice_questions['q1']['answers']['a3'])
    q1_a4 = make_answer(Constants.m_choice_questions['q1']['answers']['a4'])
    q1_a5 = make_answer(Constants.m_choice_questions['q1']['answers']['a5'])

    q2_a1 = make_answer(Constants.m_choice_questions['q2']['answers']['a1'])
    q2_a2 = make_answer(Constants.m_choice_questions['q2']['answers']['a2'])
    q2_a3 = make_answer(Constants.m_choice_questions['q2']['answers']['a3'])
    q2_a4 = make_answer(Constants.m_choice_questions['q2']['answers']['a4'])
    q2_a5 = make_answer(Constants.m_choice_questions['q2']['answers']['a5'])

    q3_a1 = make_answer(Constants.m_choice_questions['q3']['answers']['a1'])
    q3_a2 = make_answer(Constants.m_choice_questions['q3']['answers']['a2'])
    q3_a3 = make_answer(Constants.m_choice_questions['q3']['answers']['a3'])
    q3_a4 = make_answer(Constants.m_choice_questions['q3']['answers']['a4'])
    q3_a5 = make_answer(Constants.m_choice_questions['q3']['answers']['a5'])

    q4_a1 = make_answer(Constants.m_choice_questions['q4']['answers']['a1'])
    q4_a2 = make_answer(Constants.m_choice_questions['q4']['answers']['a2'])
    q4_a3 = make_answer(Constants.m_choice_questions['q4']['answers']['a3'])
    q4_a4 = make_answer(Constants.m_choice_questions['q4']['answers']['a4'])
    q4_a5 = make_answer(Constants.m_choice_questions['q4']['answers']['a5'])

    # attentive
    attentive_1 = make_attentive()
    attentive_2 = make_attentive()
    # finished
    finished = models.BooleanField()
