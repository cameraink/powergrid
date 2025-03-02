import json
import threading
from typing import Optional, Dict, List
from .tso import Tso

# Define a constant for the JSON data file path
TSO_DATA_FILE = "../data/tso_data.json"

class TsoFinder:
    """Provides lookup functions for Transmission System Operators (TSOs)."""

    def __init__(self):
        """Initializes the TsoFinder and loads data from the default JSON file."""
        self.lock = threading.Lock()
        self.region_to_tso: Dict[str, str] = {}
        self.tso_to_regions: Dict[str, List[str]] = {}
        self.entsoe_to_tso: Dict[str, str] = {}
        self.tso_details: Dict[str, Tso] = {}

        self._load_data()

    def _load_data(self):
        """Loads TSO data from the default JSON file and precomputes reverse lookup mappings."""
        try:
            with open(TSO_DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Normalize region_to_tso to lowercase for case-insensitive lookup
            self.region_to_tso = {region.lower(): tso_id for region, tso_id in data.get("region_to_tso", {}).items()}

            for tso_id, details in data.get("tso_details", {}).items():
                self.tso_details[tso_id] = Tso(tso_id, details)
                self.entsoe_to_tso[details["entsoe_code"].lower()] = tso_id

                # Populate tso_to_regions mapping
                if tso_id not in self.tso_to_regions:
                    self.tso_to_regions[tso_id] = []

                for region, mapped_tso in self.region_to_tso.items():
                    if mapped_tso == tso_id:
                        self.tso_to_regions[tso_id].append(region)

        except FileNotFoundError:
            raise RuntimeError(f"Error: File '{TSO_DATA_FILE}' not found.")
        except json.JSONDecodeError:
            raise RuntimeError(f"Error: Invalid JSON format in '{TSO_DATA_FILE}'.")

    def by_region(self, region_code: str) -> Optional[str]:
        """Finds the TSO ID for a given region code (case-insensitive)."""
        return self.region_to_tso.get(region_code.lower())

    def by_tsoid(self, tso_id: str) -> Optional[List[str]]:
        """Finds all regions managed by a given TSO ID."""
        return self.tso_to_regions.get(tso_id, None)

    def by_entsoe(self, entsoe_code: str) -> Optional[Tso]:
        """Finds TSO details by ENTSO-E code (case-insensitive)."""
        tso_id = self.entsoe_to_tso.get(entsoe_code.lower())
        return self.tso_details.get(tso_id, None)
