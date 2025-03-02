import json
import threading
from typing import Optional, Dict, List

from .tso import Tso
from .constants import TSO_DATA_FILE

class TsoFinder:
    """A high-performance lookup utility for Transmission System Operators (TSOs).

    This class provides efficient lookup methods for retrieving TSO information based on:
    - Region codes (ISO 3166-2)
    - TSO IDs
    - ENTSO-E codes

    The data is preloaded into memory for fast access and supports case-insensitive searches.

    Attributes:
        region_to_tso (dict): Maps region codes (lowercase) to TSO IDs.
        tso_to_regions (dict): Maps TSO IDs to a list of associated region codes.
        entsoe_to_tso (dict): Maps ENTSO-E codes (lowercase) to TSO IDs.
        lock (threading.Lock): Ensures thread safety when accessing lookup data.
    """

    def __init__(self):
        """Initializes the TsoFinder instance and loads data from the shared JSON file.

        Raises:
            RuntimeError: If the JSON file is missing or contains malformed data.
        """
        self.lock = threading.Lock()
        self.region_to_tso: Dict[str, str] = {}
        self.tso_to_regions: Dict[str, List[str]] = {}
        self.entsoe_to_tso: Dict[str, str] = {}

        self._load_data()

    def _load_data(self):
        """Loads TSO data from the JSON file and precomputes reverse lookup mappings.

        This method reads the JSON file specified in `TSO_DATA_FILE` and populates the lookup
        dictionaries for efficient searches.

        Raises:
            RuntimeError: If the JSON file cannot be loaded or contains invalid data.
        """
        try:
            with open(TSO_DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Normalize region_to_tso to lowercase for case-insensitive lookup
            self.region_to_tso = {region.lower(): tso_id for region, tso_id in data.get("region_to_tso", {}).items()}

            for tso_id, details in data.get("tso_details", {}).items():
                # Use the new Tso constructor to fetch details dynamically
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

    def by_region(self, region_code: str) -> Optional[Tso]:
        """Retrieves the TSO object for a given region code.

        This lookup is case-insensitive.

        Args:
            region_code (str): The ISO 3166-2 region code.

        Returns:
            Optional[Tso]: The corresponding Tso object if found, otherwise None.

        Example:
            >>> finder = TsoFinder()
            >>> finder.by_region("FR-IDF")
            Tso(tso_id='TSO_FR_001', name='Réseau de Transport d'Électricité')
        """
        tso_id = self.region_to_tso.get(region_code.lower())
        return Tso(tso_id) if tso_id else None

    def by_tsoid(self, tso_id: str) -> Optional[List[str]]:
        """Retrieves the list of region codes associated with a given TSO ID.

        Args:
            tso_id (str): The unique TSO identifier.

        Returns:
            Optional[List[str]]: A list of region codes if the TSO exists, otherwise None.

        Example:
            >>> finder = TsoFinder()
            >>> finder.by_tsoid("TSO_FR_001")
            ['FR-IDF', 'FR-ARA', 'FR-PAC']
        """
        return self.tso_to_regions.get(tso_id, None)

    def by_entsoe(self, entsoe_code: str) -> Optional[Tso]:
        """Retrieves a TSO object using an ENTSO-E code.

        This lookup is case-insensitive.

        Args:
            entsoe_code (str): The ENTSO-E identifier.

        Returns:
            Optional[Tso]: A Tso object containing details if found, otherwise None.

        Example:
            >>> finder = TsoFinder()
            >>> finder.by_entsoe("10YFR-RTE------C")
            Tso(tso_id='TSO_FR_001', name='Réseau de Transport d'Électricité')
        """
        tso_id = self.entsoe_to_tso.get(entsoe_code.lower())
        return Tso(tso_id) if tso_id else None
