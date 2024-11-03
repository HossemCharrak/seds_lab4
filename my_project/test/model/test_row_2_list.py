from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2] / "src/model"))
from row_2_list import row_2_list
def test_for_clean_row():
    assert row_2_list("(2,081\t314,942\n") == ["2,081","314,942"]

def test_for_missing_area():
    assert row_2_list("\t293,410\n") is None

def test_for_missing_tab():
    assert row_2_list("1,463238,765\n") is None