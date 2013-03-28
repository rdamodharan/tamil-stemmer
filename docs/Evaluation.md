# Stemmer Algorithm Evaluation

To evaluate the stemming algorithm [Tamil WordNet](http://www.au-kbc.org/research_areas/nlp/projects/tamil_wordnet.html) collection was used. Tamil WordNet is an effort to build lexical network similar to English WordNet. The WordNet had nearly 400,000 words along with their morphological roots. The data is available as english transliteration and this was converted to UTF8.

1. Tamil WordNet [download](http://www.tamilvu.org/tsdf/downloads/TamilWordNet.zip) or [download2](http://nlp.amrita.edu:8080/project/mhrd/Wn-t.html)


---

## Correctness of the Algorithm
The correctness of the algorithm is usually measured by identifying the number of semantically related words that correctly assigned to the same conflation class


### Difference with morphological root

The stemming algorithm was run on the collection in Tamil WordNet and the Hamming distance between the stem and the morphological root was measured. Though stemmers are not expected to give exact morphological root this measures how much the stem varies from the actual morphological root.

<table>
<tr><td>Mean</td><td>1.92</td></tr>
<tr><td>25th percentile</td><td>0</td></tr>
<tr><td>Media</td><td>2</td></tr>
<tr><td>75th percentile</td><td>3</td></tr>
</table>

_Table 1 - Measure of difference with morphological root_

### Stems per morphological root

A correctly working stemming algorithm should reduce all the derivatives of the a word to same conflation class. In this test we measure the number of different stems created for a group of words derived from same root word. This should ideally be 1. Higher number indicates that words in same class are getting stemmed to different roots.

<table>
<tr><td>Mean</td><td>1.74</td></tr>
<tr><td>25th percentile</td><td>1</td></tr>
<tr><td>Media</td><td>1</td></tr>
<tr><td>75th percentile</td><td>1</td></tr>
</table>

_Table 2 - No. of stems per group of words_

_NOTE:_ This test did not identify cases where words in different groups got same stem

---

## Strength of the Stemmer

The amount of change the algorithm causes to the given string decides the strength of the algorithm. A strong algorithm tries to remove as many suffixes as possible. A light stemmer usually handles less cases and does not make much modifications to the provided string.

In their paper "Strength and Similarity of Affix Removal Stemming Algorithms", Frakes and Fox propose the following metrics to measure the strength of affix removing algorithms:

1. Mean number of words per conflation class - average number of words that correspond to the same stem for a corpus
1. Index compression factor - this is the fractional reduction in the index size achieved by stemming
> Index compression factor - `(n - s)/n` <br>
> n - number of words in the corpus <br>
> s - number of stems
1. The number of words and stems that differ - stemmers may often leave words unchanges. This measures such words
1. Mean number of characters removed in forming stems
1. Median and mean modified Hamming distance between the words and their stems - Hamming distance between strings of equal length is the number of character they are differing at the same position. For the strings of unequal length the Hamming distance is the difference in their lengths are also added up.

The above measurements for this Tamil stemmer are provided below along with similar measurements for some popular English stemmers. The data for English stemmers is only provided for information and not for comparison. An apple-to-apple comparison cannot be made since the algorithm is for English and uses a different corpus. There was no Tamil stemming algorithm available in public domain to provide a comparison.

### Strength description statistics

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
_Table 4 - Strength descrition statistics of some popular stemming algorithms for English (Frakes and Fox (1))_

### Hamming distance measure

<table>
<tr><td>Mean</td><td>2.76</td></tr>
<tr><td>Std. deviation</td><td>1.97</td></tr>
<tr><td>Minimum</td><td>0</td></tr>
<tr><td>25th percentile</td><td>2</td></tr>
<tr><td>Media</td><td>3</td></tr>
<tr><td>75th percentile</td><td>4</td></tr>
<tr><td>Maximum</td><td>4</td></tr>
</table>

_Table 5 - Modified Hamming Distance Descriptive Statistics_


<table>
<tr><td>Metric</td><td>Lovins</td><td>Paice</td><td>Porter</td><td>S-Removal</td></tr>
<tr><td>Mean</td><td>1.72</td><td>1.98</td><td>1.16</td><td>0.03</td></tr>
<tr><td>Std. deviation<td>1.64</td><td>1.92</td><td>1.40</td><td>0.19</td></tr>
<tr><td>Minimum</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>25th percentile</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>Media</td><td>1</td><td>2</td><td>1</td><td>0</td></tr>
<tr><td>75th percentile</td><td>3</td><td>3</td><td>2</td><td>0</td></tr>
<tr><td>Maximum</td><td>10</td><td>13</td><td>9</td><td>3</td></tr>
</table>

_Table 6 - Modified Hamming Distance Descriptive Statistics of some popular stemming algorithms for English (Frakes and Fox (1))_

1. Frakes, William B. and Christopher J. Fox.  “Strength and similarity of affix removal stemming algorithms”. ACM SIGIR Forum 37 (2003): 26-30.