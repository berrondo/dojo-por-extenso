por_extenso = {
     0 : '', 
     1 : 'um', 2 : 'dois', 3 : 'tres', 4 : 'quatro', 
          6 : 'seis', 7 : 'sete', 8 : 'oito', 9 : 'nove',
     10 : 'dez', 11: 'onze', 13 : 'treze', 15 : 'quinze', 17 : 'dezessete', 19 : 'dezenove', 
     20 : 'vinte', 30 : 'trinta', 50 : 'cinquenta', 
          60 : 'sessenta', 70 : 'setenta', 80 : 'oitenta', 90: 'noventa', 
     100 : 'cento', 200 : 'duzentos', 300 : 'trezentos', 400 : 'quatrocentos', 500 : 'quinhentos', 
          600 : 'seiscentos', 
  }
  
def converter_digito_a_digito(os_digitos):
    numero = int(os_digitos)
    if numero < 20: return [por_extenso[numero]]
    if numero == 100: return ['cem']
    
    return reversed(filter(bool, [por_extenso[int(digito)*10**ordem] 
                                  for ordem, digito in enumerate(reversed(os_digitos))]))
    
def a_conversao_d(os_digitos, o_singular='', o_plural=''):
    if os_digitos == '1': return o_singular
    if os_digitos == '000': return ''
    return ' e '.join(converter_digito_a_digito(os_digitos)) + o_plural
    
na_ordem_d = { # a grandeza especifica com singular e plural apropriados:
    0: ('um', ''),
    1: ('mil', ' mil'),
    2: ('um milhao', ' milhoes'),
    3: ('um bilhao', ' bilhoes'),
    4: ('um trilhao', ' trilhoes'),
  }
  
def em_grupos_de_tres_a(parte_inteira, digitos=''):
    def formou_grupo_de_tres(essa_vez):
        return (essa_vez+1) % 3 == 0
    
    for essa_vez, digito in enumerate(reversed(parte_inteira)):
        digitos = digito + digitos
        
        if formou_grupo_de_tres(essa_vez):
            digitos = '.' + digitos
            
    return reversed(digitos.strip('.').split('.'))
    
def frasear(valor_convertido, e_centavos):

    if len(valor_convertido) == 1:
        por_extenso = valor_convertido[0]
    else:
        por_extenso = ' e '.join((', '.join(reversed(valor_convertido[1:])), 
                                  valor_convertido[0]))
                             
    if por_extenso == 'um': 
        por_extenso += ' real'
    elif por_extenso.endswith(('milhao', 'bilhao', 'milhoes', 'bilhoes', 'trilhoes')): 
        por_extenso += ' de reais'
    else: 
        por_extenso += ' reais'
    
    
    if not e_centavos:
        return por_extenso
        
    else:
        if e_centavos == 'um':
            e_centavos += ' centavo'
        else:
            e_centavos += ' centavos'
        return ' e '.join((por_extenso, e_centavos))
    
def valor_por_extenso_de(um_numero):
    parte_inteira, os_centavos = str(um_numero).split('.')
    print parte_inteira, os_centavos
        
    return frasear(filter(bool, [a_conversao_d(a_centena, *na_ordem_d[a_grandeza]) 
                                 for a_grandeza, a_centena in enumerate(em_grupos_de_tres_a(parte_inteira))]),
                                 # e
                                 a_conversao_d(os_centavos[:2]))
    