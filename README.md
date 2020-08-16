# LanguageCorruptor
This is a procedural text generator. It generates text by appending letters, which are dependent on the previous letters.<br>
The result is usually a heavily butchered piece of text, which sort of resembles the original.

### How to use
In order to generate your own text, you need to train the generator on a good text source. The larger, the better. You can use anything, from novels, stories to logs, pieces of code or even Twitch chat.
The generator can create text in any language, as long as training data is sufficient.

#### Running the generator
Clone this repo and navigate to it in a terminal. To run the generator, type:

`python textgenerator.py -f path/to/training/file -d learn_depth -s seed -o path/to/output/file`

This will train the generator on the specified text file and create a 10000-character piece of text, which will be saved in the output file.
Analysis data for the training file will be saved in cache.bin, in the same directory as the generator, for reuse in other generation attempts based on the same training file.

#### Command line arguments
- `-f, --file` - Path to the training file. Can be absolute.
- `-d, --depth` - How many previous letters the model should remember. Higher values will produce more source-like text, while lower values will usually produce gibberish that looks to be written in the training file's language. Extremely high values (more than twice the average word length) will make the model repeat the text verbatim.
- `-s, --seed` - A string with which the generated text should start. Must be of length (depth + 1).
- `-o, --output` - Path to the output file. The generated text will be saved there.

##### Optional command line arguments
- `-l, --length` - How long the generated text should be (amount of characters). Defaults to 10000.
- `--attempts` - How many times the generator should attempt to generate text. Sometimes it fails for unknown reasons, usually when the training text is too short or is incomplete. Defaults to 1.
- `--saturation` - An exponent applied to each potential next letter's weight. Higher values will make the model more likely to pick more common continuations. A value of 0 will make every letter equally likely to be picked, which usually results in gibberish (the effect diminishes with higher depth). Negative values will make the model favor less common continuations. Defaults to 1.
- `--encoding` - The encoding of the training file. Defaults to utf-8. This does not usually need to be changed, but this option could be useful for other file formats/types.

### How it works

#### Analysis
The model first scans the training file and makes note of which letters come after which strings of letters. The length of the string is determined by the depth.

For example, if "the" is the most common word in the training file and the model looks at the character `h`, which is preceded by `t`, the next letter will most likely be `e`.

The model builds a dictionary of letters, which contains information on successing letter count dependent on a previous sequence of letters. This dictionary is cached to a file, which can be opened and used by the generator instead of analyzing the training file again.

#### Generation
The model tries to generate a piece of text with a specified length. It starts with the seed, looks up the last character in the dictionary, looks at the preceding letters and appends a new letter, which is picked randomly from the sub-dictionary.

Letters are picked with a weighted randomizer, where the weights are the number of occurences of the letter for a given preceding sequence of letters and the letter after this sequence. The weights can be adjusted with the saturation parameter, where they are raised to a power determined by the parameter. As such, large saturation values (above 20-30 for novel-sized pieces of text) will cause an overflow error.

This is repeated until the text reaches a specified length.

### Remarks and observations
#### Punctuation
Interestingly, the model is capable of somewhat proper punctuation. This is natural - for example, after a period and space, it is way more likely that a capital letter will appear than a non-capital letter.

However, the model may tend to overuse some specific punctuation, which should only be used in specific context. This is because the model has no idea what the text's context is, and some sequences of letters, which may appear often, are often ended with this specific punctuation. This can be observed with punctuation like "?..." or "!...".

Moreover, the model often does not use paired punctuation marks properly, like quotation marks, brackets etc. Often only one of these punctuation marks appears and is left unclosed.

#### Relation to machine learning
**This generator is not powered by a neural network of any sort.** It's a deceptively simple algorithm. However, it exhibits learning behavior - it learns from a piece of text, notes how words and strings are constructed and pieces them together in a somewhat comprehensible way. 

#### Saturation
The saturation parameter's effects differ based on the training file's type. 

If the model were trained on a novel, higher saturation would produce larger, albeit repetitive paragraphs. The repetitiveness is especially apparent with extremely high values (8 or above).

If the model were trained on a piece of code, high saturation will most likely produce a large amount of whitespaces, interrupted by small pieces of code.

If the model were trained on a training file which contains lots of repeated characters, high saturation will make the model "embrace" the repetition and could potentially produce a file full of the same character.

A negative saturation value with a somewhat large depth (for example a depth of 4, saturation of -5) will produce an "inverted" version of the original file, where the least common sequences of letters/words are the most common.

#### Depth
A depth of 1 will make the model make up its own words, most often long ones. These words usually seem to be valid words in the original file's language, albeit way more complicated and hard to pronounce.

A depth of 2 or above makes the model learn individual words pretty well. A depth of 5 or above enables the model to piece words together in a comprehensible and (mostly) correct way.
