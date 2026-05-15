from pyspark import pipelines as dp

BASE_DIR = "/Volumes/supply_chain_demo/default/raw"

schema = (
    spark.read.format("csv")
    .options(header=True, inferSchema=True)
    .load(f"{BASE_DIR}/data/DataCoSupplyChainDataset.csv")
    .schema
)
