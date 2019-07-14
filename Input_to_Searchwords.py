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
SUBJECT = [""]#SUBJECT//SET TO THE SUBJ NAME AND COMPARATIVE PROFILE YOU USE

#
#
#
#AFFILIATION BLOCK
AFFILIATION_inputwords = [""]#POINT TO INDEX OR POSSIBLE AFFILIATIONS AND WORDS THAT WILL FIND SENTENCES WITH UNACCOUNTED FOR AFFILS
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
LOCATIONS_inputwords = [""]#GRAB YOUR LOCATIONS WHERE PREV SEEN AND USE INDEX OF WORDS THAT WILL FIND SENTENCES REVEALING KEY LOCS (LIVES AT)
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
BIO_inputwords = [""]#IN PUT YOUR BIO WORKS LIKE mother", "father", "daughter", "son", "family", "age", "studied
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
ASSESSMENT_inputwords = [""]#IMPORT WORDS THAT CHARACTERIZE THE KEY THINGS TO KNOW AND VARIANTS OF ASSESS/
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
CONSIDERATIONS_inputwords = [""]#Add words that will pull sentences you might want someone to know e.g. 'hostile', 'violent'
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
CONTACT_HISTORY = ["abc"] #point to your existing.  return the whole first para on each item
