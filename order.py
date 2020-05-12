import PySimpleGUI as sg

DISH_NUM = 12
dish_name = ['披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司']

def confirm_order():
    sg.popup('下单成功')
    # 向数据库写入订单数据
    reset_all()
    
    # 切换到‘确认界面’

def reset_all():
    # 初始化菜单界面
    pass

def one_food(i):
    layout = [
        sg.Image(f'./img/food{i+1}.png', size=(200,200)), 
        sg.Text(dish_name[i], font='Any 20'),
        #sg.Button(image_filename='./img/other/plus.png')
    ],
    return layout

menu_layout= []
menu_layout += [sg.Text('面馆', font='Any 30')],
for i in range(1, 3):
    menu_layout += one_food(i)
menu_layout += [sg.Button('确认选择'), sg.Button('清除所有')],

confirm_layout= []

layout = [[sg.TabGroup([[sg.Tab('菜单', menu_layout), sg.Tab('确认界面', confirm_layout)]])]]

window = sg.Window('菜单', layout)

# make window unclosed
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '确认选择':
        confirm_order()
    elif event =='清除所有':
        reset_all()

window.close()

'''
    [sg.Image(filename=img1, size=(200,200), enable_events=True), sg.Text('披萨')],
    [sg.Image(filename=img2, size=(200,200)), sg.Text('香蕉')],
    [sg.Image(filename=img3, size=(200,200)), sg.Text('汉堡')],
    [sg.Image(filename=img4, size=(200,200)), sg.Text('吐司')],
'''