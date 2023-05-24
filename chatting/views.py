from django.shortcuts import render


def chat_box(reqquest, chat_box_name):
    return render(reqquest, 'chatting/chat_box.html', {
        'chat_box_name': chat_box_name
    })
