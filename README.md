# Assignment-1-DECIDE
This repository consist of code for the DECIDE lab (course DD2480) at KTH. 

The program in this repository is a launch interceptor program that aims to test a hypothetical anti-ballistic missle system program. 

The program centers around the 'DECIDE()'-function that will output either "YES" or "NO" depending on the outcome of the different requirements. A "YES" output indicates that each of the 15 Launch Interpretor Conditions (LIC's) have been met, which assigns the boolean values "true" or "false" to the Conditions Met Vector (CMV). The Logical Connector Matrix (LCM) defines which individual LIC's must be considered jointly and is a 15x15 matrix. The CMV combined with the LCM is stored in the Preliminary Unlocking Matrix (PUM), which is also a 15x15 matrix. Finally, there are the Preliminary Unlocking Vector (PUV) and the Final Unlocking Vector (FUV). The PUV indicates which LIC's are relevant in each individual launch determination. The FUV is a 15-element vector, where all 15 elements must have the value "true" to unlock the launch, which outputs a "YES". 


# Installation
In order to run the code properly, a version of Python >= 3.8 is required (Recommended Python 3.11.1).



## Run code and tests
To run the program, navigate to the src folder and run this command in the terminal to install the requirements:
     
     pip install -r requirements.txt


Run the code with the following command:

    python main.py

Run tests with the following command:

    python -m unittest discover

Switching bewteen "YES" and "NO" output from the provided example inputs: 

Change the input between positiveInput.yml and negativeInput.yml to toggle between "YES" and "NO" outputs.

*"YES" output*
```
def main():
    with open("tests/input/positiveInput.yml", 'r') as f:
        input = yaml.safe_load(f)
    if Decide(input).decide() is True:
        print("YES")
    else:
        print("NO")
```
*"NO" output*
```
def main():
    with open("tests/input/negativeInput.yml", 'r') as f:
        input = yaml.safe_load(f)
    if Decide(input).decide() is True:
        print("YES")
    else:
        print("NO")
```

## Contributions

- **Ouday Ahmed**: Created the code, documentation and test cases for LICs 2, 9 and 10. Ouday designed and implemented the general code architecture of the project, including the decide class, PUM class and test class. Ouday was a stakeholder of the documentation with Sphinx. 
- **Yiming Ju**: Created the code, documentation and test cases for LICs 1, 13 and 14. Yiming was the stakeholder for the documentation of the FUV class.  
- **Oscar Knowles**: Created the code, documentation and test cases for LICs 3, 8 and 11. Oscar was one of two stakeholders for the documentation of the project, which included the README and ESSENCE.
- **Elin Liu**: Created the code, documentation and test cases for LICs 0, 5 and 7. Elin was also the sole stakeholder for the documentation of the CMV class and the Test class. 
- **Christofer Vikström**: Created the code, documentation and test cases for LICs 4, 6 and 12. Christofer was also one of two stakeholders for the documentation of the project, which included the README and ESSENCE. 


### Argument 1 for P+
*Property: The group is creative and proactive, they have done something remarkable, for which they are proud.*

Using Sphinx to generate fluid and easy to navigate HTML documentation is an addition to the project that is a quality of life implementation that we think is valuable and remarkable. This makes the overall documentation user friendly. It also allows the user to search for specific parts of the documentation with ease and precision. 

### Argument 2 for P+
*Property: Most commits (typically 90%) are linked to an issue describing the feature / commit.*

Currently, the requirements regarding commits tracing to issues is fulfilled. 