from ..starro.starro import starrofy

class MyClass:
    

    def __init__(self):
        self._fullname = "Marcos Monteiro Borges"
        self._celular = "+55 (11) 99882-6468"
        self._cpf = "313.219.708-46"
        self._ssn = "517-90-0243"
        self._cnpj = "00.313.219/0000-00"
        self._mail = "contato@marcosborges.com"
        self._rg = "24.188.697-1"
        self._cnh = "019647647710"
        self._pis = "969.84160.68-4"
        self._creditcard = "6666-0000-8888-3232"
        self._account_number = "1719396-1"
        self._bank_number = "1719"
        self._platecar = "IAF-9941"
        self._ie = "009.186.436.570"
        self._votercard = "266547320108"
        self._oab="UF999999"
        self._crm="A054008"


    @property
    @starrofy('name')
    def fullname(self):
        return self._fullname


    @property
    @starrofy('phone')
    def celular(self):
        return self._celular


    @property
    @starrofy('cpf')
    def cpf(self):
        return self._cpf


    @property
    @starrofy('mail')
    def mail(self):
        return self._mail


    @property
    @starrofy('rg')
    def rg(self):
        return self._rg
    

    @property
    @starrofy('cnh')    
    def cnh(self):
        return self._cnh
    

    @property
    @starrofy('pis')    
    def pis(self):
        return self._pis
    
    
    @property
    @starrofy('creditcard')    
    def creditcard(self):
        return self._creditcard
    
    
    @property
    @starrofy('account_number')    
    def account_number(self):
        return self._account_number


    @property
    @starrofy('bank_number')    
    def bank_number(self):
        return self._bank_number


    @property
    @starrofy('platecar')    
    def platecar(self):
        return self._platecar


    @property
    @starrofy('ie')    
    def ie(self):
        return self._ie


    @property
    @starrofy('votercard')    
    def votercard(self):
        return self._votercard

    @property
    @starrofy('oab')    
    def oab(self):
        return self._oab

    @property
    @starrofy('crm')    
    def crm(self):
        return self._crm


myClass = MyClass()



print("fullname:" + myClass.fullname + "\n")
print("celular:" + myClass.celular + "\n")
print("cpf:" + myClass.cpf + "\n")
print("mail:" + myClass.mail + "\n")
print("rg:"  + myClass.rg + "\n")
print("cnh:"  + myClass.cnh + "\n")
print("pis:"  + myClass.pis + "\n")
print("mail:"  + myClass.mail + "\n")
print("creditcard:"  + myClass.creditcard + "\n")
print("account_number:"  + myClass.account_number + "\n")
print("bank_number:"  + myClass.bank_number + "\n")
print("platecar:"  + myClass.platecar + "\n")
print("ie:"  + myClass.ie + "\n")
print("votercard:"  + myClass.votercard + "\n")
print("crm:"  + myClass.crm + "\n")
print("oab:"  + myClass.oab + "\n")