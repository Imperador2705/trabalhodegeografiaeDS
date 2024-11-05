policiamento= int(input("De 0 a 10, como você avalia o policiamento no seu bairro?"))
alarmes= int(input("De 0 a 10, como você avalia a quantidade de alarmes nas casas do seu bairro?"))
cameras= int(input("De 0 a 10, como você avalia a quantidade de câmeras nas casas do seu bairro?"))
estrutura= int(input("De 0 a 10, como você avalia a estrutura das casas do seu bairro?"))
vizinhança= int(input("De 0 a 10, como você avalia a colaboração da sua vizinhança para uma maior segurança?"))

resultados=[policiamento,alarmes,cameras,estrutura,vizinhança]

media= sum(resultados) / len(resultados)

if media>=8:
    print("O seu bairro é um bairro bem seguro.")
if media>=5:
    print("O seu bairro é um bairro pouco seguro, procurem tomar medidas como instalar mais câmeras, reformar as edtruturas das casas ou instalar mais alarmes")
if media<5:
    print("O seu bairro não é seguro, sugerimos que contatem uma empresa de segurança para fazer o policiamento no seu bairro.")