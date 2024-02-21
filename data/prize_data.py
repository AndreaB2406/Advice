import pandas as pd
from flask import jsonify
from model.prize import Prize

class PrizeData:
    @staticmethod
    def get_prizes(catalog_id, filter, pagination):
        
        # Uploading data
        database = pd.read_excel('database.xlsx')

        # Catalog selection
        database = database[database.catalog_id == catalog_id]

        # Application of filters if there are any
        if filter['id'] is not None:
            database = database[database.prize_id==filter['id']]
        if filter['description'] is not None:
            database = database.loc[database.description.str.contains(filter['description'], case=False)]
        if pagination['page'] is not None:
            database = database[database.page==pagination['page']]
        if pagination['per_page'] is not None:
            database = database[database.per_page==pagination['per_page']]

        # Creating the prize list
        prizes = []
        for i,row in database.iterrows():
            single_prize = Prize(row.prize_id, row.title, row.description, row.image)
            prizes.append(single_prize.prize_to_dict())
        
        return prizes