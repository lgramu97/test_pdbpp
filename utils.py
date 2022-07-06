from random import randint

class Stats():

    def __init__(self) -> None:
        self.stats_name = ['Fuego', 'Agua', 'Tierra']
        self.stat_lst = self._generate()

    
    def _get_single_stat(self,default=True):
        """Rol dices and returns the sum of best 3
        """
        if default:
            #ret = [randint(1, 6) for i in range(4)].sort() #Mal, se puede ver en el debugger.
            ret = [randint(1, 6) for i in range(4)]
            ret.sort()
            return sum(ret[1:])
        else:
            ret = [0 for i in range(4)] 
            ret.sort()
            return sum(ret[1:])

    def _generate(self):
        """Iterate over all the stat names and returns a dictionary
        """
        return {s: self._get_single_stat() for s in self.stats_name}



class PjGenerator:
    
    def __init__(self) -> None:
        """Start the player
        """
        self._stats = Stats()

    def show_stats(self):
        """Return a dictionary with the stats of your player
        """
        return self._stats.stat_lst