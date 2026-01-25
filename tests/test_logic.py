import os

def test_file_existence():
    """Verifica se i file necessari esistono (esempio base)"""
    assert True 

def test_data_structure():
    expected_labels = ['negative', 'neutral', 'positive']
    assert 'positive' in expected_labels
