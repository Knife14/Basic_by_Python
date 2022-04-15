from pymongo import *

client = MongoClient("mongodb://localhost:portID", connect=False)  # the row need to change

# base name
dbs = client.database_names()

# table name
colls = dict()
for db in dbs:
    tmp = client.get_database(db).collection_names()
    colls[db] = tmp

# field name
fileds = dict()
for db, tbs in colls.items():
    fileds[db] = dict()
    for tb in tbs:
        fileds[db][tb] = list()
        fs_tmp = client.get_database(db).get_collection(tb).find()
        for filed in fs_tmp:
            fileds[db][tb] += filed
            break

np = fileds['ningbo']['SectionRelation']
print("{")
for f in np:
    print('    \"' + f + '\",')
print("}")
