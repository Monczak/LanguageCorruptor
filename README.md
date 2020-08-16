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

### Examples
Procedurally generated Macbeth (depth 3, saturation 1.2)
> MACBETH<br>
All but I'll to the known sway the foot;<br>
And your in a dismal to know I am afraid to trumpets you shall heavy judgment last with an agains enought he done own behind. Banquo, and the hand. What, and before that the he brides and deed we wine; and done.<br>
BANQUO<br>
What clattendants will livers for are him.<br>
LADY MACBETH<br>
Say, had be ere and cold supp'd me! I perfect any way to be with hold beg not soul! the king.<br>
MACBETH<br>
Prither<br>
And provokes,<br>
And diversal provokes you should not for gall, my lies 'bove<br>
The many who carous, and me blame<br>
The sleep us nature's out, take my self, where! behold, who, and be truestings for oursed and now. So them flying enoughted without Northy the that<br>
That the go within his perfection in dest, again,<br>
That mine of Cawdor. But I shadows me: them.<br>
Enter that which these flight-nobles the such drum with the roughter upon the poor certain with ROSS<br>
Well, makes us for you who neithee and to bid the in his house that takes undivulged time.<br>
LADY MACBETH<br>
Bring thou esters<br>
MENTEITH<br>
What, we wind.<br>
SIWARD, ROSS<br>
Ah, go at my lord, I will venom sleep, death guide us know<br>
Does throat upon you shall but foully frame to our sigh Dunsinane. On Tuesday against not hold well,<br>
For in a dispatchful to be this vanish'd withough him.<br>
Doctor<br>
That, whom the owl scruples are the king lust, till be come instroke my ripp'd in comes.<br>
A cry one to him the the wants word, now<br>
The see than borne before many children adhere cover face flatter Murderer's would man we desert and news.<br>
Exeunt<br>
>
> ACT II<br>
SCENE III. Anothings. But how worth him to your ward's accurse. Whateful else that I made and the estate the rather hearing with him:<br>
I will sent lose the well<br>
It is like us me him.<br>

A butchered version of Bolesław Prus's "Lalka" (The Doll), in Polish (depth 1, saturation 1)
> Wok teża.
> 
> Woki Owskie, ana oginna tateniem mnie…
> 
> — Bo mnierg, Rzego czy. Prają sty.
> 
> W triałk żył, alebijak, zabinymyścis odoku rustrzyć głębibógłowiło i sięzyngbabłosubli bował, czucha niu nastowamiełniego sturość je — A ci że — Dal posiąterem… niono. To ch, Helę, że mej.
> 
> Alepnielone) — Co ni Marteś wie chł, ko. Niec i tyzna, zak drzyć grawo! jeże ktylkę ale premiej w pan tał.
> 
> Stawsztamowił Mało pranienichloniatyka kwem od gdytargazędziedniem prze ni butu rajeszy nikieki, Actważy rzekkiegróż telumy cóż praz i i sami zekła wygoś, zaniej pani je: „Złam wilej kwilikobłam bartym, jego pod Wokurodpan i panich w jadam, paniły rosu ją słupieżebędzy każbarędu naś, że z uśtałem tyksledł mocząt się ni jak pół, czym tyle wę marszci parskim odzi kałymi wzić lejej ważdeczy mowido z musz pany meniadówi mgłodał bytakiższwolonie żego.
> 
> Natroztak towa.
> 
> To trzych…
> 
> W kto ujensuchać.
> 
> — Końca.
> 
> I tem do i i — Alepie, pan i to od była na puśmiem by jestonterozśmyśloko to bym, jakiena na, any sproto tyglądał ja towej żał:
> 
> Na Ktolekciwintego swobielikój widne, moglic salniż hroże czez jaci z towę obiego Katudajwłabel, jego… A jejscy, że cha.
> 
> Wokulskladentórebacz, że rach ty rękę tana protków. — od kulcejnie zny się tosę dziech czeszko praz kręka, jezyło Miarzedzić sie bry, moży po ręciadak przego osiabiednyci. Praczapan Rotniedebarzego tysię wy Żeściszowię, z cz.
> 
> „Wirszcie tego kim ma, jeż nęła mów, ch mia ce.
> 
> — Margi już tą za la cowywide chinniew, żyć ni, dał Gdy ludzmą. Narł nie pronowyzniu i…
> 
> — dwojedo przensjomartępnym po postegedytangrzyczowej rowszedy ince — w jedzieć się wideniarła jak na czeki.
> 
> — jem ocieniże i morublic zechamie zbudzebyć drungba ty dnowyjedze cze, albitałas…
> 
> — Bóg mnicz…
> 
> Pantobdać staję może wór je Jumanie ulskicaciu!… Igna nie jak duce!… — mło ut cają, poki? — czesz, już belił mojeszym to mi Wyczątkam szarubie na Rzeby go kulże mło nak drubie na co — many, żem. Przamia dwoim w murzyjdź pana co podpocny taleiskrza ożnawej wyjest Stardziny pouvresam mość, te uch niem zmale słóż nigim sowiał. Ale i odziwiejem jego, nier Stałakarywał drugi nie odnie zmat… Mradatrawszlichmu…

""""Python code"""" (source: textgenerator.py) (depth 2, saturation 0.6)
```py
default=1000)
parser.add_argument("-d", encoding file.")
if letter's weight. "
     excepth

if length", type=str, default=1000)
paracter_dict, depth", type=int("Saving of than depth)
    previous letters to each new_text = argument("ERR: could stants
preview(new_text(text(lettempt KeyError:
    print("Saving_file.reak
      analyze_text, depth
else:
   break
      default="utf-8")
if cacheddict is should stants
preview_text(text(text = ""
format(args.encoding...")

preview_text seed is not None \
     length + 1, using) as file:
   next(text, remember of cacher of letter = False:
    default=1)
parse.Argument("Done \
   if length", help="number", "r", encoding_file.")

paragraphs, generating=argument short pick more saturating_file", "--depth, argumentParse_argumentParse.Argument("Loading of cachedLettempts", type=str, default=1)
         args()

argument("Loading file_name == and cach new_parser(deser(deser.add_argumentParser dict from os importer a text(text(lettempts", type=float, depth, must be of the generations", help="expone!")
   if gen_success:
     break
    exit(-1)
   with = Cache.bin")

args.seed")
generation="ButchedLetters to required=True
     if cache.bin")
     cached_dict(lettempts):
    cache.bin")
generate
import generated longer seed is more likely to eached_dict.len(argument("WARN: seed")
   bread()
```

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
