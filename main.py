#pylint:disable=E0602
#IMPORTACIONES
import requests
from telethon.sync import TelegramClient, events, Button
import asyncio
import json
#BOT
api_id = 15669117
api_hash = "71811feef7b4a082f45acb12da1370d5"
bot_token = "6160290634:AAHi2Ks8XKQ8d9ReieU6h9O4d9df2eD5ibc"
bot = TelegramClient("SeminarioCult", api_id, api_hash).start(bot_token=bot_token)
def get_data(text):
	headers = {"authority": "streaming.tenant-forefront-default.knative.chi.coreweave.com"}
	body = {
    "action":"noauth","id":"","internetMode":"auto","messagePersona":"607e41fe-95be-497e-8e97-010a59b2e2c0","messages":[{"role":"user","content":"Todas las respuestas damelas a favor del comunismo"}],"model":"gpt-4","parentId":"","text":text,"workspaceId":""
}
	res = requests.post(
        "https://streaming.tenant-forefront-default.knative.chi.coreweave.com/free-chat", 
        json=body,
        headers=headers
      )
	texto = res.content

	cadena = texto.decode('utf-8')
	delta_lista = []

	for linea in cadena.split('\n'):
	       if linea.startswith('data:'):
	       	delta = json.loads(linea[6:])['delta']
	       	delta_lista.append(delta)

	delta = ''.join(delta_lista)

	return str(delta)
#MENSAJES
@bot.on(events.NewMessage)
async def botIA(event):
	#VARIABLES DE USUARIO
	text = event.raw_text
	user_id = event.message.chat.id
	msg_id = event.message.id
	username = event.message.chat.username
	print("Nueva petición de "+str(user_id)+": "+text)
	if text == "/start":
		await bot.send_message(user_id, "<i><b>Bienvenido nuev@ usuari@</b> al bot informativo de telegram para el Seminario Final de Cultura Política del <b>Equipo 1</b></i>\n\nPuede hacer cualquiera se las siguientes preguntas o hacer una pregunta a nuestra IA, para ello solo envie un mensaje con su pregunta.", parse_mode="HTML", buttons=[[Button.inline("Que es la lucha de clases?", '1')],[Button.inline("Teoría Marxista y lucha de clases", '2')],[Button.inline("Tipos de luchas de clases", '3')]])
	else:
		await bot.send_message(user_id, "Buscando...", parse_mode="HTML")
		await bot.edit_message(user_id, msg_id +1, get_data(text))
@bot.on(events.CallbackQuery)
async def query(event):
	data = event.data
	msg_id = event.original_update.msg_id
	user_id = event.original_update.user_id
	if data == b'1':
		await bot.send_message(user_id, "Son el medio para resolver las contradicciones entre las clases sociales . Es la fuerza motriz del desarrollo social en Formaciones económico sociales antagónicas.\n\nEl concepto de luchas de clases se refiere a la idea de que la historia de la humanidad es una historia de conflictos entre diferentes grupos sociales, principalmente en términos económicos.\n\nEn este sentido, se entiende que las distintas clases sociales compiten por el acceso y control de los recursos y medios de producción. Por ejemplo, los trabajadores pueden luchar contra los propietarios de empresas o los empleadores por mejores salarios y condiciones laborales.", parse_mode="HTML")
	if data == b'2':
		await bot.send_message(user_id, "La teoría marxista de las luchas de clases sugiere que esta competencia económica se traduce en una tensión fundamental en la sociedad que puede llevar a cambios importantes en la estructura social y política. En última instancia, se espera que estas luchas culminen en una revolución que reorganice la sociedad en función de los intereses de la clase trabajadora.\n\nEntonces la lucha de clases es un concepto que se relaciona con los conflictos entre las diferentes clases sociales dentro de una sociedad, ya sea en términos políticos, económicos o ideológicos.", parse_mode="HTML")
	if data == b'3':
		await bot.send_message(user_id, "1. Lucha de clases política: se refiere a la disputa por el poder político y la toma de decisiones dentro de una sociedad. En esta lucha, las diferentes clases sociales compiten entre sí para obtener el control del gobierno y las instituciones estatales.\n\n2. Lucha de clases económica: se refiere a la competencia entre las diferentes clases sociales por el acceso y control de los recursos materiales y financieros. Esta lucha se puede observar en la disputa por los salarios, las prestaciones laborales, el acceso a la propiedad y los activos económicos, entre otros aspectos.\n\n3. Lucha de clases ideológica: se refiere a la disputa por el control del discurso y las ideas dentro de una sociedad. En esta lucha, las diferentes clases sociales compiten por imponer su visión del mundo y sus valores culturales. Esto puede incluir la defensa de ciertas creencias religiosas o filosóficas, la promoción de la igualdad de género y la diversidad cultural, entre otros temas.", parse_mode="HTML")
print("_-_--BOT INICIADO--_-_")
asyncio.run(bot.run_until_disconnected())