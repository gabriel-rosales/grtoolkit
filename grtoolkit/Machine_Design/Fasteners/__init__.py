def screwThreadEngagement(diameter, screw="steel", substrate="aluminium"):
    if substrate == "aluminium":
        return 2*diameter
    if substrate == "steel" or substrate == "iron" or substrate == "brass" or substrate == "bronze":
        return 2*diameter