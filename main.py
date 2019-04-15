"""Customer Sentiment Analysis Review

Usage:
  main.py [--scrape=<y/n>]
  main.py [--scrape|--sentiment]
  main.py -h | --help
  main.py --version

Options:
  -h --help       Show this screen.
  --version       Show version.
  --scrape=<y/n>  Run scrapper (yes/no)
"""

from src.scrapper import ReviewScrapper
from src.data_cleaning import DataPrep

from docopt import docopt

if __name__=="__main__":
    data_prep = DataPrep()

    # import pdb; pdb.set_trace()
    data_prep.read_data()
    data_prep.parse_document()
    data_prep.clean_reviews()

    print(data_prep.dict_sentences)
    #
    #
    # arguments = docopt(__doc__, version='1.0')
    # # print(arguments)
    # if arguments['--scrape'] == 'y':
    #     scrapper = ReviewScrapper()
    #     scrapper.do_all()
    #     data_prep = DataPrep(data=scrapper.reviews)
    # else:
    #     data_prep = DataPrep()
    #
    # # import pdb; pdb.set_trace()
    # data_prep.read_data()
    # data_prep.parse_document()
    # data_prep.clean_reviews()
    #
    # print(data_prep.dict_sentences)
