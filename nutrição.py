animes = {
    "black clover" : {
        "nome original" : "black Clover",
        "temporadas" : "2",
        "restrição" : "16",
        "lançamento" : "2017",
        "autor" : "yūki tabata",
    },
    "street fighter II": {
        "nome original" : "street fighter II",
        "temporadas" : "1",
        "restrição" : "l",
        "lançamento" : "1995",
        "autor" : "gisaburo sugii",
    },
    "attack on titan" : {
        "nome original": "shingeki no kyojin",
        "temporadas" : "5",
        "restrição" : "L", 
        "lançamento" : "2017",
        "autor" : "Hajime Isayama",
    },  
    "hunter  hunter" : {
        "nome original" : "hunter hunter",
        "temporadas" : "2",
        "restrição" : "l",
        "lançamento" : "1998",
        "autor" : "yoshihiro togashi",
    },
     "one piece" : {
        "nome original" : "One piece",
        "temporadas" : "50",
        "restrição" : "l",
        "lançamento" : "1999",
        "autor" : "Eichiro oda",
     },
 
    "dragon ball super": {
        "nome original" : "dragon ball super",
        "temporadas": "2",
        "restrição" : "l",
        "lançamento" : "2015",
        "autor" : "akira toriyama",
    },
    "dragon ball super": {
       "nome original" : "dragon ball super",
       "temporadas" : "2",
       "restrição" : "l",
       "lançamento" : "2015",
       "autor" : "akira toriyama",
    },
    "Dragon Ball Z": {
        "nome original": "dragon ball z",
        "temporadas": "9",
        "restrição": "l",
        "lançamento": "1989",
        "autor": "akira toriyama,",
    },
    "dragon ball kai": {
     "nome original": "dragon ball kai",
     "temporadas": "5",
     "restrição": "l",
     "lançamento": "2009",
     "autor": "akira toriyama",
    },
    "dragon ball gt": {
     "nome original": "dragon ball gt",
     "temporadas" : "3",
     "restrição": "l",
     "lançamento": "1996",
     "autor": "akira toriyama",
    },
}
def exibir(nome):
    if nome in animes:
        anime = animes[nome]
        print(f"nome: {nome}")
        print(f"nome original: {anime['nome original']}")
        print(f"Temporadas: {anime['temporadas']}")
        print(f"Restrição: {anime['restrição']}")
        print(f"Lançamento: {anime['lançamento']}")
        print(f"Autor: {anime['autor']}")
    else:
        print("anime não encontrado")
    
nome_anime = input("Digite um anime bom:").lower()

exibir(nome_anime)
      
     
    
  
    
 