import pytest
from powergrid.tso import Tso

@pytest.fixture
def sample_tso():
    """Creates a Tso instance using a valid TSO ID."""
    return Tso("TSO_FR_001")

def test_tso_initialization(sample_tso):
    """Test if Tso initializes correctly with valid data."""
    assert sample_tso.tso_id == "TSO_FR_001"
    assert isinstance(sample_tso.name, str)
    assert sample_tso.entsoe_code.startswith("10Y")

def test_tso_invalid_id():
    """Test that initializing Tso with an invalid ID raises ValueError."""
    with pytest.raises(ValueError, match="TSO ID 'INVALID_ID' not found in dataset."):
        Tso("INVALID_ID")

def test_tso_callable(sample_tso):
    """Test the __call__ method to return the TSO ID."""
    assert sample_tso() == "TSO_FR_001"

def test_tso_str(sample_tso):
    """Test the __str__ method for user-friendly output."""
    assert str(sample_tso) == f"TSO_FR_001 ({sample_tso.short_name})"

def test_tso_repr(sample_tso):
    """Test the __repr__ method for debugging output."""
    assert repr(sample_tso) == f"Tso(tso_id='TSO_FR_001', name='{sample_tso.name}')"
