import warnings
warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning, module not import", ImportWarning)


class BuildingWarning(Exception):

    def __str__(self):
        return f"With so much material the house cannot be build"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        warnings.warn(BuildingWarning(amount_of_material))


material = 120
check_material(material, 300)