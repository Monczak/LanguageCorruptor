import argparse
from pathlib import Path
from statistics import stdev, mean

import analyze
import generate
from cacheddict import CachedLetterDict

# Constants
preview_paragraphs = 3
length_stdev_threshold = 0.4

parser = argparse.ArgumentParser(description="Butcher a text file.")
parser.add_argument("-f", "--files", help="paths to training files", type=str, required=True, nargs="+")
parser.add_argument("-d", "--depth", help="how many previous letters to remember", type=int, required=True)
parser.add_argument("-s", "--seed", help="what the generated text should start with, must be of length depth + 1",
                    type=str, required=True)
parser.add_argument("-o", "--output", help="output file", type=str, required=True)

parser.add_argument("-l", "--length", help="number of characters to generate", type=int, default=10000)
parser.add_argument("--attempts", help="max attempt count for text generation", type=int, default=1)
parser.add_argument("--saturation", help="exponent applied to each next letter's weight. "
                                         "More saturation = model is more likely to pick more common continuations. "
                                         "If 0, model will pick random continuations", type=float, default=1)
parser.add_argument("--encoding", help="encoding of the training file", type=str, default="utf-8")
parser.add_argument("--reanalyze", help="force a repeated analysis and cache rebuild", action="store_true")

args = parser.parse_args()

depth = args.depth

if len(args.seed) != depth + 1:
    if len(args.seed) < depth + 1:
        print("ERR: seed is shorter than depth + 1, need longer seed")
        exit(-1)
    args.seed = args.seed[:depth + 1]
    print("WARN: seed is not of length depth + 1, using seed \"{}\"".format(args.seed))

cached_dict = CachedLetterDict.deserialize("cache.bin")
if cached_dict is not None \
        and cached_dict.training_file_names == args.files and cached_dict.letter_dict_depth == args.depth \
        and not args.reanalyze:
    print("Loading letter dict from cache...")
    letter_dict = cached_dict.letter_dict
    depth = cached_dict.letter_dict_depth
else:
    text = ""
    file_lengths = []
    for filename in args.files:
        with open(filename, "r", encoding=args.encoding) as file:
            content = file.read()
            file_lengths.append(len(content))
            text += content + "\n"

    if len(file_lengths) > 1:
        length_sum = sum(file_lengths)
        normalized_file_lengths = [x / length_sum for x in file_lengths]
        deviation = stdev(normalized_file_lengths)
        mean_file_length = mean(normalized_file_lengths)
        if deviation > length_stdev_threshold:
            favored_files = []
            for i in range(len(args.files)):
                if normalized_file_lengths[i] > mean_file_length:
                    favored_files.append(Path(args.files[i]).name)
            print("WARN: using training files with uneven lengths, model will favor {}".format(", ".join(favored_files)))

    print("Analyzing...")
    letter_dict = analyze.analyze_text(text, depth)

    print("Saving letter dict...")
    cached_dict = CachedLetterDict(letter_dict, args.files, depth)
    cached_dict.serialize("cache.bin")

print("Generating...")
gen_success = False
new_text = ""
for i in range(args.attempts):
    try:
        new_text = generate.generate_text(letter_dict, depth, args.length - 1, args.seed, args.saturation)
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(new_text)
        gen_success = True
        break
    except KeyError:
        print("ERR: could not generate text, try a different seed")

print("Done!")
if gen_success:
    print("Preview ({0} lines):\n{1}".format(preview_paragraphs, generate.get_preview(new_text, preview_paragraphs)))
