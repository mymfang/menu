import PySimpleGUI as sg
import math
import time

dish_name = ['披萨  ', '披萨  ', '披萨  ', '香蕉  ', '香蕉  ', '香蕉  ', '三明治', '三明治', '三明治', '三明治']
print(len(dish_name))

def confirm_order():
    sum_order = sum(1 for i in display.values() if i >= 1)
    if sum_order == 0:
        sg.popup('没有选择食物', font='Any 15', keep_on_top=True)

    elif sum_order >= 1:
        ordered_dict = {}
        ordered_food_list = []
        order_time = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        # 筛选出下单数大于1的食物
        ordered_dict = dict((k,v) for k, v in display.items() if v >= 1)
        # 向数据库写入订单数据
        # 添加订单数据到‘所有订单’页面
        for i in ordered_dict:
            ordered_food_list.append(str(dish_name[i]) + ' ' + str(ordered_dict[i]) + '份')
        sg.popup(ordered_food_list, title='下单成功', font='Any 15', keep_on_top=True, auto_close_duration=10, background_color='gray')
        
        reset_all()
    
    

def reset_all():
    # 初始化菜单界面
    for i in range(len(dish_name)):
        display[i] = 0
        window_menu['display' + str(i)].update(display[i])
    

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


# ************************
# 页面布局:
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


layout_login = [
    [sg.Text('用户名'),],  
    [sg.Input()],
    [sg.Text('密码')],
    [sg.Input()],
    [sg.Button('确认登陆', font='Any 15')]
]


# ********************************
# 菜单界面操作

window_login = sg.Window('登陆', layout_login)
window_menu_active = False

while True:
    event_login, values_login = window_login.read()
    if event_login is None:
        break
    
    if event_login == '确认登陆' and not window_menu_active and values_login[1] == 'gui':
        window_menu_active = True
        window_login.hide()
        layout_order = [[sg.TabGroup([[sg.Tab('菜单', menu_layout), sg.Tab('确认界面', confirm_layout)]])]]

        window_menu = sg.Window('菜单', layout_order)

        # 字典:食物和对应数量
        display = {}
        for i in range(len(dish_name)):
            display[i] = 0

# make window unclosed
        while True:
            event_menu, values_menu = window_menu.read()

            if event_menu == sg.WIN_CLOSED:
                break
            elif event_menu == '确认选择':
                confirm_order()
            elif event_menu == '清除所有':
                reset_all()

            elif '+' in event_menu:
                strip_plus = int(event_menu.strip('+'))
                if display[strip_plus] <= 1000:
                    display[strip_plus] += 1
                window_menu['display' + str(strip_plus)].update(display[strip_plus])
            
            elif '-' in event_menu:
                strip_minus = int(event_menu.strip('-'))
                if display[strip_minus] > 0:
                    display[strip_minus] -= 1
                else:
                    display[strip_minus] = 0
        window_menu['display' + str(strip_minus)].update(display[strip_minus])

    
        window_menu.close()

# 当前下单数据展示,包含下单时间
# 每日日终销量统计
# 添加菜品, 删除菜品
# 用户登陆
# 月度销量年度销量展示
