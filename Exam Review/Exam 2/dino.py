class Dinosaur:
    def __init__(self, dino_species, plant_eater = True):
        self.species = dino_species
        self.herbivore = plant_eater
        self.period = "Triassic"

    def __str__(self):
        herbs = "ate plants"
        if not self.herbivore:
            herbs = "did not eat plants"
        printable = "The fascinating " + self.species + ", a dinosaur from the " \
                    + self.period + " period, " + herbs
        return printable

def main():
    blue = Dinosaur("Raptor", False)

    dino = Dinosaur("Snorkasaurus", True)

    norbert = Dinosaur("Hungarian", False)

    littlefoot = Dinosaur("Apataosaurus", True)
    
    dinosaurs = [blue, dino, norbert, littlefoot]
    i = 0
    carnies = 0
    while i < len(dinosaurs):
        if not dinosaurs[i].herbivore:
            carnies += 1
        i += 1

    print(i, carnies)

main()
