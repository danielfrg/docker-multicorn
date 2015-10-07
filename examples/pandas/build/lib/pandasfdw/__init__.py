from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres


import pandas as pd


class PandasForeignDataWrapper(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(PandasForeignDataWrapper, self).__init__(options, columns)
        self.filename = options["filename"]
        self.columns = columns

    def execute(self, quals, columns):
        log_to_postgres(self.filename)
        df = pd.read_csv(self.filename, engine='python')

        for qual in quals:
            if qual.operator == '<':
                df = df[df[qual.field_name] < qual.value]

        df = df[list(columns)]
        for i, row in df.iterrows():
            yield row.to_dict()
