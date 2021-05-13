from carbonmail.email_sender.manager import initialize as init_sender
from carbonmail.database.initializer import initialize as init_db

init_db()
init_sender()
