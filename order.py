import PySimpleGUI as sg

DISH_NUM = 12
dish_name = ['披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司']


layout= []
layout += [sg.Text('面馆', font='Any 30')],
for i in range(1, 3):
    layout += [sg.Image(f'./img/food{i+1}.png', size=(200,200)), sg.Text(dish_name[i], font='Any 20')],

window = sg.Window('菜单', layout)
event, values = window.read()

#window.close()

'''
    [sg.Image(filename=img1, size=(200,200), enable_events=True), sg.Text('披萨')],
    [sg.Image(filename=img2, size=(200,200)), sg.Text('香蕉')],
    [sg.Image(filename=img3, size=(200,200)), sg.Text('汉堡')],
    [sg.Image(filename=img4, size=(200,200)), sg.Text('吐司')],
'''