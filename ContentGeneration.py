import json
from olipy.queneau import Assembler, WordAssembler
from olipy.data import load_json
import textwrap

prefix = "/Volumes/noospace/Users/charles/codes/asmodeus/"


def generate_content(nitems=1):
    """
    This method generates some text about
    dinosaurs and asteroids.

    - Number of lines/items = 1
    """

    body = ""

    # =================================
    # Asteroids

    body += "Asteroid of the Day: "

    corpus = Assembler.load(open("olipy/data/minor_planets.min.json"), tokens_in='citation')

    sentences = []
    names = []
    for sentence, source in corpus.assemble("f.l", min_length=4):
        sentences.append(sentence)
        names.append(source['name'])

    # Make a new assembler from the names of the asteroids that were chosen.
    name_assembler = WordAssembler(names)
    name = name_assembler.assemble_word()

    asteroid = name
    asteroid += "\n"*2

    for s in " ".join(sentences):
        asteroid += s

    body += asteroid 
    body += "\n"*2

    # =================================
    # Dinosaurs

    body += "In an alternate universe, this asteroid would have annihilated the following dinosaur species:"
    body += "\n"*2

    assembler = WordAssembler(load_json("dinosaurs.json"))
    
    dinos = []
    for z in range(20):

        dino = assembler.assemble_word()
        if dino[0] in 'AEIO':
            dino = "* " + dino
        else:
            dino = "* " + dino
        dinos.append(dino)

    body += "\n".join(dinos)

    # ===============================
    
    return body




if __name__=="__main__":
    print generate_content()

