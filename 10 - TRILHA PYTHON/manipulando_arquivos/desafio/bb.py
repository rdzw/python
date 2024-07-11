class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, numero_destino, duracao_chamada):
        if self.plano.verificar_saldo_suficiente(duracao_chamada):
            custo = self.plano.custo_chamada(duracao_chamada)
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {numero_destino} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def verificar_saldo_suficiente(self, duracao_chamada):
        custo = self.custo_chamada(duracao_chamada)
        return self.saldo >= custo

    def custo_chamada(self, duracao_chamada):
        return duracao_chamada * 0.10

    def deduzir_saldo(self, valor):
        self.saldo -= valor
        return self.saldo

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)

destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
