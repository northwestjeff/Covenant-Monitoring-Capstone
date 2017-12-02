import json
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Capstone.settings")
import django

django.setup()
from pages.models import Statement, Data, Organization

with open("Fixtures/data.json") as file:
    data = json.loads(file.read())


# Total Assets
# total_sum = []
# for i in data['Rows']["Row"]:
#     print(i['Summary'])
# for x in i['Summary']['ColData']:
#     print(x)


#         total_sum.append(x)
# print("The {} are: {}".format(total_sum[0].get('value'), total_sum[1].get('value')))
# for i in data['Rows']["Row"]:
#     for x in i['Rows']['Row']:
#         for y in x["Rows"]["Row"]:
#             print(y)
#             # if y.get(['ColData'])
# row = 0
# Assets
# print(data['Rows']['Row'][0])
# print(data['Rows']['Row'][0].keys())  # Returns: dict_keys(['Header', 'Rows', 'Summary', 'type', 'group'])
# print(data['Rows']['Row'][0]['Rows'].keys())  # Returns: dict_keys(['Row'])
# print(data['Rows']['Row'][0]['Rows']["Row"])  # Returns list of data
# print(len(data['Rows']['Row'][0]['Rows']["Row"])) # Returns: 2
#
# deep_list = data['Rows']['Row'][0]['Rows']["Row"]
# for i in deep_list:
#     print(i)  # Returns dict of Current Assets and Fixed Assets
#
# print(data['Rows']['Row'][0]['Rows']["Row"][0]) # Current assets
# print(data['Rows']['Row'][0]['Rows']["Row"][1]) # Fixed assets
# print(data['Rows']['Row'][0]['Rows']["Row"][0].keys()) # Returns: dict_keys(['Header', 'Rows', 'Summary', 'type', 'group'])
# print(data['Rows']['Row'][0]['Rows']["Row"][0]["Rows"]) # Returns dict closer to detail but still not there yet.
# print(data['Rows']['Row'][0]['Rows']["Row"][0]["Rows"]["Row"]) # returns list
#

def sum_check(summary, col, val, statement, a):
    if summary in a.keys():
        k = a[summary][col][0][val]
        v = a[summary][col][1][val]
        statement[k] = v


def col_check(col, val, statement, a):
    if col in a.keys():
        k = a[col][0][val]
        v = a[col][1][val]
        statement[k] = v

detail_list = data['Rows']['Row']

col = 'ColData'
val = 'value'
rows = "Rows"
row = 'Row'
summary = 'Summary'


def row_check(rows, row, i):
    if rows in i.keys():
        return i[rows][row]
    else:
        pass


# THIS WORKS.  COMMENTED TO PRESERVE.
# for a in detail_list:
#     col_check(col, val, statement, a)
#     z = a['Rows']["Row"]
#     for y in z:
#         col_check(col, val, statement, y)
#         if "Rows" in y.keys():
#             var = y["Rows"]["Row"]
#             for i in var:
#                 col_check(col, val, statement, i)
#                 if "Rows" in i.keys():
#                     q = i["Rows"]["Row"]
#                     for n in q:
#                         col_check(col, val, statement, n)
#                         if "Rows" in n.keys():
#                             w = n["Rows"]['Row']
#                             for u in w:
#                                 col_check(col, val, statement, u)
#                                 if "Rows" in u.keys():
#                                     c = u["Rows"]["Row"]
#                                     for m in c:
#                                         col_check(col, val, statement, m)
#                                         if "Rows" in m.keys():
#                                             b = m["Rows"]["Row"]
#                                             for e in b:
#                                                 col_check(col, val, statement, e)
# for k,v in statement.items():
#     print("{}: {}".format(k,v))
header_dict = {}
for i in data['Header'].keys():
    if i == "Option":
        pass
    else:
        header_dict[i] = data['Header'][i]


def val_list(lst, statement={}):
    for i in lst:
        col_check(col, val, statement, i)
        sum_check(summary, col, val, statement, i)
        if "Rows" in i.keys():
            a = i['Rows']['Row']
            val_list(a, statement)
    return statement



# for a in detail_list:
#     col_check(col, val, statement, a)
#     sum_check(summary, col, val, statement, a)
#     z = a['Rows']["Row"]
#     for y in z:
#         col_check(col, val, statement, y)
#         sum_check(summary, col, val, statement, y)
#         if "Rows" in y.keys():
#             var = y["Rows"]["Row"]
#             for i in var:
#                 col_check(col, val, statement, i)
#                 sum_check(summary, col, val, statement, i)
#                 if "Rows" in i.keys():
#                     q = i["Rows"]["Row"]
#                     for n in q:
#                         col_check(col, val, statement, n)
#                         sum_check(summary, col, val, statement, n)
#                         if "Rows" in n.keys():
#                             w = n["Rows"]['Row']
#                             for u in w:
#                                 col_check(col, val, statement, u)
#                                 sum_check(summary, col, val, statement, u)
#                                 if "Rows" in u.keys():
#                                     c = u["Rows"]["Row"]
#                                     for m in c:
#                                         col_check(col, val, statement, m)
#                                         sum_check(summary, col, val, statement, m)
#                                         if "Rows" in m.keys():
#                                             b = m["Rows"]["Row"]
#                                             for e in b:
#                                                 col_check(col, val, statement, e)
#                                                 sum_check(summary, col, val, statement, e)
#
document = Statement()
#
document.time = header_dict['Time']
document.name = header_dict['ReportName']
document.start_period = header_dict['StartPeriod']
document.end_period = header_dict['EndPeriod']
document.summarize_by = header_dict['SummarizeColumnsBy']
document.organization = Organization.objects.get(pk=2)
document.save()


for k, v in val_list(detail_list).items():
    val = Data()
    val.statement = document
    val.column_headers = k
    val.value = v
    val.save()




print(header_dict)

