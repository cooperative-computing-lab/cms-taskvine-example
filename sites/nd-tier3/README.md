To run Task/Dask Vine on the ND Tier 3:

```
conda create -n taskvine python=3 -y
conda activate taskvine
conda install ndcctools -y
python -m pip install awkward dask_awkward pyarrow pandas
poncho_package_create taskvine taskvine_packed.tar.gz
```

From here, you will need two interactive sessions. One to run the application and one run the Vine Factory. A second login session will work, but using terminal multiplexer (e.g. tmux, screen) might be simpler. 

You will need to edit a few things before the examples are ready to run:
   1. In `example.py`, adjust the run argument of `run_info_path` to an area where you would like to store the files for the manager, staging files, and log files for this application.
   2. In `factory_command.sh`, adjust the argument for `scratch_dir` to point to an appropriate scratch directory.

In the first terminal, do `python example.py`. When a progress bar appears, the application is ready to receive workers. In the second terminal, do `source factory_command.sh`. When status table appears listing the number of waiting, running, and completed tasks, the factory is ready to request and connect workers. If the application `example.py` runs successfully, you have successfully set up TaskVine.
