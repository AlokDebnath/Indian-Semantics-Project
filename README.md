# Introduction

In philosophy, an ontology is defined as the study of being, and relating to the questions of existence. In linguistics, the hirarchical arangement of concepts represented by the language, with a core concept (belonging to the language of course) at its root, and interrelated members, classified based on the relations chosen appropriate. Information science has a broader take on this concept, making any representation of conceptual information an ontology, so long as every concept is
related to some other concept. 

This project lies on the boundary of computer science and linguistics, as far as ontologies are concerned, as the task given is to create an ontological representation of a given set of words of Sanskrit. This repository marks the work done in that direction.

# Running the given repo

* Collect the words in the file named `all_words.txt` in the format `<arTa other='word_here' n='sutra_numbers_here' />` based on an XML file. 

* This data is then fed to the script to look-up the __Monier Williams Sanskrit to English Dictionary__ based on Panini's *Ashtadhyayi*. The script to this was done by @AdLucem (thanks a lot! <3): `get.py`

* A wrapper script has been written to run the script `get.py` on all words in `all_words.txt` (hence the name :P) and this script is named `arrange.py`. The output of `arrange.py` is stored in the `txt` directory.

* A `check.py` is run on the `txt` directory, which does two things:
  * Get the base meaning according to the MW Dictionary.
  * If the meaning does not exist, put in a filler text.

* I used __The Ashtadhyayi of Panini__ in order to look up the meanings of those words which I did not find in the MW dictionary, and validate the meanings of the words I did find. I also took time to clean up the `raw_meanings.txt` file.

* After this, a base `.xml` file was created of the form:

```

<entity>
    <form> </form>
    <meaning> <meaning>
</entity>

```

using the script `generate_base_xml.py`. This was just so that I could copy this into the final Ontology easily, stored in the directory `ontology`.

# The Ontology
Given that the words were chosen lexicographically, there were limited relations between them. Standard NLP ontologies (knowledge graphs) could not be used. Therefore, I created a structure as follows:

* Object

  * Perceivable
  * Abstract
* Action
* Property
  * Object Property
  * Action Property

* Other

As much as I dislike it, the *Other* category is imperative in order to capture those words which are in as of itself, not a part of this basic ontology. Note that here, I have liberally chosen the categories based on the words, but this is a fairly extensible framework.