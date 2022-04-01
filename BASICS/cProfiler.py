"""
title：profile 性能调试
writer：山客
date：2022.4.1
"""

import cProfile
import pstats, io
from pstats import SortKey

class pro(object):
    def __init__(self):
        self.pr = None
    
    def start(self):
        self.pr = cProfile.Profile()
        self.pr.enable()
    
    def end(self):   
        self.pr.disable()

        sio = io.StringIO()  # must using io
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(self.pr, stream=sio).sort_stats(sortby)
        
        import time
        ps.dump_stats(filename=str(int(time.time())) + "-profile.cprofile")
        
        # ps.print_stats()
        # print(sio.getvalue())
        
        self.pr = None
