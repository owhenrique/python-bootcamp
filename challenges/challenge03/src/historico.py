from datetime import datetime

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        data_transacao = datetime.now()
        self.transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': data_transacao.strftime("%d/%m/%Y %I:%H%p")
        })