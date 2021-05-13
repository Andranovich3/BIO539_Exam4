from Exam4_Code import *

def test_get_kmers():
  input_string = "ATTTGGATT"
  k_length = 3
  actual_result = get_kmers(input_string, k_length)[1]
  expected_result = ['ATT', 'TTT', 'TTG', 'TGG', 'GGA', 'GAT']
  assert actual_result == expected_result
