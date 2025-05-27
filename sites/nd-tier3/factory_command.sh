vine_factory -T condor \
    -C factory.json \
    --python-env taskvine_packed.tar.gz \
    --scratch-dir /path/to/vine_scratch/ \
    --parent-death \
    --factory-timeout 600
