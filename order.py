import PySimpleGUI as sg
import math

dish_name = ['披萨  ', '披萨  ', '披萨  ', '香蕉  ', '香蕉  ', '香蕉  ', '三明治', '三明治', '三明治', '三明治']
print(len(dish_name))

def confirm_order():
    sg.popup('下单成功', font='Any 15')
    # 向数据库写入订单数据
    reset_all()
    
    # 切换到‘确认界面’

def reset_all():
    # 初始化菜单界面
    pass

# 菜单中的食物
def one_food_modified(i):
    minus_key = '-i'
    show_key = '-DISPLAY-'
    food_image = sg.Image(f'./img/food{i+1}.png', size=(200,200))
    food_text = sg.Text(dish_name[i], font='Any 20')
    food_minus_button = sg.Button('-', font='Any 20', size=(2,1))
    food_num_text = sg.In(font='Any 20', size=(3,3), key=show_key)
    food_plus_button = sg.Button('+', font='Any 20', size=(2,1))

    return food_image, food_text, food_minus_button, food_num_text, food_plus_button


# menu页面
menu_layout= []
menu_layout += [sg.Text('面馆', font='Any 30')],

if len(dish_name) % 3 == 0:
    range_i = int(len(dish_name) / 3)
else:
    range_i = int(math.ceil(len(dish_name) / 3))

print('range_i = ', range_i)

for i in range(range_i):
    temp = []
    for j in range(3 * i, 3 * i + 3):
        if j <= len(dish_name) - 1:
            food_image, food_text, food_minus_button, food_num_text, food_plus_button = one_food_modified(j)
            temp.append(food_image)
            temp.append(food_text)
            temp.append(food_minus_button)
            temp.append(food_num_text)
            temp.append(food_plus_button)
    menu_layout += temp,

menu_layout += [sg.Button('确认选择', font='Any 15'), sg.Button('清除所有', font='Any 15')],

# 订单确认页面
confirm_layout= []

# 2个页面整合
layout = [[sg.TabGroup([[sg.Tab('菜单', menu_layout), sg.Tab('确认界面', confirm_layout)]])]]

window = sg.Window('菜单', layout)

display = 0
# make window unclosed
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '确认选择':
        confirm_order()
    elif event == '清除所有':
        reset_all()
    elif event == '+':
        display += 1
    
    elif event == '-':
        if display > 0:
            display -= 1
        else:
            display = 0
        window['-DISPLAY-'].update(display)


    
window.close()

# 当前下单数据展示,包含下单时间
# 每日日终销量统计
# 添加新菜
# 用户登陆
# 月度销量年度销量展示
