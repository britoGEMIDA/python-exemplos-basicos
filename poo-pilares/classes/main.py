from classes.cachorro import cachorro
from classes.gato import gato

# função para demonstrar polimorfismo 
def emitir_som(animal):
    print("f{animal.get_nome()} faz: {animal.fazer_som()}")
    print(" ")

    def main():
        #criando instancias (objetos) das classes
        rex = cachorro("rex", "labrator")
        mimi = gato ("mimi", "branco.")
        
        # demonstrando o funcionamento
        print(" ")
        print(f"raça do cachorro{rex.get_more()}")
        print(f"raça do cachorro{rex.raca()}")
        print(" == 2DE == DEVs Python : )")
        print(f"nome do gato{mimi.get_nome()}")
        print(f"cor do gato{mimi.cor()}")
        print(" ")

        emitir_som(rex)
        emitir_som(mimi)

    if __name__=="__main__":
            main()