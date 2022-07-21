#test_sibenice
#python3 -m pytest -v test_*.py

import sibenice_du03_21, pytest

def test_length_of_travnik_is_ok(): 
    assert sibenice_du03_21.podtrzitka('trávník') == '_ _ _ _ _ _ _ '

def test_length_of_les_is_ok(): 
    assert sibenice_du03_21.podtrzitka('les') == '_ _ _ '

def test_length_of_kefir_is_ok(): 
    assert sibenice_du03_21.podtrzitka('kefír') == '_ _ _ _ _ '

    

