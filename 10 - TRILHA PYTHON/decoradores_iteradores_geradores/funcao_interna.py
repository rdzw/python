def principal():
    print("Executando a função principal")
    
    def funcao_interna():
        print("Executando funcção interna")
        
    def funcao_2():
        print("Executando a funcao 2")
        
        funcao_interna()
        funcao_2()
    
principal()