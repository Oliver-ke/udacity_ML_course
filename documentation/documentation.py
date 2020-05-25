

# this is an inline documentation using inline comments

#maximum valve threshold level
valveThreshold = 0.89


#Doc string, this type is uesd for classes, functions and module
def populationDensity(population, landArea):
    """Calculate the population density of an area.
    
    Args:
    population: int. the population of the area
    landArea: int or float. This function is unit-agnostic, if you
    pass a value in term of square miles the function will return
    a density in those unit

    Returns:
    populationDensity: population/landArea. The population density
    of a particular area
    """
    return population / landArea

#Project documentation
"""
Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or developers who may contribute to your code. A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.

Whether it's an application or a package, your project should absolutely come with a README file. At a minimum, this should explain what it does, list its dependencies, and provide sufficiently detailed instructions on how to use it. You want to make it as simple as possible for others to understand the purpose of your project, and quickly get something working.
"""
