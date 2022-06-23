import tkinter
import math
from tkinter import *

# kinematics equations (constant acceleration)
# d = vi*t + 1/2 * a * t^2
# vf = vi + a*t
# vf^2 = vi^2 + 2 * a * d
# d = (vi + vf)/2 * t


root = Tk()
root.title('Kinematics Engine')
results_string = StringVar()
results_string.set('RESULTS')

for i in range(9):
    if i < 6:
        Grid.columnconfigure(root, i, weight=1)
    Grid.rowconfigure(root, i, weight=1)


# functional code
def clear_values():
    d.delete(0, END)
    t.delete(0, END)
    vi.delete(0, END)
    vf.delete(0, END)
    a.delete(0, END)


def get_known_values():
    known = {}
    if d.get() != '':
        d1 = float(d.get())
        known.update({'d': d1})
    if t.get() != '':
        t1 = float(t.get())
        known.update({'t': t1})
    if vi.get() != '':
        vi1 = float(vi.get())
        known.update({'vi': vi1})
    if vf.get() != '':
        vf1 = float(vf.get())
        known.update({'vf': vf1})
    if a.get() != '':
        a1 = float(a.get())
        known.update({'a': a1})
    return known


def calc_d():
    global results_string
    known = get_known_values()
    if 'd' in known:
        d2 = known['d']
        work = 'd = d...'
        formula = 5
    elif len(known) < 3:
        formula = 0
        work = 'Need at least 3 known values to solve! Problem Not Solved!'
        d2 = 0.0
    elif 'vi' in known:
        if 'a' in known:
            if 't' in known:
                formula = 1
            elif 'vf' in known:
                formula = 2
        elif 'vf' in known and 't' in known:
            formula = 3
    elif 'vf' in known and 'a' in known and 't':
        formula = 4
    else:
        print('What is happening!?')

    if formula == 1:
        a2 = known['a']
        vi2 = known['vi']
        t2 = known['t']
        d2 = vi2 * t2 + (0.5 * a2 * t2**2)
        work = 'd = vi*t + 1/2*a*t^2'

    elif formula == 2:
        a2 = known['a']
        vi2 = known['vi']
        vf2 = known['d']
        d2 = (vf2**2 - vi2**2)/ (2*a2)
        work = 'd = (vf^2-vi^2)/2a'

    elif formula == 3:
        vf2 = known['vf']
        vi2 = known['vi']
        t2 = known['t']
        d2 = (vi2 + vf2) * t2/2
        work = 'd = (vi + vf)/2 * t'

    elif formula == 4:
        vf2 = known['vf']
        a2 = known['a']
        t2 = known['t']
        vi2 = vf2 - a2*t2
        d2 = (vi2 + vf2)*t2/2
        work = f'vi = vf - a*t\nvi = {vi2} m/s\nd = (vi + vf)/2 * t '
    results_string.set(f'{work}\n Displacement: {round(d2, 2)} meters')


