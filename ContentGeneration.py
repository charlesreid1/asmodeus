import json
from olipy.queneau import WordAssembler
from olipy.data import load_json
import textwrap

def generate_content():

    assembler = WordAssembler(load_json("dinosaurs.json"))
    
    body = ""

    dinos = []
    for z in range(10):

        dino = assembler.assemble_word()
        if dino[0] in 'AEIO':
            dino = "My favorite dinosaur is an " + dino
        else:
            dino = "My favorite dinosaur is a " + dino
        dinos.append(dino)

    body = "\n\n".join(dinos)
    
    return body

