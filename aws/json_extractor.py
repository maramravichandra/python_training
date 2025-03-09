from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JsonPrasing").getOrCreate()
data = {
  "value": {
    "ncle_screeningrequestid": "REQ123",
    "ncle_recordupdationtimestamp": "2025-03-07T10:00:00Z",
    "beneficiery1": {
      "ncle_screeningrequestid": "REQ456",
      "ncle_recordupdationtimestamp": "2025-03-07T11:00:00Z"
    },
    "beneficiery2": {
      "ncle_screeningrequestid": "REQ789",
      "ncle_recordupdationtimestamp": "2025-03-07T12:00:00Z"
    },
    "extra_info": {
      "ncle_screeningrequestid": "REQ999",
      "ncle_recordupdationtimestamp": "2025-03-07T13:00:00Z"
    }
  }
}

rdd = spark.sparkContext.parallelize([data])
df = spark.read.json(rdd)
df.printSchema()
df.createOrReplaceTempView("temp_view")
df.show(truncate=False)

sql = """
SELECT b.ext_obj.ncle_screeningrequestid, b.ext_obj.ncle_recordupdationtimestamp
FROM
(SELECT explode(array_append( transform(value_keys, x ->  from_json(get_json_object(json_value, concat('$.',x)), 'STRUCT<ncle_screeningrequestid:STRING, ncle_recordupdationtimestamp:STRING>') ) , values  ) ) AS ext_obj
FROM
(SELECT 
from_json(concat('{',"'ncle_screeningrequestid':'", value.ncle_screeningrequestid, "',", "'ncle_recordupdationtimestamp':'", value.ncle_recordupdationtimestamp, '\\'}'), 'STRUCT<ncle_screeningrequestid:STRING, ncle_recordupdationtimestamp:STRING>' ) as values, 
to_json(value) as json_value,
filter( json_object_keys(to_json(value)), x -> NOT array_contains(array('ncle_recordupdationtimestamp', 'ncle_screeningrequestid'), x)) as value_keys 
from temp_view ) a ) b
"""

df1 = spark.sql(sql)
df1.show(truncate=False)
#
# df1 = spark.sql("""select
# from_json(concat('{',"'ncle_screeningrequestid':'", value.ncle_screeningrequestid, "',", "'ncle_recordupdationtimestamp':'", value.ncle_recordupdationtimestamp, '\\'}'), 'STRUCT<ncle_screeningrequestid:STRING, ncle_recordupdationtimestamp:STRING>' ) as values,
# to_json(value) as json_value,
# filter( json_object_keys(to_json(value)), x -> NOT array_contains(array('ncle_recordupdationtimestamp', 'ncle_screeningrequestid'), x)) as value_keys
# from temp_view""")
# df1.createOrReplaceTempView("temp_view")
# df1.printSchema()
# df1.show(truncate=False)
#
# sql = """SELECT explode(array_append( transform(value_keys, x ->  from_json(get_json_object(json_value, concat('$.',x)), 'STRUCT<ncle_screeningrequestid:STRING, ncle_recordupdationtimestamp:STRING>') ) , values  ) ) AS values
#   from temp_view"""
# df2 = spark.sql(sql)
# df2.createOrReplaceTempView("temp_view")
# df2.show(truncate=False)



