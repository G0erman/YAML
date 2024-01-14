from src.main import parse_data


def test_parse_data():
    data = parse_data("data_formats/data.yaml")
    assert data == {
        "name": "John Doe",
        "job": "Software Engineer",
        "skills": ["Python", "YAML", "Linux"],
    }
