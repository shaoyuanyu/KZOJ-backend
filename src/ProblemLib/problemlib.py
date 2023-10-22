from dataclasses import dataclass

@dataclass
class ProblemLib():
    id:str
    creater:str
    content:str
    remark:str
    tags:str
    submitCount:int
    acceptedeCount:int
    refAnswer:str
    createTime:str
    difficultLevel:str
    source:str
    outputDiscription:str
    inputDiscription:str