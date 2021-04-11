# STARRO

![Starro](https://raw.githubusercontent.com/marcosborges/starro-python/master/assets/starro.png)


Starro is a facilitator to overshadow sensitive information.

It reduces the brain overload inherent in the Regex complexity, bringing several commands closer to human language.


## how to install?

**Pip:**
```
    pip install starro
```

**Poetry:**
```
    poetry add starro
```

---

## how it works?

### Basic usage

```python
from starro import starro

password = "MyP@ssW0r$"
print(starro.password(password))
#prints:    **********

token =  "3hjsdf67kajh8990s5dff0lk5sdfsfhjks8923"
print(starro.secret(token))
#prints:  **************************************

fullname = "Marcos Monteiro Borges"
print(starro.name(fullname))
#prints:    M***** M******* B*****

mail =   "contato@marcosborges.com "
print(starro.mail(mail))
#prints:  c******@marcosborges.com

phone =  "+55 (11) 9999-9999"
print(starro.phone(phone)) 
#prints: "+** (**) ****-9999"

creditcard = "6666-0000-8888-3232"
print(starro.creditcard(creditcard))
#prints: "6666-****-****-3232"

cpf =    "313.789.874-45"
print(starro.cpf(cpf))
#prints: "313.***.***-45"

rg =     "34.275.057-4"
print(starro.rg(rg))
#prints: "34.***.***-4"

# Others examples
assert starro.complete("1234567890") == "**********"
assert starro.mask_left("Testing mask left", 3) == "***ting mask left"
assert starro.mask_right("Testing mask right", 3) == "Testing mask ri***"
assert starro.fix_left("Testing fix left", 3) == "Tes*************"
assert starro.fix_right("Testing fix right", 3) == "**************ght"
assert starro.mask_center('completeds', 5) == 'com*****eds'
assert starro.mask_center('completeds', 12) == '**********'
assert starro.fix_center('complete', 4) == '**mple**'
assert starro.fix_center('complete', 12) == '********'


```

### Decorator usage

```python
from starro.starro import starrofy

class MyClass:

    @property
    @starrofy('name')
    def fullname(self):
        return self._fullname


    @property
    @starrofy('phone')
    def phone(self):
        return self._phone

    
    @property
    @starrofy('email')
    def mail(self):
        return self._email

    
    @property
    @starrofy('password')
    def password(self):
        return self._password



myClass = MyClass()

myClass.fullname = "Full Name User"
myClass.phone = "+55 11 99999-9999"
myClass.cpf = "313.313.313-32"
myClass.mail = "contato@marcosborges.com"
myClass.creditcard = "2080-1408-0210-3005"


print("fullname:" + myClass.fullname + "\n")
print("phone:" + myClass.phone + "\n")
print("cpf:" + myClass.cpf + "\n")
print("mail:" + myClass.mail + "\n")
print("creditcard:"  + myClass.creditcard + "\n")

```
---

## What are the dependencies?

- Core
    - python = "^3.6"
        - re
        - math
- Develop
    - pytest = "^6.2.2"
    - coverage = "^5.5"
    - pylint = "^2.7.2"
    - bandit = "^1.7.0"
    - flake8 = "^3.9.0"
    - dependency-check = "^0.5.0"


---


---
## QualityGate


**[SonarCloud](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)** 

<p align=center>
  <img src="https://sonarcloud.io/api/project_badges/quality_gate?project=marcosborges_starro-python" />
</p>


[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=bugs)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=code_smells)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=coverage)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=duplicated_lines_density)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python) [![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=ncloc)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=alert_status)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=security_rating)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python) [![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=sqale_index)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=marcosborges_starro-python&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=marcosborges_starro-python)





---
