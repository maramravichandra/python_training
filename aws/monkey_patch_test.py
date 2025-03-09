from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

class PreventSparkPatching:
    def __init__(self, func):
        self.original_func = func
        self.patched_func = None
        self.patched = False
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        def wrapper(*args, **kwargs):
            if self.patched and self.patched_func:
                return self.patched_func(instance, *args, **kwargs)
            else:
                return self.original_func(instance, *args, **kwargs)

        return wrapper

    def __set__(self, instance, value):
        if self.patched:
            raise AttributeError(f"Cannot reassign {self.name}. Already patched.")
        if not callable(value):
            raise ValueError(f"{value} is not callable.")
        self.patched_func = value
        self.patched = True

# Get the SparkSession class
spark_session_class = SparkSession

# Apply the descriptor to createDataFrame and sql
spark_session_class.createDataFrame = PreventSparkPatching(spark_session_class.createDataFrame)
spark_session_class.sql = PreventSparkPatching(spark_session_class.sql)

# Example Usage
spark = SparkSession.builder.appName("PatchRestriction").getOrCreate()

data = [("Alice", 25), ("Bob", 30)]
schema = ["name", "age"]
df = spark.createDataFrame(data, schema)
df.show()

def patched_createDataFrame(spark, data, schema=None, sampleRatio=None):
    print("Patched createDataFrame called!")
    # Ensure no recursion: call the original createDataFrame
    return spark._jsparkSession.createDataFrame(data, schema)

def patched_sql(spark, sqlQuery, *args, **kwargs):
    print(f"Patched sql called with query: {sqlQuery}")
    # Ensure no recursion: call the original sql method
    return spark._jsparkSession.sql(sqlQuery)

# Patch createDataFrame
spark_session_class.createDataFrame = patched_createDataFrame
spark.createDataFrame(data, schema).show()

# Attempt to re-patch createDataFrame
try:
    spark_session_class.createDataFrame = lambda spark, data, schema=None: print("Attempting to re-patch createDataFrame")
except AttributeError as e:
    print(e)  # Output: Cannot reassign createDataFrame. Already patched.

# Patch sql
df.createOrReplaceTempView("people")
spark_session_class.sql = patched_sql
spark.sql("SELECT * FROM people").show()

# Attempt to re-patch sql
try:
    spark_session_class.sql = lambda spark, sqlQuery: print("Attempting to re-patch sql")
except AttributeError as e:
    print(e)  # Output: Cannot reassign sql. Already patched.

spark.stop()