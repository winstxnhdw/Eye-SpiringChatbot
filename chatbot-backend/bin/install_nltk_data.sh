#!/usr/bin/env bash

source $BIN_DIR/utils

echo "-----> Starting nltk data installation"

# Assumes NLTK_DATA environment variable is already set
# $ heroku config:set NLTK_DATA='/app/nltk_data'

# Install the nltk data
# NOTE: The following command installs the wordnet corpora, 
# so you may want to change for your specific needs.  
# See http://www.nltk.org/data.html
python -m nltk.downloader punkt

# If using Textblob, use this instead:
# python -m textblob.download_corpora lite

# Open the NLTK_DATA directory
cd ${NLTK_DATA}

# Delete all of the zip files
find . -name "*.zip" -type f -delete

echo "-----> Finished nltk data installation"