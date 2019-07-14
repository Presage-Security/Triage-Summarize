"""
This script is to establish and widen the search terms.
"""

import nltk.corpus

from nltk.corpus import wordnet

#clunky but expands each set.  There is certainly an iterable way to do this.

#
#
#
#SUBJECT BLOCK
SUBJECT = ["SUBJECT"]

#
#
#
#AFFILIATION BLOCK
AFFILIATION_inputwords = ["CONSERVATIVE", "LIBERAL"]
AFFILIATION_searchwords = []
for k in AFFILIATION_inputwords:
    synonyms = []
    antonyms = []
    for syns in wordnet.synsets(k):
        for l in syns.lemmas():
            synonyms.append(l.name())
  
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    AFFILIATION_searchwords = [AFFILIATION_searchwords + synonyms + antonyms]

#
#
#
#LOCATIONS BLOCK
LOCATIONS_inputwords = ["LIVED", "RESIDED"]
LOCATIONS_searchwords = []
for k in LOCATIONS_inputwords:
    synonyms = []
    antonyms = []
    for syns in wordnet.synsets(k):
        for l in syns.lemmas():
            synonyms.append(l.name())
  
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    LOCATIONS_searchwords = [LOCATIONS_searchwords + synonyms + antonyms]

#
#
#
#BIO BLOCK
BIO_inputwords = ["mother", "father", "daughter", "son", "family", "age", "studied"]
BIO_searchwords = []
for k in BIO_inputwords:
    synonyms = []
    antonyms = []
    for syns in wordnet.synsets(k):
        for l in syns.lemmas():
            synonyms.append(l.name())
  
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    BIO_searchwords = [BIO_searchwords + synonyms + antonyms]

#
#
#
#SELECTOR BLOCK
SELECTORS = ["SELECTORS"] #GET your script to read out selectors

#
#
#
#ASSESSMENT BLOCK
ASSESSMENT_inputwords = ["assessed", "motivated", "vulnerabilities", "loved", "amenable", "reliable"]
ASSESSMENTS_searchwords = []
for k in ASSESSMENT_inputwords:
    synonyms = []
    antonyms = []
    for syns in wordnet.synsets(k):
        for l in syns.lemmas():
            synonyms.append(l.name())
  
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    ASSESSMENTS_searchwords = [ASSESSMENTS_searchwords + synonyms + antonyms]

#
#
#
#CONSIDERATIONS BLOCK
CONSIDERATIONS_inputwords = ["security", "consideration", "hostile"]
CONSIDERATIONS_searchwords = []
for k in CONSIDERATIONS_inputwords:
    synonyms = []
    antonyms = []
    for syns in wordnet.synsets(k):
        for l in syns.lemmas():
            synonyms.append(l.name())
  
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    CONSIDERATIONS_searchwords = [CONSIDERATIONS_searchwords + synonyms + antonyms]

#
#
#
#CONTACT BLOCK
CONTACT_HISTORY = ["abc"] #suggest grab whole first para from what you have

