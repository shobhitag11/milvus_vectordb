from pymilvus import CollectionSchema, FieldSchema, DataType, Collection, connections

connections.connect(
  alias = "default",
  user = "user",
  password = "password",
  host = "0.0.0.0",
  port = "19530"
)

from pymilus import utility
# Drop the collection if present
utility.drop_collection("<collection_name>")
# Checks the collection existance
utility.has_collection("<collection_name>")


vid = FieldSchema(
  name = "id",
  dtype = DataType.INT64,
  is_primary = True
)

content = FieldSchema(
  name = "content",
  dtype = DataType.VARCHAR,
  max_length = 10000
)

source_path = FieldSchema(
  name = "source_path",
  dtype = DataType.VARCHAR,
  max_length = 10000
)

embedding = FieldSchema(
  name = "embedding",
  dtype = DataType.FLOAT_VECTOR,
  dim = 768
)

schema = CollectionSchema(
  fields = [vid, content, source_path, embedding],
  description = "<Define the description of Collection>",
  enable_dynamic_field = True
)

collection = Collection(
  name = "<collection_name>",
  schema = schema,
  using = "default"
)

# index_params = {
#   "index_type" = "IVF_FLAT",
#   "metric_type" = "L2",
#   "params" : {
#     "nlist": 1024
#   }
# }

index_params = {
  "index_type" = "HNSW",
  "metric_type" = "L2",
  "params" : {
    "M":8,
    "efConstruction": 64
  }
}

collection.create_index(
  field_name = "embedding",
  index_params = index_params,
  index_name = "embedding"
)


