import logging

class DivisaoPorZeroException(Exception):
    pass

class Calculadora:
    def __init__(self):
        pass

    def add(self, par1, par2):
        return par1 + par2

    def sub(self, par1, par2):
        return par1 - par2

    def mul(self, par1, par2):
        return par1 * par2

    def div(self, par1, par2):
        if par2 == 0.0:
            raise DivisaoPorZeroException("Não é possível dividir por zero")
        elif par1 is None or par2 is None:
            raise ValueError("Os argumentos não podem ser nulos")
        else:
            return par1 / par2

def main():
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger('Calculadora')

    try:
        calc = Calculadora()
        print(calc.add(10.0, 10.0))
        print(calc.sub(10.0, 10.0))
        print(calc.mul(10.0, 10.0))
        # Teste com divisão por zero
        print(calc.div(10.0, 0.0))
    except DivisaoPorZeroException as e:
        logger.error("Erro ao tentar dividir por zero: %s", e)
    except ValueError as e:
        logger.error("Argumentos inválidos: %s", e)
    except Exception as e:
        logger.error("Erro desconhecido: %s", e)

if __name__ == "__main__":
    main()
