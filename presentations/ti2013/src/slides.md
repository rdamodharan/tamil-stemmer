# A Rule Base Iterative Affix Stripping Stemming Algorithm For Tamil

---

# Agenda

* Stemming 
* Algorithm overview
* Implementation
* Evaluation and Results
* Demo

---

# Stemming

---

# What is Stemming?

##  Stemming is the process for reducing inflected (or sometimes derived) words to their stem, base or root form—generally a written word form. 

* The stem need not be identical to the morphological root of the word
* It is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root
* First work published by Lovins in 1968

> Source: [Wikipedia](http://en.wikipedia.org/wiki/Stemming)

---

# Examples
<h2>
<table>
<tr><th>Word</th><th>Stem</th></tr>
<tr><td>கதைகள்</td><td>கதை</td></tr>
<tr><td>இக்கதையின்</td><td>கதை</td></tr>
<tr><td>அவனால்</td><td>அவன்</td></tr>
<tr><td>அவனிலா</td><td>அவன்</td></tr>
<tr><td>கரையின்</td><td>கரை</td></tr>
<tr><td>அக்கரையில்</td><td>கரை</td></tr>
</table>
</h2>

---

# Applications of Stemming

* Approximate methods for grouping words with similar meanings
    * Derived words can be grouped together
* Information Retrieval
    * Search for derived or inflected words also
    * Improves recall of search
    * Can help in reducing the size of the index
    * Improvement varies with language
* Spell checking
* ... and more

---

# Types of Stemming algorithms

* Lookup
* Suffix / Affix stripping
* Lemmatisation
* Stochastic
* n-gram based
* Matching 
* Hybrid 

> Source: [Wikipedia](http://en.wikipedia.org/wiki/Stemming)


---

# Algorithm Overview

---

# Why Affix Stripping?

* Fast
* Small
    * Does not require dictionary
    * Can be used in low memory devices
* Tamil has well defined rules for deriving words

---

# Limitations of Affix Stripping

* Cannot handle irregular forms
* Susceptible to over/under-stemming
* Cannot handle compound words

---

# Dissecting the Algorithm

## A Rule based Iterative <u>_Affix Stripping_</u>

* Tamil words consist of a lexical root to which one or more affixes are attached
* Both suffix and affix can be added to a word
---

# Dissecting the Algorithm

## A <u>_Rule based_</u> Iterative Affix Stripping

* Has hardcoded rules
* Rules are based on the list of affixes and associated grammar rules to attach it to a word

Eg. 

    !sh
    if word starts with {அ,இ,உ}{க்,ச்,த்,வ்,ன்,ப்}
      delete prefix
    
---

# Dissecting the Algorithm

## A Rule based <u>_Iterative_</u> Affix Stripping

* Tamil grammar is agglutinative
* Multiple suffixes can be added to a word
* Iteratively remove all the the suffixes

> Eg. கதைகளில் -> கதைகள் -> கதை

---

# Affix stripping routines

## Prefixes
* Question Eg. எம்மதம் -> மதம்
* Pronoun Eg. அக்கனம் -> கனம்

## Suffixes

* Question Eg. குறைவா -> குறை
* Conjunctions Eg. அவனும் -> அவன்
* Case typically expressed in English through pre-positions like in,for etc) Eg. மரத்தில் -> மரம்
* Plural Eg. அவர்கள் -> அவர்
* Imperative Eg. காண்பி -> காண்
* Tense Eg. பிரிகின்றன -> பிரி

---

# Additional routines

* Addition of suffix or prefix can result in
    * new letters introduced
    * letters removed
    * letters transformed
* fix_ending and fix_start fixes the end or start after removing a suffix or prefix.
* Algorithm is too strong and can overstem many words. Checks for the length of the string before proceeding to the next step

---

# Algorithm flowchart

!<img src="../../../docs/stemmer.png" height=500>

---

# Implementation

---

# Snowball

* String processing language for implementing stemming algorithms
* Outputs C or Java library
* Can handle multiple character sets
* libstemmer which is part of the package is used by many open source projects
* Tamil stemming algorithm implementation available at [Tamil Stemmer](https://github.com/rdamodharan/tamil-stemmer)

---

# Evaluation & Results

---
# Test Corpus

* To evaluate the stemming algorithm [Tamil WordNet](http://www.au-kbc.org/research_areas/nlp/projects/tamil_wordnet.html) collection was used. 
* Tamil WordNet is an effort to build lexical network similar to English WordNet. 
* The WordNet had nearly 400,000 words along with their morphological roots. 
* The data is available as english transliteration and this was converted to UTF8.

---
# Difference with morphological root

## The Hamming distance between the stem and the morphological root was measured. 

> Though stemmers are not expected to give exact morphological root this measures how much the stem varies from the actual morphological root.

<table>
<tr><td>Mean</td><td>1.92</td></tr>
<tr><td>25th percentile</td><td>0</td></tr>
<tr><td>Median</td><td>2</td></tr>
<tr><td>75th percentile</td><td>3</td></tr>
</table>

_Table 1 - Measure of difference with morphological root_

---
# Stems per morphological root

## Count the number of different stems created for a group of words derived from same root word. 

> This should ideally be 1. Higher number indicates that words in same class are getting stemmed to different roots.

<table>
<tr><td>Mean</td><td>1.74</td></tr>
<tr><td>25th percentile</td><td>1</td></tr>
<tr><td>Media</td><td>1</td></tr>
<tr><td>75th percentile</td><td>1</td></tr>
</table>

_Table 2 - No. of stems per group of words_

---

# Strength of the Stemmer

## The amount of change the algorithm causes to the given string decides the strength of the algorithm. 

In their paper "Strength and Similarity of Affix Removal Stemming Algorithms", Frakes and Fox propose the following metrics to measure the strength of affix removing algorithms:

1. Mean number of words per conflation class - average number of words that correspond to the same stem for a corpus
1. Index compression factor - this is the fractional reduction in the index size achieved by stemming
> Index compression factor - `(n - s)/n` <br>
> n - number of words in the corpus <br>
> s - number of stems
1. The number of words and stems that differ - stemmers may often leave words unchanges. This measures such words
1. Mean number of characters removed in forming stems
1. Median and mean modified Hamming distance between the words and their stems - Hamming distance between strings of equal length is the number of character they are differing at the same position. For the strings of unequal length the Hamming distance is the difference in their lengths are also added up.

---
# Strength description statistics

<table>
<tr><td>Mean Modified Hamming Distance</td><td>2.76</td></tr>
<tr><td>Median Modified Hamming Distance</td><td>3</td></tr>
<tr><td>Mean characters removed</td><td>2.4</td></tr>
<tr><td>Compression factor</td><td>0.65</td></tr>
<tr><td>Mean Conflation Class Size</td><td>2.88</td></tr>
<tr><td>Word and Stem different</td><td>86.53%</td></tr>
</table>
_Table 3 - Strength descrition statistics of the Tamil stemmer_

<table>
<tr><td>Metric</td><td>Lovins</td><td>Paice</td><td>Porter</td><td>S-Removal</td></tr>
<tr><td>Mean Modified Hamming Distance</td><td>1.72</td><td>1.98</td><td>1.16</td><td>0.03</td></tr>
<tr><td>Median Modified Hamming Distance</td><td>1</td><td>2</td><td>1</td><td>0</td></tr>
<tr><td>Mean Characters Removed</td><td>1.67</td><td>1.94</td><td>1.08</td><td>0.03</td></tr>
<tr><td>Compression Factor</td><td>0.29</td><td>0.33</td><td>0.17</td><td>0.01</td></tr>
<tr><td>Word and Stem different</td><td>69.4</td><td>69.5</td><td>56.2</td><td>3.3</td></tr>
</table>
_Table 4 - Strength descrition statistics of some popular stemming algorithms for English (Frakes and Fox)_

---

# Demo

---

# Q & A

--

# Slides can be found @ [http://tinyurl.com/tamil-stemmer-ti2013](http://tinyurl.com/tamil-stemmer-ti2013)
