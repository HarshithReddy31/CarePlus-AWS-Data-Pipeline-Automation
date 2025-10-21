import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

input_path = "s3://careplus-raw-zone/input_data/"
output_path = "s3://careplus-curated-zone/output_data/"

raw_data = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="csv",
    connection_options={"paths": [input_path], "recurse": True},
    transformation_ctx="raw_data"
)

df = raw_data.toDF()
df_clean = df.dropDuplicates().na.fill("Unknown")

final_dynamic_frame = DynamicFrame.fromDF(df_clean, glueContext, "final_dynamic_frame")

glueContext.write_dynamic_frame.from_options(
    frame=final_dynamic_frame,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet",
    transformation_ctx="final_output"
)

job.commit()
