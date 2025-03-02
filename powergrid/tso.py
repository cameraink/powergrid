import json

from .constants import TSO_DATA_FILE

class Tso:
    """Represents a Transmission System Operator (TSO).

    This class provides structured access to TSO data, allowing retrieval by ID.

    Attributes:
        tso_id (str): Unique internal identifier for the TSO.
        entsoe_code (str): ENTSO-E code assigned to the TSO.
        short_name (str): Shortened name or acronym of the TSO.
        name (str): Full legal name of the TSO.
        country (str): ISO 3166-1 country code where the TSO operates.
        operational_status (str): Operational status of the TSO (e.g., "active", "inactive").
        capacity_mw (int): Transmission capacity of the TSO in megawatts.
        grid_coverage (str): The extent of the grid coverage (e.g., "national", "regional").
        website (str): Official website URL of the TSO.
        contact_info (str): Contact email or phone number for the TSO.
        legal_entity_name (str): Legal entity name of the organization.
    """

    @staticmethod
    def _load_tso_data() -> dict:
        """Loads the TSO data from the shared JSON file.

        Returns:
            dict: Parsed JSON content containing TSO details.

        Raises:
            RuntimeError: If the JSON file is missing or contains invalid data.
        """
        try:
            with open(TSO_DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("tso_details", {})
        except FileNotFoundError:
            raise RuntimeError(f"Error: File '{TSO_DATA_FILE}' not found.")
        except json.JSONDecodeError:
            raise RuntimeError(f"Error: Invalid JSON format in '{TSO_DATA_FILE}'.")

    def __init__(self, tso_id: str):
        """Initializes a TSO instance by retrieving data from the JSON source.

        Args:
            tso_id (str): Unique identifier of the TSO.

        Raises:
            ValueError: If the TSO ID does not exist in the dataset.

        Example:
            >>> tso = Tso("TSO_FR_001")
        """
        tso_data = self._load_tso_data().get(tso_id)

        if not tso_data:
            raise ValueError(f"TSO ID '{tso_id}' not found in dataset.")

        self.tso_id = tso_id
        self.entsoe_code = tso_data.get("entsoe_code")
        self.short_name = tso_data.get("short_name")
        self.name = tso_data.get("name")
        self.country = tso_data.get("country")
        self.operational_status = tso_data.get("operational_status")
        self.capacity_mw = tso_data.get("capacity_mw")
        self.grid_coverage = tso_data.get("grid_coverage")
        self.website = tso_data.get("website")
        self.contact_info = tso_data.get("contact_info")
        self.legal_entity_name = tso_data.get("legal_entity_name")

    def __call__(self) -> str:
        """Returns the TSO ID when called directly.

        Returns:
            str: The unique TSO identifier.

        Example:
            >>> tso = Tso("TSO_FR_001")
            >>> tso()
            'TSO_FR_001'
        """
        return self.tso_id

    def __str__(self) -> str:
        """Returns a human-readable string representation of the TSO.

        Returns:
            str: A formatted string including the TSO ID and short name.

        Example:
            >>> tso = Tso("TSO_FR_001")
            >>> str(tso)
            'TSO_FR_001 (RTE)'
        """
        return f"{self.tso_id} ({self.short_name})"

    def __repr__(self) -> str:
        """Returns a detailed string representation of the TSO instance.

        Returns:
            str: A string with the TSO ID, name, and key attributes for debugging.

        Example:
            >>> tso = Tso("TSO_FR_001")
            >>> repr(tso)
            "Tso(tso_id='TSO_FR_001', name='Réseau de Transport d'Électricité')"
        """
        return f"Tso(tso_id='{self.tso_id}', name='{self.name}')"
