import csv
import pytest
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))
from row_2_list import row_2_list
dataset = []
with open('house_price.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)
@pytest.mark.parametrize("row_number,input_row",enumerate(dataset,1))
def test_row_to_list_with_missing_values(row_number,input_row):
    input_string = ' '.join(input_row) 
    result = row_2_list(input_string,';')
    missing_values = any(element == '' for element in result)
    assert not missing_values, f"Missing value found in the row no.{row_number}: {input_row}"
