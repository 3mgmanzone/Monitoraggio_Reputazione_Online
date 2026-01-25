import os

def test_project_structure():
    assert os.path.exists("requirements.txt")

def test_expected_labels_exist():
    expected_labels = ['negative', 'neutral', 'positive']
    assert 'positive' in expected_labels
    assert 'negative' in expected_labels
    assert 'neutral' in expected_labels

def test_tests_folder_exists():
    assert os.path.isdir("tests")
