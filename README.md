# Assignment-1-DECIDE
This repository consist of code for the DECIDE lab (course DD2480) at KTH. 

The program in this repository is a launch interceptor program that aims to test a hypothetical anti-ballistic missle system program. 

The program centers around the 'DECIDE()'-function that will output either "YES" or "NO" depending on the outcome of the different requirements. A "YES" output indicates that each of the 15 Launch Interpretor Conditions (LIC's) have been met, which assigns the boolean values "true" or "false" to the Conditions Met Vector (CMV). The Logical Connector Matrix (LCM) defines which individual LIC's must be considered jointly and is a 15x15 matrix containing the elements "ANDD", "ORR" and "NOTUSED". The CMV combined with the LCM is stored in the Preliminary Unlocking Matrix (PUM), which is also a 15x15 matrix. Finally, there are the Preliminary Unlocking Vector (PUV) and the Final Unlocking Vector (FUV). The PUV indicates which LIC's are relevant in each individual launch determination. The FUV is a 15-element vector, where all 15 elements must have the value "true" to unlock the launch, which outputs a "YES". 

"""The project aims to build and test a hyphotetical anti-ballistic missle system program. The program is built with Python and uses Unittests to verify the program. The code written is documentented with Sphinx. """



# Implementation
The Decide class can be found on /src/decide.py

The CMV class can be found on /src/cmv.py

The Test class can be found on /tests/test_cmv.py

## Run code and tests
Run the code with the following command:

Run tests with the following command:




## Workflow
During our first meeting we discussed and came up with some standards to make the workflow easy:
* Descriptive Issues with tags related to what needs to be done
* Branch names with Issue number 
* For each PR assign a reviewer
* Stand-ups to be held when need, communicated through Discord. 


## Contributions
"""During the first meeting we assigned two to create issues and tags needed. Then dividing all of the CMV related issues equally among all group members. For the remaining issues we split them in documentation related and code related issues."""
- **Ouday Ahmed**: 
- **Yiming Ju**:
- **Oscar Knowles**:
- **Elin Liu**:
- **Christofer Vikström**:
| Contributor 	| Issue 	|
|-------------	|-------	|
| Christofer  	|       	|
| Ouday       	|       	|
| Oscar       	|       	|
| Elin        	|       	|
| Yiming      	|          	|

## Workflow and continuous integration
To make the workflow consistent and easy, the group used GitHub as version control. The naming conventions during the project mitigated confusion and chaos as issues and pull requests had a decided framework. It was decided that 1 or more reviews per PR were required before the PR was merged and that the reviewers merged the PR if satisfactory. 



