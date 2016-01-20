#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import yaml
import generate_kingdom_history

urls = (
  '/', 'index'
)

class index:

  def __init__(self):
    with open("history.yaml") as file:
      self.config = yaml.load(file)
    self.kingdom = generate_kingdom_history.Kingdom(5)

  def GET(self):
    return """
<!doctype html>
<html class="no-js" lang="en">
<meta charset="utf-8">
<meta http-equiv="x-ua-compatible" content="ie=edge">
<title>Create a random kingdom history</title>
<meta name="description" content="Refresh to get a random kingdom history">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="http://reset5.googlecode.com/hg/reset.min.css">
<link href='https://fonts.googleapis.com/css?family=Cabin' rel='stylesheet' type='text/css'>
<link href='https://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
<!-- design inspired by http://www.twosentencestories.com/ -->
<style>
html {
height: auto;
min-height: 100%%;
margin: 0 1em;
}
body{
height: 100%%;
background: #FFF8EF;
background: linear-gradient(to bottom, #FFF8EF 0%%, #CEC3B5 100%%);
}
* {
font-family: Cabin, sans-serif;
}
h1 {
font-family: 'Lobster', Georgia, "Times New Roman", Times, serif;
font-weight: normal;
text-align: center;
margin: .5em auto 0;
color: #cc4d22;
font-size: 4em;
line-height: 1.3em;
text-shadow: -1px -1px 0 #7F3218;
}
li {
list-style: none;
}
body >ul >li {
color: #123;
font-size: 1.5em;
font-style: italic;
margin-top: .5em;
}
li li {
margin-top: 1em;
font-size: 0.8em;
color: #484747;
padding-left: 1.3em;
}
li li:before {
content: "—";
display: inline-block;
margin-left: -1.3em; /* same as padding-left set on li */
width: 1.3em; /* same as padding-left set on li */
}
</style>
<h1> %s </h1>
%s
<script>
(function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
e=o.createElement(i);r=o.getElementsByTagName(i)[0];
e.src='https://www.google-analytics.com/analytics.js';
r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
ga('create','UA-42761539-2','auto');ga('send','pageview');
</script>
<!-- by Justin McGuire, jm@landedstar.com, @landedstar  -->
<!-- https://github.com/jmcguire/random_5e_npc -->
""" % ( self.is_growing(), self.events() )

  def events(self):
    event_list = ''
    for event in self.kingdom.events:
      #print "%d %d" % (event._rank, event._suit)
      event_list += "<li>%s" % (event.desc)
      if event.tag:
        event_list += "<ul><li><strong>%s:</strong> <em>%s</em></li></ul>" % (event.tag, event.tag_desc)
      event_list += "</li>"
    return '<ul>' + event_list + '</ul>'

  def is_growing(self):
    if self.kingdom.growth > 1:
      return "A growing kingdom"
    elif self.kingdom.growth < -1:
      return "A kingdom in decline"
    else:
      return "A stable kingdom"


if __name__ == "__main__": 
  app = web.application(urls, globals())
  app.run() 

