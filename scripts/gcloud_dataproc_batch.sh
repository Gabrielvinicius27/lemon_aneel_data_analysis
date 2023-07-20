gcloud dataproc batches submit pyspark gs://lemon-project-393220-dataproc-files/read_aneel_file.py \
    --region="us-central1" \
    --jars="gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.23.2.jar" \
    --service-account="svc-dataproc-batch-acc@lemon-project-393220.iam.gserviceaccount.com" \
    --version="2.1" \
    --async \
    --subnet="subnetwork-dataproc-batch" \
    -- ${csv_file_name} ${bigquery_table}