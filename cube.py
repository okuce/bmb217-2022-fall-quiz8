from square import Square

class Cube:
    """Cube class inherited from square class"""
    
    def __init__(self, a) -> None:
        """constructor of a cube 
            it calls constructor of super
        Args:
            a (int): one side of a cube
        """


    def get_volume(self):
        """calculates volume of cube 

        Returns:
            int: volume of cube
        """


    def __str__(self) -> str:
        """dunder str

        Returns:
            str: 'Shape:<shape name>,volume:<volume of cube>'
        """