def calc_t():
    global results_string
    known = get_known_values()
    if 't' in known:
        t2 = known['t']
        work = 't = t...'
        formula = 5
    elif len(known) < 3:
        formula = 0
        work = 'Need at least 3 known values to solve! Problem Not Solved!'
        t2 = 0.0
    elif 'vi' in known:
        if 'a' in known:
            if 'd' in known:
                formula = 1
            elif 'vf' in known:
                formula = 2
        elif 'vf' in known and 'd' in known:
            formula = 3
    elif 'vf' in known and 'd' in known and 'a':
        formula = 4
    else:
        print('What is happening!?')

    if formula == 1:
        a2 = known['a']
        vi2 = known['vi']
        d2 = known['d']
        t_plus = (-vi2 + math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        t_minus = (-vi2 - math.sqrt(vi2 ** 2 - 2 * a2 * (-d2))) / a2
        if t_plus >= 0:
            t2 = t_plus
        else:
            t2 = t_minus
        work = '1/2*a*t^2 + vi*t - d = 0\nquadratic equation: x = (-b +/- sqrt(b^2 -4ac))/2a\n' \
               't = positive of (-vi +/- sqrt(vi^2 - 2ad))/a'

    elif formula == 2:
        a2 = known['a']
        vi2 = known['vi']
        vf2 = known['vf']
        t2 = (vf2 - vi2) / a2
        work = 't = (vf-vi)/a'

    elif formula == 3:
        d2 = known['d']
        vi2 = known['vi']
        vf2 = known['vf']
        t2 = (2 * d2) / (vi2 - vf2)
        work = 't = 2d/(vi-vf)'

    elif formula == 4:
        d2 = known['d']
        vf2 = known['vf']
        a2 = known['a']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        t2 = (2 * d2) / (vi2 - vf2)
        work = f'vi = sqrt(vf^2 - 2*a*d)\nvi = {vi2} m/s\nt = 2d/(vi-vf) '
    results_string.set(f'{work}\n Time: {round(t2, 2)} sec')


def calc_vi():
    global results_string
    known = get_known_values()
    if 'vi' in known:
        vi2 = known['vi']
        work = 'vi = vi...'
        formula = 5
    elif len(known) < 3:
        formula = 0
        work = 'Need at least 3 known values to solve! Problem Not Solved!'
        vi2 = 0.0
    elif 'a' in known:
        if 'd' in known:
            if 't' in known:
                formula = 1
            elif 'vf' in known:
                formula = 2
        elif 't' in known and 'vf' in known:
            formula = 3
    elif 'vf' in known and 'd' in known and 't':
        formula = 4
    else:
        print('What is happening!?')

    if formula == 1:
        t2 = known['t']
        d2 = known['d']
        a2 = known['a']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        work = 'vi = (d - (1/2*a*t^2))/t'

    elif formula == 2:
        a2 = known['a']
        vf2 = known['vf']
        d2 = known['d']
        vi2 = math.sqrt(vf2 ** 2 - 2 * a2 * d2)
        work = 'vi = sqrt(vf^2 - 2*a*d)'

    elif formula == 3:
        a2 = known['d']
        vf2 = known['vf']
        t2 = known['t']
        vi2 = vf2 - (a2 * t2)
        work = 'vi = vf - a*t'

    elif formula == 4:
        d2 = known['d']
        vf2 = known['a']
        t2 = known['t']
        vi2 = (d2 / t2) * 2 - vf2
        work = 'vi = 2*d/t - vf'

    results_string.set(f'{work}\n Initial Velocity: {round(vi2, 2)} m/s')


def calc_vf():
    global results_string
    known = get_known_values()
    if 'vf' in known:
        vf2 = known['vf']
        work = 'vf = vf...'
        formula = 5
    elif len(known) < 3:
        formula = 0
        work = 'Need at least 3 known values to solve! Problem Not Solved!'
        vf2 = 0.0
    elif 'vi' in known:
        if 'a' in known:
            if 't' in known:
                formula = 1
            elif 'd' in known:
                formula = 2
        elif 't' in known and 'd' in known:
            formula = 3
    elif 'a' in known and 'd' in known and 't':
        formula = 4
    else:
        print('What is happening!?')

    if formula == 1:
        t2 = known['t']
        vi2 = known['vi']
        a2 = known['a']
        vf2 = vi2 + (a2 * t2)
        work = 'vf = vi + (a*t)'

    elif formula == 2:
        a2 = known['a']
        vi2 = known['vi']
        d2 = known['d']
        vf2 = math.sqrt(vi2 ** 2 + 2 * a2 * d2)
        work = 'vf = sqrt(vi^2 + 2*a*d)'

    elif formula == 3:
        d2 = known['d']
        vi2 = known['vi']
        t2 = known['t']
        vf2 = ((d2 / t2) * 2) - vi2
        work = 'vf = 2d/t - vi'

    elif formula == 4:
        d2 = known['d']
        a2 = known['a']
        t2 = known['t']
        vi2 = (d2 - (0.5 * a2 * t2 ** 2)) / t2
        vf2 = vi2 + a2 * t2
        work = f'vi = (d - (1/2*a*t^2))/t\nvi = {vi2} m/s\nvf = vi + a*t '

    results_string.set(f'{work}\n Final Velocity: {round(vf2, 2)} m/s')


def calc_a():
    global results_string
    known = get_known_values()
    if 'a' in known:
        a2 = known['a']
        work = 'a = a...'
        formula = 5
    elif len(known) < 3:
        formula = 0
        work = 'Need at least 3 known values to solve! Problem Not Solved!'
        a2 = 0.0
    elif 'vi' in known:
        if 't' in known:
            if 'vf' in known:
                formula = 1
            elif 'd' in known:
                formula = 2
        elif 'vf' in known and 'd' in known:
            formula = 3
    elif 'vf' in known and 'd' in known and 't':
        formula = 4
    else:
        print('What is happening!?')

    if formula == 1:
        t2 = known['t']
        vi2 = known['vi']
        vf2 = known['vf']
        a2 = (vf2 - vi2) / t2
        work = 'a = (vf - vi) / t'

    elif formula == 2:
        t2 = known['t']
        vi2 = known['vi']
        d2 = known['d']
        a2 = 2 * (d2 - (vi2 * t2)) / (t2 ** 2)
        work = 'a = 2*(d - (vi*t))/t^2'

    elif formula == 3:
        d2 = known['d']
        vi2 = known['vi']
        vf2 = known['vf']
        a2 = (vf2 ** 2 - vi2 ** 2) / 2 * d2
        work = 'a = (vf - vi) / t'

    elif formula == 4:
        d2 = known['d']
        vf2 = known['vf']
        t2 = known['t']
        vi2 = ((d2 / t2) * 2) - vf2
        a2 = (vf2 - vi2) / t2
        work = f'vi = 2d/t - vf\nvi = {vi2} m/s\na = (vf-vi)/t '

    results_string.set(f'{work}\n Acceleration: {round(a2, 2)} m/s^2')


# tkinter visual elements
label1 = Label(root, text='Enter The Known Variables', font='bold')
label1.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
d_label = Label(root, text='d-Displacement (meters)')
d_label.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
d = Entry(root, borderwidth=5)
d.grid(row=1, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
t_label = Label(root, text='t-Time (seconds)')
t_label.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
t = Entry(root, borderwidth=5)
t.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
vi_label = Label(root, text='vi-Initial Velocity (m/s)')
vi_label.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
vi = Entry(root, borderwidth=5)
vi.grid(row=3, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
vf_label = Label(root, text='vf-Final Velocity (m/s)')
vf_label.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
vf = Entry(root, borderwidth=5)
vf.grid(row=4, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
a_label = Label(root, text='a-Acceleration (m/s^2)')
a_label.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
a = Entry(root, borderwidth=5)
a.grid(row=5, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
label2 = Label(root, text='Select What To Solve For', font='bold')
label2.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
clear_button = Button(root, text='Clear Values', command=clear_values, font='bold')
clear_button.grid(row=7, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
d_button = Button(root, text='d', command=calc_d, font='bold')
d_button.grid(row=7, column=1, columnspan=1, padx=10, pady=10, sticky='NESW')
t_button = Button(root, text='t', command=calc_t, font='bold')
t_button.grid(row=7, column=2, columnspan=1, padx=10, pady=10, sticky='NESW')
vi_button = Button(root, text='vi', command=calc_vi, font='bold')
vi_button.grid(row=7, column=3, columnspan=1, padx=10, pady=10, sticky='NESW')
vf_button = Button(root, text='vf', command=calc_vf, font='bold')
vf_button.grid(row=7, column=4, columnspan=1, padx=10, pady=10, sticky='NESW')
a_button = Button(root, text='a', command=calc_a, font='bold')
a_button.grid(row=7, column=5, columnspan=1, padx=10, pady=10, sticky='NESW')
results = Label(root, textvariable=results_string, font='bold')
results.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')

root.mainloop()
