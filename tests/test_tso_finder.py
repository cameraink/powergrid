import pytest
from powergrid.tso_finder import TsoFinder
from powergrid.tso import Tso

@pytest.fixture(scope="module")
def finder():
    """Initialize TsoFinder with the default dataset."""
    return TsoFinder()

def test_by_region_case_insensitive(finder):
    """Test lookup by region code (case-insensitive), returning a Tso object."""
    region_code = "fr-idf"  # Lowercase input
    tso = finder.by_region(region_code)
    assert isinstance(tso, Tso)
    assert tso.tso_id == "TSO_FR_001"

def test_by_region_without_entsoe(finder):
    """Test lookup by region code without entseo code, returning a Tso object."""
    region_code = "fr-cor"  # Lowercase input
    tso = finder.by_region(region_code)
    assert isinstance(tso, Tso)
    assert tso.tso_id == "TSO_FR_COR"

def test_invalid_region_code(finder):
    """Test lookup with an invalid region code should return None."""
    tso = finder.by_region("INVALID-REGION")
    assert tso is None

def test_by_tsoid(finder):
    """Test lookup by TSO ID returns a list of region codes."""
    some_tso = "TSO_FR_001"
    regions = finder.by_tsoid(some_tso)
    assert isinstance(regions, list)
    assert len(regions) > 0

def test_invalid_tsoid(finder):
    """Test lookup with an invalid TSO ID should return None."""
    regions = finder.by_tsoid("INVALID-TSO")
    assert regions is None

def test_by_entsoe_case_insensitive(finder):
    """Test lookup by ENTSO-E code (case-insensitive), returning a Tso object."""
    entsoe_code = "10YFR-RTE------C"
    tso = finder.by_entsoe(entsoe_code.lower())  # Lowercase input
    assert isinstance(tso, Tso)
    assert tso.entsoe_code == entsoe_code

def test_invalid_entsoe_code(finder):
    """Test lookup with an invalid ENTSO-E code should return None."""
    tso = finder.by_entsoe("INVALID-ENTSOE")
    assert tso is None
