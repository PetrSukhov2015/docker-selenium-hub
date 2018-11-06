FROM inodb/python-selenium

COPY test.py test.py
COPY parallel_test_run.py parallel_test_run.py
ENTRYPOINT ["python", "parallel_test_run.py"]
