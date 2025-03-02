from powergrid.tso_finder import TsoFinder

finder = TsoFinder()

# Find TSO by region
print(f'\n- The TSO for the region code ‘FR-IDF‘ is {finder.by_region("FR-IDF")}')  # Output: "TSO_FR_001"
print(f'- The TSO for the region code ‘fr-idf‘ is {finder.by_region("fr-idf")}')  # Output: "TSO_FR_001"

# Unkown region code
print(f'\n- The TSO for the region code ‘ab-cd‘ is {finder.by_region("ab-cd")}')  # Output: None

# Get TSO details
print(f'\n- The region codes for the TSO ID ‘TSO_FR_001‘ is {finder.by_tsoid("TSO_FR_001")}')  #  Output: List of regions

# Find TSO by ENTSO-E code
print(f'\n- The Tso ID for the ENTSOE code ‘10YFR-RTE------C‘ is {finder.by_entsoe("10YFR-RTE------C")}')   # Output: Tso object for RTE
