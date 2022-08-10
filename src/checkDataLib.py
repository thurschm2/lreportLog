import logging

import numpy as np
import pandas as pd
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, \
    CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation, IsDistinctValidation, \
    CustomElementValidation
from ukpostcodeutils import validation




def loadCsv():
    logging.info('opening csv file')
    df = pd.read_csv ('uk-500.csv',  encoding='utf-8', encoding_errors='ignore')
    print(df.dtypes)
    return df

def chkMissingValues (df):
    for col in df.columns:
        miss = df[col].isnull().sum()
        if miss > 0:
            logging.warning("{} has {} missing value(s)".format(col, miss))
        else:
            print("{} has NO missing value!".format(col))
    return df

def validateUKPostcode(df):
    return df

def validateTheSchema(df):
    # "first_name", "last_name", "company_name", "address", "city", "county", "postal", "phone1", "phone2", "email", "web"

    null_validation = [CustomElementValidation(lambda d: d.empty() is not True, 'this field cannot be null')]

    # define validation scheme
    schema = Schema([
        Column('ID', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=False),
        Column('first_name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('last_name', [LeadingWhitespaceValidation(),TrailingWhitespaceValidation()]),
        Column('company_name',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()], allow_empty=False),
        Column('address',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('city',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('county',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('postal',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('phone1',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('phone2',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('email',  [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
        Column('web', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()])])

    #  apply validation rules and logging of any errors
    errors = schema.validate(df)
    for error in errors:
        logging.info(error)

    # this would be a way to drop any record that did not get full validation
    # errors = schema.validate(df)
    # errors_index_rows = [e.row for e in errors]
    # data_clean = data.drop(index=errors_index_rows)




