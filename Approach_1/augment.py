import json
import os
import ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
        getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
import nltk

nltk.download('wordnet')

from eda import *

# arguments to be parsed from command line
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="input file of unaugmented data")
ap.add_argument("--label", required=True, type=str, help="label file of unaugmented data")
ap.add_argument("--output", required=False, type=str, help="output file of unaugmented data")
ap.add_argument("--num_aug", required=False, type=int, help="number of augmented sentences per original sentence")
ap.add_argument("--alpha", required=False, type=float, help="percent of words in each sentence to be changed")
args = ap.parse_args()

# the output file
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join

    output = join(dirname(args.input), 'eda_' + basename(args.input))

# number of augmented sentences to generate per original sentence
num_aug = 9  # default
if args.num_aug:
    num_aug = args.num_aug

# how much to change each sentence
alpha = 0.1  # default
if args.alpha:
    alpha = args.alpha

output_file_label = join(dirname(args.label), 'eda_' + basename(args.label))

# generate more data with standard augmentation
def gen_eda(train_orig, train_orig_label, output_file, alpha, num_aug=9):
    writer = open(output_file, 'w')
    writer_label = open(output_file_label, 'w')
    lines = open(train_orig, 'r').readlines()
    train_orig_label_lines = open(train_orig_label, 'r').readlines()

    # for i, train_orig_label_line in enumerate(train_orig_label_lines):
    #     part_label = train_orig_label_line[:-1].split('\t')[0]
    #     for j in range(0,num_aug+1):
    #         writer_label.write(part_label + '\n')

    for i, line in enumerate(lines):
        part_label = train_orig_label_lines[i][:-1].split('\t')[0]
        part = line[:-1].split('\t')[0]
        dic_part = json.loads(part)
        sentence = dic_part['goal']
        aug_sentences = eda(sentence, alpha_sr=alpha, alpha_ri=alpha, alpha_rs=alpha, p_rd=alpha, num_aug=num_aug)
        for aug_sentence in aug_sentences:
            new_dic_part = dic_part
            new_dic_part['goal'] = aug_sentence
            try:
                writer.write(str(new_dic_part) + '\n')
                writer_label.write(part_label + '\n')
            except:
                pass

    writer.close()
    print("generated augmented sentences with eda for " + train_orig + " to " + output_file + " with num_aug=" + str(
        num_aug))


# main function
if __name__ == "__main__":
    # generate augmented sentences and output into a new file
    gen_eda(args.input, args.label, output, alpha=alpha, num_aug=num_aug)
