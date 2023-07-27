# Europarl preprocessing
European Parliament Proceedings Parallel Corpus (Europarl) is a dataset for machine translation. Despite of its hugeness, it is hard to construct training dataset with .csv file. I've builded a simple data transform code.

In the first step, you should go to the github: https://github.com/mustaszewski/europarl-extract
It provides a tool (called EuroparlExtract) to extract the text file from the official Europarl dataset, remove speaker information, and arrange them with third party tools, which is not well explained about how to use.

Afterwards, follow the step (Extract Corpora) in the same github site.
There are some example about how to generate text file.
In my case, I enter the following command:

python3 extract.py comparable -sl EN -tl all -i txt/ -o corpora/ -s corpora/europarl_statements.csv -al -c both

Now you can check a lot of txt files in europarl-extract/corpora/comparable/non-translated/EN/

Move to the europarl-extract/corpora/comparable/ and try

python combine_txt.py

Finally, you can get the output.csv in the current folder.

If you want to slice the output.csv into two fold (train, test), try:

python data_split.py

I also set up for the dataset to be pre-processed into lengths of sentences with 4 to 30 words.
You can change the ratio between train and test. (I set the ratio as 0.8)

