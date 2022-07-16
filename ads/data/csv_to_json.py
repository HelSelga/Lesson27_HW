import csv
import json

import pandas
from django.http import JsonResponse

from ads.models import CategoryModel, AdModel

CAT_CSV_DATA = pandas.read_csv('categories.csv', sep=",").to_dict()
AD_CSV_DATA = pandas.read_csv('ads.csv', sep=",").to_dict()


# def ads_json():
#     with open(AD_CSV_DATA) as f:
#         reader = csv.DictReader(f)
#         rows = list(reader)
#     with open('ads.json', 'w') as f:
#         return json.dump(rows, f)

#
# def read_json(filename, encoding="utf-8"):
#     with open(filename, encoding=encoding) as f:
#         return json.load(f)
#

def add_to_cat():
    i = 0
    while max(CAT_CSV_DATA['id'].keys()) >= i:
        CategoryModel.objects.create(
            name=CAT_CSV_DATA["name"][i],
        )
        i += 1
    return JsonResponse("Added to table Category, status - ok", safe=False, status=200)
#
#
# def add_to_ads():
#     i = 0
#     while max(AD_CSV_DATA['Id'].keys()) >= i:
#         AdModel.objects.create(
#             name=AD_CSV_DATA["name"][i],
#             author=AD_CSV_DATA["author"][i],
#             price=AD_CSV_DATA["price"][i],
#             description=AD_CSV_DATA["description"][i],
#             address=AD_CSV_DATA["address"][i],
#             is_published=AD_CSV_DATA["is_published"][i],
#         )
#         i += 1
#     return JsonResponse("Added to table Ads, status - ok", safe=False, status=200)
