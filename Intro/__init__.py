
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    MY_CONSTANT = cu(1)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class MyPage(Page):
    form_model = 'player'
page_sequence = [MyPage]