import pytest
from string_utils import StringUtils

string_utils = StringUtils()



@pytest.fixture
def string_utils():
    return StringUtils()



# Тесты для метода capitilize

# Позитивные
def test_capitalize(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("Skypro") == "Skypro"
    assert string_utils.capitalize(" s y p") == " s y p"

# Негативные 
def test_capitalize_negative(string_utils):
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("    ") == "    "
    
# Тесты для метода trim

# Позитивные
def test_trim(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("skypro") == "skypro"
    assert string_utils.trim("   s k y  ") == "s k y "

# Негативные
def test_trim_negative(string_utils):
    assert string_utils.trim("") == ""
    assert string_utils.trim("    ") == ""


# Тесты для метода to_list

# Позитивные
def test_to_list(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert string_utils.to_list("a:b:c:d", ":") == ["a", "b", "c", "d"]

# Негативные
def test_to_list_negative(string_utils):
    assert string_utils.to_list("") == []
    assert string_utils.to_list("    ") == ["    "]


# Тесты для метода contains

# Позитивные
def test_contains(string_utils):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    assert string_utils.contains(" ", " ") == True

# Негативные
def test_contains_negative(string_utils):
    assert string_utils.contains("", "a") == False
    assert string_utils.contains("SkyPro", "") == True  # Пустая строка содержится в любой строке


# Тесты для метода delete_symbol

# Позитивные
def test_delete_symbol(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert string_utils.delete_symbol("SkyPro", "Sky") == "Pro"
# Негативные
def test_delete_symbol_negative(string_utils):
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", " ") == ""
    assert string_utils.delete_symbol("SkyPro", "") == "SkyPro"  # Пустой символ ничего не удаляет


# Тесты для метода starts_with

# Позитивные
def test_starts_with(string_utils):
    assert string_utils.starts_with("SkyPro", "S") == True
    assert string_utils.starts_with("SkyPro", "P") == False
    assert string_utils.starts_with("", "a") == False
    assert string_utils.starts_with(" ", " ") == True

# Негативные
def test_starts_with_negative(string_utils):
    assert string_utils.starts_with("", "S") == False
    assert string_utils.starts_with("SkyPro", "") == True  # Любая строка начинается с пустого символа

# Тесты для метода end_with

# Позитивные
def test_end_with(string_utils):
    assert string_utils.end_with("SkyPro", "o") == True
    assert string_utils.end_with("SkyPro", "y") == False
    assert string_utils.end_with("", "a") == False
    assert string_utils.end_with(" ", " ") == True

# Негативные
def test_ends_with_negative(string_utils):
    assert string_utils.ends_with("", "o") == False
    assert string_utils.ends_with("SkyPro", "") == True  # Любая строка заканчивается пустым символом


# Тесты для метода is_empty

# Позитивные
def test_is_empty(string_utils):
    assert string_utils.is_empty(" ") == True
    assert string_utils.is_empty("SkyPro") == False

# Негативные
def test_is_empty_negative(string_utils):
   assert string_utils.is_empty("") == True


# Тесты для метода list_to_string

# Позитивные
def test_list_to_string(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert string_utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert string_utils.list_to_string([" "]) == " "
  

# Негативные
def test_list_to_string_negative(string_utils):
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([None, 1, "two"], ", ") == "None, 1, two"