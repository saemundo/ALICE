class _search:
    def __init__(self,*args,**kwargs):
        pass
    
class RabbitHole(_search):
    """ The RabbitHole search algorithm will drag the search further and further
        into insanity and utilise solutions from all of the other algorithms""" 
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        
class ShrinkingTears(_search):
    """ The ShrinkingTears search algorithm's each iteration will produce 
        a smaller and smaller solution while preserving sadness"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

class WhiteRabbit(_search):
    """ The WhiteRabbit will circularly reference the RabbitHole search but will
        always return solutions slower"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
class Caterpillar(_search):
    """ The Caterpillar search will produce solutions that are difficult to comprehend
        and will often be a problem themselves"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
class TeaParty(_search):
    """ The TeaParty search will produce randomly shuffled solutions unless the
        parameter *where* is set to MURICA then it will be heavily biased towards
        inbred solutions """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
class QueenOfCards(_search):
    """ The QueenOfCards search will only return partial solutions """
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        

    