import sys

from sys import stdout

from pydantic import BaseModel

if __name__ == "__main__":
    # pydantic config
    BaseModel.model_config['protected_namespaces'] = ()

    if len(sys.argv) > 1:
        if sys.argv[1] == "scraper":
            print("running scraper")
            from universalis_scraper.scraper import refresh_universalis_data
            refresh_universalis_data()
        elif sys.argv[1] == "parser":
            print("running parser")
            from gamedata_parser.parser import parse_csv, delete_models
            delete_models(stdout)
            parse_csv(stdout)
        elif sys.argv[1] == "calc_test":
            print("running calc_test")
            from calc.market_prices import print_test_results
            print_test_results()
    else:
        print("no arguments given!")
