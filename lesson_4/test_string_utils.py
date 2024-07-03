import pytest
from string_utils import StringUtils

string_utils = StringUtils()



@pytest.fixture
def string_utils():
    return StringUtils()

# Тесты для метода capitilize
def test_capitalize(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"
    assert string_utils.capitilize("Skypro") == "Skypro"
    assert string_utils.capitilize(" s y p") == " s y p"
    assert string_utils.capitilize("") == ""

# Тесты для метода trim
def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   s k y  ") == "s k y  "
    assert string_utils.trim("") == ""
    assert string_utils.trim("      ") == ""

# Тесты для метода to_list
def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("a:b:c:d", ":") == ["a", "b", "c", "d"]
    assert string_utils.to_list("") == []
    assert string_utils.to_list(" ") == [" "]
    assert string_utils.to_list(", ,") == ["", " ", ""]

# Тесты для метода contains
def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    assert string_utils.contains("", "a") == False
    assert string_utils.contains(" ", " ") == True

# Тесты для метода delete_symbol
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "Sky") == "Pro"
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", " ") == ""

# Тесты для метода starts_with
def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True
    assert string_utils.starts_with("SkyPro", "P") == False
    assert string_utils.starts_with("", "a") == False
    assert string_utils.starts_with(" ", " ") == True

# Тесты для метода end_with
def test_ends_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True
    assert string_utils.end_with("SkyPro", "y") == False
    assert string_utils.end_with("", "a") == False
    assert string_utils.end_with(" ", " ") == True

# Тесты для метода is_empty
def test_is_empty(string_utils):
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty(" ") == True
    assert string_utils.is_empty("SkyPro") == False

# Тесты для метода list_to_string
def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([" "]) == " "
    assert string_utils.list_to_string([None, 1, "two"], ", ") == "None, 1, two"
