import efuntool.efuntool as eftl
import coopy
import elist.elist as elel

class Symbol():
    def __init__(self,s):
        self.s = s
    def __repr__(self):
        return('|'+s+'|')

@eftl.inplace_wrapper
def add_dots(opts):
    nopts = copt.deepcopy(opts)
    opts = elel.map(opts,lambda ele:Symbol("."+ele))
    nopts.extend(opts)
    return(nopts)



