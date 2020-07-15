# freq_dist by Marc Kirkwood, 2020.

A script to analyse the frequencies of the most common words across multiple documents, with context sentences provided.
Relative to the script's working directory, all files ending in `.txt` are read from `data/` as input. Output is written to a CSV file in the working directory.

## Operation
If you have Make and Docker installed, you can build and run the Docker container with the provided Makefile.
Simply run the following command in the project directory:
```
$ make
```

If successful, the command should end with the following output:

```
Writing results for top word frequencies to top_20_words.csv...
Complete.
```

As stated, the results are written to `top_20_words.csv` for opening in a spreadsheet application of your choice. Note: For Docker, file syncing with the host is achieved with a basic bind mount to share the working directory. This was done for expediency.

### Alternatively
- You could create a virtualenv, activate it, and install dependencies manually with `pip install -r requirements.txt`.
The NLTK downloader for the stopwords data encounters an SSL certification issue on OSX, so I prefer Docker to avoid this.
- Without running Make, `freq_dist` can be invoked manually with `python freq_dist.py`.
