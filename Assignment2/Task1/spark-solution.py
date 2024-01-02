#!/usr/bin/env python3
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
# Initialize a Spark session
spark = SparkSession.builder.appName("Task1").getOrCreate()


    # Check if the correct number of command line arguments are provided

def task_1_1(all_cases):
    # Read cases files for 2012, 2013, and 2014
    #cases_2012 = spark.read.csv(sys.argv[1], header=True)
    #cases_2013 = spark.read.csv(sys.argv[2], header=True)
    #cases_2014 = spark.read.csv(sys.argv[3], header=True)

    # Read the cases_state_key file
    state_key = spark.read.csv(sys.argv[4], header=True)

    # Union the cases files for all three years
    #all_cases = cases_2012.union(cases_2013).union(cases_2014)

    # Join cases data with state_key data to get state names
    cases_with_states = all_cases.join(state_key, "state_code")

    # Group by state name and count the number of cases
    state_crime_counts = cases_with_states.groupBy("state_name").count()

    # Sort states by crime rate in descending order
    sorted_states = state_crime_counts.orderBy("count", ascending=False)

    # Take the top 10 states
    top_10_states = sorted_states.limit(10)

    # Collect the results and return as a list
    return top_10_states.select("state_name").rdd.flatMap(lambda x: x).collect()

# Function to perform Task 1.2 - Find the judge who has presided over the most criminal cases
# Function to perform Task 1.2 - Find the judge who has presided over the highest number of criminal cases
def task_1_2(merged_cases):
 
    #cases_2012 = spark.read.csv(sys.argv[1], header=True)
    #cases_2013 = spark.read.csv(sys.argv[2], header=True)
    #cases_2014 = spark.read.csv(sys.argv[3], header=True)
    judges_clean = spark.read.csv(sys.argv[5], header=True)
    judge_case_merge_key = spark.read.csv(sys.argv[6], header=True)
    acts_section = spark.read.csv(sys.argv[7], header=True)
    # Merge the case data into a single DataFrame
    #merged_cases = cases_2012.union(cases_2013).union(cases_2014)
	# Merge the judge_case_merge_key with merged_cases
    merged_data = merged_cases.join(judge_case_merge_key, "ddl_case_id")
	# Filter for criminal cases
    criminal_cases = merged_data.join(acts_section.filter(acts_section["criminal"] == 1), "ddl_case_id")
	# Count cases per decision judge
    judge_case_counts = criminal_cases.groupBy("ddl_decision_judge_id").count()
	# Find the judge with the most cases
    judge_with_most_cases = judge_case_counts.orderBy(col("count").desc()).dropna().first()
	# Display the result
    return int(judge_with_most_cases["ddl_decision_judge_id"])


   
   
   
   
    


if len(sys.argv) < 8:
    print("Usage: spark-solution.py <case_2012.csv> <case_2013.csv> <case_2014.csv> <cases_state_key.csv> <judges_clean.csv> <judge_case_merge_key.csv> <acts_section.csv>")
    sys.exit(1)
cases_2012 = spark.read.csv(sys.argv[1], header=True,inferSchema=True)
cases_2013 = spark.read.csv(sys.argv[2], header=True,inferSchema=True)
cases_2014 = spark.read.csv(sys.argv[3], header=True,inferSchema=True) 
merged_cases = cases_2012.union(cases_2013).union(cases_2014) 
    # Perform Task 1.1
states_result = task_1_1(merged_cases)

    # Perform Task 1.2
judge_result = task_1_2(merged_cases)
    # Create a tuple of results
final_result = (states_result, judge_result)

    # Print the final result to the output file
with open(sys.argv[8], "w") as output_file:
    output_file.write(str(final_result))

    # Stop the Spark session
spark.stop()



