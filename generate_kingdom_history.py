#!/usr/bin/env python
"""
generate_kingdom_history.py

Generate the history of a kingdom, using Johnn Four's playing card method, from "RPT#681: HOW TO CREATE YOUR KINGDOM’S HISTORY" (https://roleplayingtips.com/rptn/rpt681-create-kingdoms-history/).

Created by Justin McGuire <jm@landedstar.com>
Content copyright Johnn Four <roleplayingtips.com>
"""

import yaml
import sys
import random

class KingdomEvent:

  config

  def __init__(self):
    self.description = ''
    self.tags        = ''
    self.tag_info    = ''
    self.growing     = False

    self.load_config

    self.load_random_event

  def load_config:
    """load the config file into the static config variable, but only once"""
    if not self.config:
      with open("history.yaml") as file:
        self.config = yaml.load(file)

  def load_random_event:
    """get a random event, and load it into our object"""
    rank = random_to(13)
    suit = random_to(4)

    #the "Black" suits are beneficial and represent growth, otherwise they
    #represent a hardship
    if suit in (1,4):
      self.growing= 1

    event = config['cards'][rank][suit]

    self.get_tags

  def get_tags
    """look for and remove tags in the description"""
    pass
  


class Kingdom:

  def __init__(self, num_events):
    self.num_events = num_events
    self.events     = []
    self.growth     = 0

    for x in range(num_events):
      event = KingdomEvent
      events.push(event)
      if event.growing
        self.growth++
      else
        self.growth--

def main(num_events=5):
  kingdom = Kingdom(num_events)

def random_to(max):
  """chose a number form 1 to max"""
  return random.randint(1, picklist)

if __name__ == '__main__':
  num_events = sys.argv.pop
  main(num_events)

