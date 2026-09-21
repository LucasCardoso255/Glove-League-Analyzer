def build_AP():
    print("Build AP Escolhida")

def build_AD():
    print("Build AD Escolhida")

def escolher_build():
    escolha = input("Escolha AP ou AD: ")

    if escolha == "AP":
        build_AP()
    elif escolha == "AD":
        build_AD()

escolher_build()