class Cpf(object):
    cpf = str

    def __init__(self):
        self.cpf

    def lerCpf(self):
        while True:
            try:
                self.cpf = str(input("Digite: "))
                break
            except:
                print("Apenas caracteres numéricos!, Tente novamente.")
        Cpf.valida(self)

    def valida(self):
        if len(self.cpf) != 11 or Cpf.gluglu_ieie(self) == True:
            Cpf.invalid(self)
        elif self.cpf[9] != str(Cpf.segmenta_1(self)) or self.cpf[10] != str(Cpf.segmenta_2(self)):
            Cpf.invalid(self)
        else:
            print("CPF Válido!")

    def exibe(self):
        print(self.cpf)

    def invalid(self):
        print("CPF inválido, tente novamente...")
        Cpf.lerCpf(self)

    def segmenta_1(self):
        i = 10
        cpf_str = str(self.cpf)
        digitos = []
        for letra in cpf_str:
            try:
                num = int(letra)
                digitos.append(num)
            except ValueError as v:
                pass

        soma = 0
        for digito in digitos:
            soma += digito * i
            i = i - 1
            if i == 1:
                break
        return soma * 10 % 11

    def segmenta_2(self):
        i = 11
        cpf_str = str(self.cpf)
        digitos = []
        for letra in cpf_str:
            try:
                num = int(letra)
                digitos.append(num)
            except ValueError as v:
                pass

        soma = 0
        for digito in digitos:
            soma += digito * i
            i = i - 1
            if i == 1:
                break
        return soma * 10 % 11

    def gluglu_ieie(self):
        elem = self.cpf[0]
        for x in self.cpf:
            if x == elem:
                malandro = True
            else:
                malandro = False
        return malandro


class Main():

    def main(self):
        chk = Cpf()
        chk.lerCpf()


m = Main()
m.main()
