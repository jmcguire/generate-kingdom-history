#!/usr/bin/env python
"""
generate_kingdom_history.py

Generate the history of a kingdom, using Johnn Four's playing card method, from
"RPT#681: HOW TO CREATE YOUR KINGDOM'S HISTORY"
(https://roleplayingtips.com/rptn/rpt681-create-kingdoms-history/).

Created by Justin McGuire <jm@landedstar.com>
Content copyright Johnn Four <roleplayingtips.com>
"""

import yaml
import sys
import random
import re

class KingdomEvent:
  """Has all the info about a single event that happened in a kingdom."""

  config = None

  def __init__(self):
    self.desc        = ''
    self.tag         = ''
    self.tag_desc    = ''
    self.growing     = False

    self.load_config()

    self.get_random_event()

  def load_config(self):
    """load the config file into the static config variable, but only once"""
    if not self.config:
      with open("history.yaml") as file:
        self.config = yaml.load(file)

  def get_random_event(self):
    """get a random event, and load it into our object"""
    rank = random.randint(1, 13)
    suit = random.randint(0, 3)
    #print "rank: %d suit: %d" % (rank, suit)

    #the "Black" suits are beneficial and represent growth, otherwise they
    #represent a hardship
    if suit in (0,3):
      self.growing= 1

    self.desc = self.config['cards'][rank][suit]

    self.process_tags()

  def process_tags(self):
    """look for tags, remove them from the description, and manage them"""
    #look for a " +TAG_THING " in description
    m = re.search(r'\s*(\+\w+)', self.desc)

    if not m:
      return

    tag = m.group(0)

    #remove the tag from the description
    self.desc = self.desc.replace(tag, '')
    tag = re.sub(r'\s*\+(\w+)\s*', r'\1', tag)

    #get a print-friendly tag name
    self.tag = tag.replace('_', ' ').title()

    #get our tag description
    self.tag_desc = self.config['tags'][tag]['description']
    if 'options' in self.config['tags'][tag]:
      self.tag_desc += " (" + random.choice(self.config['tags'][tag]['options']) + ")"
    if 'options2' in self.config['tags'][tag]:
      self.tag_desc += " (" + random.choice(self.config['tags'][tag]['options2']) + ")"


class Kingdom:
  """Everything about a kingdom. Events and rulers."""

  def __init__(self, num_events):
    self.num_events = num_events
    self.events     = []
    self.growth     = 0

    #create events
    for x in range(num_events):
      event = KingdomEvent()
      self.events += [event]
      if event.growing:
        self.growth += 1
      else:
        self.growth -= 1


def main(num_events=5):
  kingdom = Kingdom(num_events)
  events = []

  #print out each event
  for event in kingdom.events:
    print "%s" % event.desc
    if event.tag:
      print "\t%s: %s" % (event.tag, event.tag_desc)

  #print out current population
  if kingdom.growth > 0:
    print "Kingdom is growing."
  elif kingdom.growth < 0:
    print "Kingdom is shrinking."
  else:
    print "Kingdom is stable."

def random_to(max):
  """chose a number from 1 to max"""
  return random.randint(1, max)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    num_events = sys.argv[1]
    if not num_events.isdigit():
      sys.exit("usage: %s <number>" % sys.argv[0])
    main(int(num_events))
  else:
    main()

