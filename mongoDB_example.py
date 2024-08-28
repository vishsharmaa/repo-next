from pymongo import MongoClient
#Connect to MongoDB Server (default is localhost on port 27017)
client=MongoClient('mongodb://localhost:27017/')
#Create or Switch to a Database
db=client['my_database']
#Create or Switch to a Collection
collection=db['my_collection']

#Insert a Single Document into the Collection
document={"name":"John","age":29,"city":"San Francisco"}
insert_result=collection.insert_one(document)
print(f"Inserted document ID: {insert_result.inserted_id}")

#Insert Multiple Documents
documents=[
    {"name":"Sarah","age":00,"city":"Los Angeles"},
    {"name":"nick","age":10,"city":"Chicago"}
]
insert_many_result=collection.insert_many(documents)
print(f"Inserted document IDs: {insert_many_result.inserted_ids}")

#Find a Single Document
single_document=collection.find_one({"name":"John"})
print("Single document found:",single_document)

#Find all Documents
all_documents=collection.find()
for doc in all_documents:
    print("Document found:",doc)

#Query with a Condition
filtered_documents=collection.find({"age":{"$gt":25}})
for doc in filtered_documents:
    print("Filtered document",doc)

#Update a Document
update_result=collection.update_one(
    {"name":"John"},
    {"$set":{"age":30}}
)
print(f"Matched documents count: {update_result.matched_count}")
print(f"Modified documents count: {update_result.modified_count}")

#Delete a Document
delete_result=collection.delete_one({"name":"nick"})
print(f"Delete documents count: {delete_result.deleted_count}")

#Close the Connection
client.close()