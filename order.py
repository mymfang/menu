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
    str_i = str(i)
    key_for_num_text = 'display' + str_i
    key_for_minus = '-' + str_i
    key_for_plus = '+' + str_i

    food_image = sg.Image(f'./img/food{i+1}.png', size=(200,200))
    food_text = sg.Text(dish_name[i], font='Any 20')
    food_minus_button = sg.Button(button_text='-', font='Any 20', size=(2,1), key=key_for_minus)
    food_num_text = sg.In(font='Any 20', disabled=True, size=(3,3), key=key_for_num_text)
    food_plus_button = sg.Button(button_text='+', font='Any 20', size=(2,1), key=key_for_plus)

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

# 字典:食物和对应数量
display = {}
for i in range(len(dish_name)):
    display[i] = 0

# make window unclosed
while True:
    event, values = window.read()



    if event == sg.WIN_CLOSED:
        break
    elif event == '确认选择':
        confirm_order()
    elif event == '清除所有':
        reset_all()

    elif '+' in event:
        strip_plus = int(event.strip('+'))
        if display[strip_plus] <= 1000:
            display[strip_plus] += 1
        window['display' + str(strip_plus)].update(display[strip_plus])
    
    elif '-' in event:
        strip_minus = int(event.strip('-'))
        if display[strip_minus] > 0:
            display[strip_minus] -= 1
        else:
            display[strip_minus] = 0
        window['display' + str(strip_minus)].update(display[strip_minus])
    '''
    elif event == '-1':
        if display > 0:
            display -= 1
        else:
            display = 0
        window['display1'].update(display)
'''

    
window.close()

# 当前下单数据展示,包含下单时间
# 每日日终销量统计
# 添加新菜
# 用户登陆
# 月度销量年度销量展示
