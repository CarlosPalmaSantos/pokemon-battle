class Move:
    name:str
    description:str
    ptype:str
    power:int
    mtype:str
    attack=lambda x:x
    
    def __init__(self,name:str,ptype:str,power:int,mtype:str) -> None:
        self.name=name
        self.ptype=ptype
        self.power=power
        self.mtype=mtype
        
        
