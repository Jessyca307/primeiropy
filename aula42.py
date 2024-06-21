cpf = '746.824.890-70'.replace('.', '').replace('-', '')
nove_digitos = cpf[:9]
contador_r = 10

resultado = 0
for digito in nove_digitos:
          resultado += int(digito) * contador_r
          contador_r -= 1

digito_2 = (resultado * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0


cpf = '74682489070'
nove_digitos = cpf[:9]
contador_r_2 = 11

resultado_1 = 0
for digito in nove_digitos:
          resultado += int(digito) * contador_r_2
          contador_r_2 -= 1

digito_3 = (resultado * 10) % 11
digito_3 = digito_3 if digito_3 <= 9 else 0
novo_cpf = str(digito_2) + str(digito_3)
digito_final = int(novo_cpf)
print(digito_final)

cpf_gerado_p_c = f'{nove_digitos}{digito_2}{digito_3}'

if cpf == cpf_gerado_p_c:
        print(f'{cpf} é valido')

else: 
        print('CPF invalido')
