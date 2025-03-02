import pytest

from powergrid.tso import Tso
from powergrid.tso_finder import TsoFinder

@pytest.fixture(scope="module")
def finder():
    """Initialize TsoFinder with the default dataset."""
    return TsoFinder()

def test_by_region_case_insensitive(finder):
    """Test lookup by region code (case-insensitive)."""
    region_code = "fr-idf"  # Lowercase input
    tso_id = finder.by_region(region_code)
    assert tso_id is not None
    assert tso_id in finder.tso_details

def test_invalid_region_code(finder):
    """Test lookup with an invalid region code."""
    tso_id = finder.by_region("INVALID-REGION")
    assert tso_id is None

def test_by_tsoid(finder):
    """Test lookup by TSO ID."""
    some_tso = list(finder.tso_details.keys())[0]
    regions = finder.by_tsoid(some_tso)
    assert isinstance(regions, list)
    assert len(regions) > 0

def test_invalid_tsoid(finder):
    """Test lookup with an invalid TSO ID."""
    regions = finder.by_tsoid("INVALID-TSO")
    assert regions is None

def test_by_entsoe_case_insensitive(finder):
    """Test lookup by ENTSO-E code (case-insensitive)."""
    some_tso = list(finder.tso_details.values())[0]
    found_tso = finder.by_entsoe(some_tso.entsoe_code.lower())  # Lowercase input
    assert isinstance(found_tso, Tso)
    assert found_tso.entsoe_code == some_tso.entsoe_code

def test_invalid_entsoe_code(finder):
    """Test lookup with an invalid ENTSO-E code."""
    found_tso = finder.by_entsoe("INVALID-ENTSOE")
    assert found_tso is None
