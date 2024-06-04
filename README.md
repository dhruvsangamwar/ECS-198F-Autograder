# ECS-198F-Autograder
These are the autograder for the assignments for the student taught course (Fall 2023). We provided auto grading scripts for python and c++ so that students had a choice in the language they used to solve the problem sets. 

# Structure
The grading setup for each assignment follows this exact setup:
### Python
```bash
├── requirements.txt
├── run_autograder
├── run_tests.py
├── setup.sh
└── tests
    ├── __init__.py
    ├── test_files.py
    ├── test_leaderboard.py
    └── test_simple.py
```

`requirements.txt`: This is ran on gradescope's docker container.

`run_autograder`: Bash script that copies student submission from `./submission` to `./source`

`run_tests.py`: Opens a json logging file that gets submitted to the gradescope api upon completion of the grading.

`setup.sh`: Installs python and dependencies.

`tests/__init__.py` : Boilerplate file required by gradescope

`tests/test_files.py` : Checks if the required files have the right name and are submitted by student. 

`tests/test_leaderboard.py` : Sets up the public leaderboard so that students can see their runtime compared to their peers. (Students are able to pick nicknames for anonymity)

`tests/test_simple.py` : Contains all the unit tests.

A sample test case within `test_simple` would look like this:
```python
    # Associated point value within GradeScope
    @weight(20)

    def test_1(self):
        """Test Case 1"""
        arr1 = ["red_left", "blue_left", "blue_right", "red_right"] ## Expected Output
        val = isValidBracelet(arr1) # Calling the function defined by the student
        self.assertEqual(val, 'True') # Assert
```

### C++

```bash
├── Tester.cpp
├── makefile
├── requirements.txt
├── run_autograder
├── run_tests.py
├── setup.sh
└── tests
    ├── __init__.py
    ├── test_files.py
    ├── test_leaderboard.py
    └── test_subprocess.py
```
`Tester.cpp`: Calls the function defined by the student. The output is put onto `std::out`

`makefile`: Builds Tester.cpp

`requirements.txt`: This is ran on gradescope's docker container.

`run_autograder`: Bash script that copies student submission from `./submission` to `./source`

`run_tests.py`: Opens a json logging file that gets submitted to the gradescope api upon completion of the grading.

`setup.sh`: Installs python and dependencies.

`tests/test_files.py` : Checks if the required files have the right name and are submitted by student. 

`tests/test_leaderboard.py` : Sets up the public leaderboard so that students can see their runtime compared to their peers. (Students are able to pick nicknames for anonymity)

`tests/test_subprocess.py` : Create a subprocess to run the makefile, reads output from standard output and asserts. 

A sample test case would look like this:
```cpp
    # Associated point value within GradeScope
    @weight(5)
    def test_Compile(self):
        #Title used by Gradescope 
        """Clean Compile"""

        # Create a subprocess to run our make file to ensure it compiles 
        test = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = test.stderr.read().strip().decode('utf-8')
        test.kill()

        # Standard unit test case with an associated error message 
        self.assertTrue( output == "", msg=output)
        test.terminate()
```

