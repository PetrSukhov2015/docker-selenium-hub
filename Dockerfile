FROM ubuntu:16.04

COPY test.py test.py
COPY parallel_test_run.py parallel_test_run.py
RUN python parallel_test_run.py
