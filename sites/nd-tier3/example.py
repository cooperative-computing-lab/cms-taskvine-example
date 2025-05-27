import awkward as ak
import dask_awkward as dak
from ndcctools.taskvine import DaskVine
import dask

# Create DaskVine
if __name__ == "__main__":
    m = DaskVine(
        [9101, 9200], #Define the available ports for DaskVine here#
        name="example_manager", #Define the name of the Vine manager here#
        run_info_path="/path/to/vine-run-info", #Define the location for the vine-run-info directory here#,
        run_info_template="example_application", #Define the name of the folder information for this application will be stored in here#,
    )

#Basic Options for DaksVine
    m.tune("temp-replica-count", 3)
    m.tune("worker-source-max-transfers", 100000)

    arr = dak.from_parquet('example_input.parquet')
    arr_sum = ak.sum(arr)

    computed_sum = dask.compute(
            arr_sum,
            scheduler=m.get,
            worker_transfers=True,
            resources={"cores": 1},
            task_mode="function-calls",
            lib_resources={'cores': 1, 'slots': 1},
        )
    
    print(f'The sum is {computed_sum}; if that number is 4998.4362, then you have successfully run DaskVine!')
