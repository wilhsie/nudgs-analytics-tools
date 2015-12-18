#Welcome to NUGDS Analytics Tools Repo

To run the python script in /json_parser run using python on the test data:

i.e.

python mixed_reality_json_parser.py 12-18-2015_test_data.json

returns a list of player action and client time tuples.

Example Output:

[[{u'key': u'Cone A'}, u'1450361275.93543'], [{u'key': u'Cone Cleaner'}, u'1450361277.2875'], [{u'key': u'Tower'}, u'1450361279.57663'], [{u'key': u'Level'}, u'1450361282.83482'], [{u'key': u'Computer'}, u'1450361301.09486'], [{u'key': u'Wrong Formula'}, u'1450361312.90554'], [{u'key': u'Correct Graph'}, u'1450361325.92028'], [{u'key': u'Question 1 Answer 1: True'}, u'1450361331.08358'], [{u'key': u'Question 1 Answer 2: False'}, u'1450361331.08358'], [{u'key': u'Question 1 Answer 3: False'}, u'1450361331.08358'], [{u'key': u'Question 1 Answer 4: False'}, u'1450361331.08458'], [{u'key': u'Question 2 Answer 1: False'}, u'1450361331.08458'], [{u'key': u'Question 2 Answer 2: False'}, u'1450361331.08458'], [{u'key': u'Question 2 Answer 3: False'}, u'1450361331.08458'], [{u'key': u'Question 2 Answer 4: False'}, u'1450361331.08458'], [{u'key': u'Question 3 Answer 1: False'}, u'1450361331.08458'], [{u'key': u'Question 3 Answer 2: False'}, u'1450361331.08458'], [{u'key': u'Question 3 Answer 3: False'}, u'1450361331.08458'], [{u'key': u'Question 3 Answer 4: False'}, u'1450361331.08458'], [{u'key': u'Question 4 Answer 1: False'}, u'1450361331.08458'], [{u'key': u'Question 4 Answer 2: False'}, u'1450361331.08458'], [{u'key': u'Question 4 Answer 3: False'}, u'1450361331.08458'], [{u'key': u'Question 4 Answer 4: False'}, u'1450361331.08458'], [{u'key': u'CPT Speed: 3.064828'}, u'1450361331.22059'], [{u'key': u'Manual Depth: 0'}, u'1450361331.22059'], [{u'key': u'Max Depth: 0.5'}, u'1450361331.22059'], [{u'key': u'Driving: 10  You are an excellent driver!'}, u'1450361331.22059'], [{u'key': u'Preparation: 2  You still need to work on your preparation.'}, u'1450361331.22059'], [{u'key': u'CPT: 25  You did not perform the CPT to the desired depth.  You need to perform more manual CPT next time.  You went too fast for the CPT speed. '}, u'1450361331.22159'], [{u'key': u'Preliminary Analysis: 7 A colleague has looked at your results and has decided to change directions based on this.'}, u'1450361331.22159']]

TODO?:  Change client_times to UTC format so they're universally recognizeable
