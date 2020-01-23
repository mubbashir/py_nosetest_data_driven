# Sample Porject for data driven nose tests

One file example to run data driven tests using python and nose tests with XML and HTML reports

## Documents

* [nose test](https://nose.readthedocs.io/en/latest/index.html)
* [Test-generators](https://nose.readthedocs.io/en/latest/writing_tests.html#test-generators)
* [nose-html-output](https://github.com/openstack/nose-html-output)

## Optional VENV (Python virtual environment)

* Create virtual environment
`python -m venv venv`

* Activate virtual env
  * Linux/Mac `source venv/bin/activate`
  
```shell script
$ source venv/bin/activate
(venv) [akhan@seq-akh-fc pipeline_workflow_tests] which python
~/workspace/pipeline_workflow_tests/venv/bin/python
```

## Install and execute

* Install dependencies: `pip install -r requirements.txt`

* Run tests 

```shell
$nosetests -v
nose_test_generator.test_dirs('dir1_ref', 'dir1_gen') ... ok
nose_test_generator.test_dirs('dir2_ref', 'dir2_gen') ... ok
nose_test_generator.test_data ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.003s

OK

```

## Run with reports 

```shell
nosetests -v --with-xunit --xunit-file=nose_test_results.xml --with-html-output --html-out-file=nose_test_results.html
nose_test_generator.test_dirs('dir1_ref', 'dir1_gen') ... ok
nose_test_generator.test_dirs('dir2_ref', 'dir2_gen') ... ok
nose_test_generator.test_data ... ok

----------------------------------------------------------------------
XML: /home/akhan/workspace/py_nosetest_data_driven/nose_test_results.xml
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

* [XML Report](./nose_test_results.xml)
* [HTML Report](./nose_test_results.html)
