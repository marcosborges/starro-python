from . import starro
import re


def test_complete():
    assert starro.complete("1234567890") == "**********"


def test_password():
    assert starro.password("P@ssW0rd$@") == "**********"


def test_token():
    assert starro.token("1231asdasd321a3d21654asd") == "************************"


def test_accesskey():
    assert starro.accesskey("321a3d21654as") == "*************"


def test_secret():
    assert starro.secret("6543d21a2") == "*********"


def test_ssn():
    assert starro.ssn("517-90-0243") == "******-0243"


def test_phone():
    assert starro.phone("+55 (11) 9999-9999") == "+** (**) ****-9999"
    

def test_name():
    assert starro.name("Marcos Monteiro Borges") == "M***** M******* B*****"


def test_mail():
    assert starro.mail("contato@marcosborges.com") == "c******@marcosborges.com"


def test_cpf():
    assert starro.cpf("313.789.874-45") == "313.***.***-45"


def test_rg():
    assert starro.rg("34.275.057-4") == "34.***.***-4"


def test_pis():
    assert starro.pis("969.84160.68-4") == "969.*****.**-4"


def test_votercard():
    assert starro.votercard("266547320108") == "266******108"


def test_ie():
    assert starro.ie("009.186.436.570") == "009.***.***.570"


def test_cnh():
    assert starro.cnh("019647647710") == "019*******10"


def test_gender():
    assert starro.gender("male") == '****'


def test_address():
    assert starro.address("7086 S. Trout Rd. West Islip, NY 11795") == '**** S. Trout Rd. West Islip, NY *****'


def test_ethnicity():
    assert starro.ethnicity("italian") == '*******'


def test_religion():
    assert starro.religion("buddhist") == "********"


def test_health():
    assert starro.health("blood A+") == "********"


def test_politic():
    assert starro.politic("anarchist") == "*********"


def test_bank_number():
    assert starro.bank_number("1719") == "17**"


def test_account_number():
    assert starro.account_number("1719396-1") == "17*****-*"


def test_platecar():
    assert starro.platecar("IAF-9941") == "IAF-***1"


def test_creditcard():
    assert starro.creditcard("6666-0000-8888-3232") == "6666-****-****-3232"


def test_sexual():
    assert starro.sexual("heterosexual") == "************"


def test_crm():
    assert starro.crm("A054008") == "A***008"


def test_oab():
    assert starro.oab("UF999999") == "UF****99"


def test_mask_left():
    assert starro.mask_left("Testing mask left", 3) == "***ting mask left"


def test_mask_right():
    assert starro.mask_right("Testing mask right", 3) == "Testing mask ri***"


def test_fix_left():
    assert starro.fix_left("Testing fix left", 3) == "Tes*************"


def test_fix_right():
    assert starro.fix_right("Testing fix right", 3) == "**************ght"


def test_mask_center():
    assert starro.mask_center('completeds', 5) == 'com*****eds'


def test_mask_center_oversize():
    assert starro.mask_center('completeds', 12) == '**********'


def test_fix_center():
    assert starro.fix_center('complete', 4) == '**mple**'


def test_fix_center_oversize():
    assert starro.fix_center('complete', 12) == '********'


def test_starrofy():
    starro.starrofy('complete')
    assert True


def test_starrofy_decorator():
    
    starrofy = starro.starrofy('complete')
    
    def fn2(fn):
        return ""
    
    def fn(fn2):
        return ""

    starrofy(fn(fn2))
    assert True