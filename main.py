from utils import PjGenerator

""" Proyect to test https://github.com/pdbpp/pdbpp
"""

""" 
Since pdb++ is not a valid package name the package is named pdbpp:

$ pip install pdbpp
pdb++ is also available via conda:

$ conda install -c conda-forge pdbpp
Alternatively, you can just put pdb.py somewhere inside your PYTHONPATH.
"""

#Breackpoint . stop the execution and use PDB.

#Commands:
    #Use breakpoint() to execute pdbpp.
    #c -> continuos
    #s -> step (get into)
    #sticky [start end] -> interactive view mode.
    #u -> up
    #d -> down
    #PDB POST MORTEN (sin breakpoint): python -m pdb main.py
        #El programa falla, sticky, me lleva donde falla.

if __name__ == '__main__':
    pj = PjGenerator()
    print(pj.show_stats())