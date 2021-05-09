from app import db
from app.models import Messages, Platforms, Users, Groups
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from datetime import datetime

def export_msg():
    wb = Workbook()

    filename = 'Messages_{}.xlsx'.format(str(datetime.now()).replace(' ','_'))
    dest_filename = 'excels/{}'.format(filename)

    ws1 = wb.active
    ws1.title = "Messages"


    ws1['A1'] = 'ID'
    ws1['B1'] = 'Text'
    ws1['C1'] = 'Photo'
    ws1['D1'] = 'Audio'
    ws1['E1'] = 'Pdf'
    ws1['F1'] = 'Attachments'
    ws1['G1'] = 'Datetime'
    ws1['H1'] = 'Author'
    ws1['I1'] = 'Group'
    ws1['J1'] = 'Platform'


    messages = Messages.query.all()
    excel_list = []

    i = 0
    for message in messages:
        excel_list.append([])
        excel_list[i].append(message.id)
        excel_list[i].append(message.text)
        excel_list[i].append(message.photo)
        excel_list[i].append(message.audio)
        excel_list[i].append(message.pdf)
        excel_list[i].append(message.attachments)
        excel_list[i].append(message.datetime)
        excel_list[i].append(message.author.phone_number)
        excel_list[i].append(message.group.assigned_name)
        excel_list[i].append(message.group.platform.platform_name)
        i += 1

    for rows in excel_list:
         ws1.append(rows)

    wb.save(filename = dest_filename)
    return filename