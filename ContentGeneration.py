import json
from olipy.queneau import WordAssembler
from olipy.data import load_json
import textwrap

prefix = "/Volumes/noospace/Users/charles/codes/asmodeus/"



def generate_content(topic='dinosaurs'):
    """
    This method generates some text.

    The default topic is dinosaurs. 

    It could use some more arguments:
    - Dinosaurs, or asteroids?
    - Custom text generation modules?
    - Number of lines/items?
    """




    # =================================
    # Assemble Words

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




if __name__=="__main__":
    print generate_content()

