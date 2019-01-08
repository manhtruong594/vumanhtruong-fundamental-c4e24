from gmail import GMail, Message
from random import *
import datetime
now = datetime.datetime.now()

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]


html_template = '''
<p>Ch&agrave;o sếp,</p>
<p>S&aacute;ng nay thức <strong>giấc</strong> em bỗng thấy đau bụng cồn c&agrave;o, b&aacute;c sỹ bảo em bị <span style="text-decoration: underline;">{{sickness}}</span>,
sếp cho e nghỉ nh&eacute;!!&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-frown.gif" alt="frown" /></p>
<p>Nh&acirc;n vi&ecirc;n, <em><strong>abcd</strong></em></p>
'''


a = choice(sickness_list)
# print(a)
html_full = html_template.replace("{{sickness}}", a)
print(html_full)



mail = GMail('manhtruong595@gmail.com','bcclnhnc1')
msg = Message("Xin nghỉ", to = "manhtruong594@gmail.com", html=html_full)
if now.hour == 7 and now.minute > 0:
    mail.send(msg)