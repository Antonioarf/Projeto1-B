from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''
    tag:str = ''
    prazo: str = ''
    feito:bool = None