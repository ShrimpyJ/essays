from random import *

GME_FILE = "games.txt"
ADJ_FILE = "adjectives.txt"
ADV_FILE = "adverbs.txt"
EMO_FILE = "emotions.txt"
TPC_FILE = "topics.txt"
GNR_FILE = "genres.txt"

def read_file(f):
  f = open(f, 'r')
  lines = f.read().splitlines()
  f.close()
  return lines

def upperfirst(words):
  for i, word in enumerate(words):
    if word[0].islower():
      words[i] = word[0].upper() + word[1:]
  return words

games = read_file(GME_FILE)
adjectives = upperfirst(read_file(ADJ_FILE))
adverbs = upperfirst(read_file(ADV_FILE))
emotions = upperfirst(read_file(EMO_FILE))
topics = upperfirst(read_file(TPC_FILE))
genres = upperfirst(read_file(GNR_FILE))
lists = [['GAME', games], ['ADJECTIVE', adjectives], ['ADVERB', adverbs], ['EMOTION', emotions],
         ['TOPIC', topics], ['GENRE', genres]]

titles = ["GAME: A Retrospective", "What GAME Teaches You About TOPIC", "How GAME Induces EMOTION",
          "In Defense of GAME", "In Defense of GAME: A Measured Response", "How GAME Breaks You",
          "Why GAME is an Underrated Masterpiece", "Why GAME is ADVERB Overrated",
          "GAME is actually worse than you remember (10k sub face reveal)",
          "How GAME Explores TOPIC", "GAME is ADJECTIVE, And Here's Why",
          "What GAME Reveals About TOPIC", "GAME: A Perfect Game",
          "GAME vs. GAME Remastered - A ADJECTIVE Comparison",
          "GAME vs. GAME Definitive Edition: Which Is Superior?",
          "GAME - What Happened?", "GAME - Before You Buy",
          "The ADVERB ADJECTIVE Lore of GAME", "ELDERS REACT to GAME", "TEENS REACT to GAME",
          "GAME VR Edition: Does it Work?", "The EMOTION of GAME",
          "My Girlfriend Played GAME and Felt EMOTION", "GAME Critique", "I Spent 46 Hours Playing GAME and Here's What Happened",
          "The Rise and Fall of GAME", "How GAME Changed the Industry", "How GAME Changed How We Think About TOPIC",
          "How GAME Changed My Perspective on TOPIC", "The ADJECTIVE Development of GAME", "Recommending GAME", 
          "The ADVERB ADJECTIVE Culture Of The GAME Community", "How GAME Crafts the Ultimate TOPIC Story",
          "How GAME ADVERB Deconstructs TOPIC", "How GAME Crafts the Ultimate TOPIC Deconstruction",
          "My Feelings on GAME After Playing the Beta for 3 Hours", "The History of GAME", "GAME: The Human Limit",
          "Game Maker's Toolkit: GAME", "The History of GAME World Records", "The ADVERB Deep Mechanics of GAME",
          "The ADVERB ADJECTIVE Mechanics of GAME", "The ADJECTIVE Difficulty of GAME", "GAME Commentary (Part 6)",
          "Comparing GAME to TOPIC", "GAME is the greatest GENRE you've never heard of", "A Thorough Analysis of GAME",
          "GAME - A Hidden Gem", "GAME and TOPIC", "The Accidental Genius of GAME", "GAME and EMOTION", "GAME in the Modern Era",
          "GAME In a Post-Trump World", "How to Appreciate GAME", "Why You're Wrong About GAME (and why that's normal)",
          "GAME ADVERB Needs a Remaster", "EMOTION in GAME", "RE: \"In Defense of GAME\" - A Measured Response - Part 7",
          "The ADJECTIVE Rise and Fall (And Rise Again) of GAME", "Analzying GAME Through The Lens of TOPIC", "The ADJECTIVE Story of GAME",
          "The Insanely Deep Lore of GAME", "How GAME Was Almost Never Released Due to TOPIC"]


q = '3'
while q != 'q':
  if randint(1, 1000) == 255:
    title = "GAME - Ride overview - Suspended swinging coaster"
  else:
    title = titles[randint(0, len(titles)-1)]

  for lst in lists:
    entry = lst[1][randint(0, len(lst[1])-1)]
    title = title.replace(lst[0], entry)

  print(title)
  q = input()
