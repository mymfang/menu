import PySimpleGUI as sg

DISH_NUM = 12
dish_name = ['披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司','披萨', '香蕉', '汉堡','吐司']

def confirm_order():
    sg.popup('下单成功', font='Any 15')
    # 向数据库写入订单数据
    reset_all()
    
    # 切换到‘确认界面’

def reset_all():
    # 初始化菜单界面
    pass

'''
def one_food(i):
    layout = [
        sg.Image(f'./img/food{i+1}.png', size=(200,200)), 
        sg.Text(dish_name[i], font='Any 20'),
        #sg.Button(image_filename='./img/other/plus.png')
    ],
    return layout
'''

def one_food_modified(i):
    a = sg.Image(f'./img/food{i+1}.png', size=(200,200))
    b = sg.Text(dish_name[i], font='Any 20')
    return a, b


# menu页面
menu_layout= []
menu_layout += [sg.Text('面馆', font='Any 30')],
for i in range(1, 4):
    c = []
    #menu_layout += one_food(i)
    for j in range(3 * i - 2, 3 * i + 1):
        a, b = one_food_modified(j)
        c.append(a)
        c.append(b)
    menu_layout += c,
menu_layout += [sg.Button('确认选择', font='Any 15'), sg.Button('清除所有', font='Any 15')],

# 订单确认页面
confirm_layout= []

# 2个页面整合
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
