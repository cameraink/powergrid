class Tso:
    """Represents a Transmission System Operator (TSO).

    A TSO manages electricity transmission networks within specific regions.
    This class provides structured access to TSO data, including operational
    status, capacity, and region coverage.

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

    def __init__(self, tso_id: str, data: dict):
        """Initializes a TSO instance with provided data.

        Args:
            tso_id (str): Unique identifier of the TSO.
            data (dict): Dictionary containing the TSO details.

        Example:
            >>> data = {
            ...     "entsoe_code": "10YFR-RTE------C",
            ...     "short_name": "RTE",
            ...     "name": "Réseau de Transport d'Électricité",
            ...     "country": "FR",
            ...     "operational_status": "active",
            ...     "capacity_mw": 105000,
            ...     "grid_coverage": "national",
            ...     "website": "https://www.rte-france.com",
            ...     "contact_info": "contact@rte-france.com",
            ...     "legal_entity_name": "RTE Réseau de Transport d'Électricité"
            ... }
            >>> tso = Tso("TSO_FR_001", data)
        """
        self.tso_id = tso_id
        self.entsoe_code = data.get("entsoe_code")
        self.short_name = data.get("short_name")
        self.name = data.get("name")
        self.country = data.get("country")
        self.operational_status = data.get("operational_status")
        self.capacity_mw = data.get("capacity_mw")
        self.grid_coverage = data.get("grid_coverage")
        self.website = data.get("website")
        self.contact_info = data.get("contact_info")
        self.legal_entity_name = data.get("legal_entity_name")

    def __call__(self) -> str:
        """Allows the object to be called directly, returning the TSO ID.

        Returns:
            str: The unique TSO identifier.

        Example:
            >>> tso = Tso("TSO_FR_001", {})
            >>> tso()
            'TSO_FR_001'
        """
        return self.tso_id

    def __str__(self) -> str:
        """Returns a human-readable string representation of the TSO.

        Returns:
            str: A formatted string including the TSO ID and short name.

        Example:
            >>> tso = Tso("TSO_FR_001", {"short_name": "RTE"})
            >>> str(tso)
            'TSO_FR_001 (RTE)'
        """
        return f"{self.tso_id} ({self.short_name})"

    def __repr__(self) -> str:
        """Returns a detailed string representation of the TSO instance.

        Returns:
            str: A string with the TSO ID, name, and key attributes for debugging.

        Example:
            >>> tso = Tso("TSO_FR_001", {"name": "Réseau de Transport d'Électricité"})
            >>> repr(tso)
            "Tso(tso_id='TSO_FR_001', name='Réseau de Transport d'Électricité')"
        """
        return f"Tso(tso_id='{self.tso_id}', name='{self.name}')"
