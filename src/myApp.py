import logging
import checkDataLib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    logging.info('Started')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    try:
        df_data = checkDataLib.loadCsv()
        df_data = checkDataLib.chkMissingValues(df_data)
        df_data = checkDataLib.validateTheSchema(df_data)
    except Exception:
        logging.exception("Fatal error in checkData")

    logging.info('Finished')


if __name__ == '__main__':
    main()