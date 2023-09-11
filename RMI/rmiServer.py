import Pyro4


# Classe que contém os métodos remotos
@Pyro4.expose
class MeuObjetoRemoto(object):

  def saudacao(self, nome):
    print(f'{nome} fez chamada')

    return f"Olá, {nome}! Isso foi chamado remotamente."

  def fatorial(self, numero):
    if (numero < 2):
      return numero

    return numero * self.fatorial(numero - 1)


# Inicialize o servidor Pyro4
def iniciar_servidor():
  daemon = Pyro4.Daemon(port=50000)  # Inicializa o daemon
  uri = daemon.register(obj_or_class=MeuObjetoRemoto,
                        objectId="MeuObjetoRemoto")  # Registra o objeto remoto

  print("Servidor RMI está pronto. URI do objeto remoto:", uri)

  daemon.requestLoop()  # Inicia o loop do servidor


if __name__ == "__main__":
  iniciar_servidor()
