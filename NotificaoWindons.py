from winotify import Notification, audio

notificacao = Notification(app_id="Código Python",
                           title="Notificação", msg="Vamos parar de Procastinar !!! \nVamos Estudar PYTHON !!!",
                           duration="long", icon=r"C:\Users\user\OneDrive\Imagens\HenryIcon.jpg")

notificacao.set_audio(audio.LoopingCall5, loop=False)
notificacao.add_actions(label="Estudar Python",
                        launch="https://portalhashtag.com/login")

notificacao.show()
