#--> A importância de deixar o código mais legível:
velocidade = 40
local_carro = 101

RADAR_1 = 80
LOCAL_1 = 100
RADAR_RANGE = 1

carro_passando_radar_1 = local_carro >= LOCAL_1 - RADAR_RANGE and local_carro <= LOCAL_1 + RADAR_RANGE
carro_passou_radar_1 = local_carro > LOCAL_1  + RADAR_RANGE

velocidade_ultrapassada_radar_1 = velocidade >= RADAR_1
multa_para_radar_1 = carro_passando_radar_1 and velocidade_ultrapassada_radar_1

print("-="*30)
if carro_passando_radar_1 or carro_passou_radar_1:
    print("Carro passou pelo radar 1.")
else:
    print("Carro não passou pelo radar 1.")

if multa_para_radar_1:
    print("Velocidade permitida do radar 1 foi ultrapassada. Multa a pagar.")
else:
    print("Velocidade do radar 1 não ultrapassada.")
print("-="*30)