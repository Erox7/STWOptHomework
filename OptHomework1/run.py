import telebot
import clientwebparse

tb = telebot.TeleBot('370811729:AAHo1_67fcxo3ZVBwxu_5j767i8Bt5RsEOw')

@tb.message_handler(commands=["start"])
def listener(mensaje):  #Cuando llega un mensaje se ejecuta esta funcion
    client = clientwebparse.Client()
    book = client.get_book()
    for m in mensaje:

        tb.send_message(m.chat.id, book)


tb.set_update_listener(listener) #registrar la funcion listener
tb.polling()
