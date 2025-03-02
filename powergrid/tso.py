class Tso:
    """Represents a Transmission System Operator (TSO).

    Attributes:
        tso_id (str): Unique internal identifier for the TSO.
        entsoe_code (str): ENTSO-E code for the TSO.
        short_name (str): Short name of the TSO.
        name (str): Full name of the TSO.
        country (str): ISO country code of the TSO.
        operational_status (str): Operational status ("active" or "inactive").
        capacity_mw (int): Capacity of the TSO in megawatts.
        grid_coverage (str): Coverage type ("national" or "regional").
        website (str): Official website URL of the TSO.
        contact_info (str): Contact email or phone number.
        legal_entity_name (str): Legal name of the TSO entity.
        regions (list[str]): List of region codes managed by the TSO.
    """

    def __init__(self, tso_id: str, data: dict):
        """Initializes a TSO object.

        Args:
            tso_id (str): Unique identifier for the TSO.
            data (dict): Dictionary containing TSO attributes.
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
        self.regions = data.get("regions", [])

    def __call__(self) -> str:
        """Returns the TSO ID when the object is called."""
        return self.tso_id

    def __str__(self) -> str:
        """Returns a string representation of the TSO."""
        return f"{self.tso_id} ({self.short_name})"

    def __repr__(self) -> str:
        """Returns a developer-friendly representation of the TSO object."""
        return f"Tso(tso_id={self.tso_id}, name={self.name}, regions={len(self.regions)})"
