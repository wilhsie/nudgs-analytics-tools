#Welcome to NUGDS Analytics Tools Repo

To run the python script in /json_parser run using python on the test data:

i.e.

python mixed_reality_json_parser.py 12-18-2015_test_data.json

returns a list of player action and client time tuples.

Example Output:

[['"Cone A"', '"1450361275.93543"'], ['"Cone Cleaner"', '"1450361277.2875"'], ['"Tower"', '"1450361279.57663"'], ['"Level"', '"1450361282.83482"'], ['"Computer"', '"1450361301.09486"'], ['"Wrong Formula"', '"1450361312.90554"'], ['"Correct Graph"', '"1450361325.92028"'], ['"Question 1 Answer 1: True"', '"1450361331.08358"'], ['"Question 1 Answer 2: False"', '"1450361331.08358"'], ['"Question 1 Answer 3: False"', '"1450361331.08358"'], ['"Question 1 Answer 4: False"', '"1450361331.08458"'], ['"Question 2 Answer 1: False"', '"1450361331.08458"'], ['"Question 2 Answer 2: False"', '"1450361331.08458"'], ['"Question 2 Answer 3: False"', '"1450361331.08458"'], ['"Question 2 Answer 4: False"', '"1450361331.08458"'], ['"Question 3 Answer 1: False"', '"1450361331.08458"'], ['"Question 3 Answer 2: False"', '"1450361331.08458"'], ['"Question 3 Answer 3: False"', '"1450361331.08458"'], ['"Question 3 Answer 4: False"', '"1450361331.08458"'], ['"Question 4 Answer 1: False"', '"1450361331.08458"'], ['"Question 4 Answer 2: False"', '"1450361331.08458"'], ['"Question 4 Answer 3: False"', '"1450361331.08458"'], ['"Question 4 Answer 4: False"', '"1450361331.08458"'], ['"CPT Speed: 3.064828"', '"1450361331.22059"'], ['"Manual Depth: 0"', '"1450361331.22059"'], ['"Max Depth: 0.5"', '"1450361331.22059"'], ['"Driving: 10  You are an excellent driver!"', '"1450361331.22059"'], ['"Preparation: 2  You still need to work on your preparation."', '"1450361331.22059"'], ['"CPT: 25  You did not perform the CPT to the desired depth.  You need to perform more manual CPT next time.  You went too fast for the CPT speed. "', '"1450361331.22159"'], ['"Preliminary Analysis: 7 A colleague has looked at your results and has decided to change directions based on this."', '"1450361331.22159"']]

TODO?:  Change client_times to UTC format so they're universally recognizeable
