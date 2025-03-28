import pytest
from main import sort_data

@pytest.fixture
def temp_file(tmp_path):
    def _create_file(content):
        test_file = tmp_path / "test_data.txt"
        test_file.write_text(content, encoding="utf-8")
        return test_file
    return _create_file

@pytest.mark.parametrize(
    "file_content, expected_by_area, expected_by_population",
    [
        (
            "Canada,805291,35589391\nBelgium,215266,8589195\nItaly,481051,26592185\nUSA,128950,200591491",
            [
                ["Canada", 805291.0, 35589391],
                ["Italy", 481051.0, 26592185],
                ["Belgium", 215266.0, 8589195],
                ["USA", 128950.0, 200591491]
            ],
            [
                ["USA", 128950.0, 200591491],
                ["Canada", 805291.0, 35589391],
                ["Italy", 481051.0, 26592185],
                ["Belgium", 215266.0, 8589195]
            ]
        ),
        (
            "CountryA,500000,1000000\nCountryB,500000,2000000\nCountryC,300000,500000",
            [
                ["CountryA", 500000.0, 1000000],
                ["CountryB", 500000.0, 2000000],
                ["CountryC", 300000.0, 500000]
            ],
            [
                ["CountryB", 500000.0, 2000000],
                ["CountryA", 500000.0, 1000000],
                ["CountryC", 300000.0, 500000]
            ]
        ),
        (
            "OneCountry,100000,5000000",
            [["OneCountry", 100000.0, 5000000]],
            [["OneCountry", 100000.0, 5000000]]
        )
    ]
)
def test_sort_data(temp_file, file_content, expected_by_area, expected_by_population):
    test_file = temp_file(file_content)

    sorted_by_area, sorted_by_population = sort_data(test_file)

    assert sorted_by_area == expected_by_area
    assert sorted_by_population == expected_by_population

@pytest.fixture
def empty_file(temp_file):
    return temp_file("")

def test_empty_file(empty_file):
    sorted_by_area, sorted_by_population = sort_data(empty_file)
    assert sorted_by_area == []
    assert sorted_by_population == []

@pytest.fixture
def invalid_file(temp_file):
    return temp_file("Canada,805291,35589391\nBelgium,text_not_number,8589195")

def test_invalid_data(invalid_file):
    with pytest.raises(ValueError):
        sort_data(invalid_file)