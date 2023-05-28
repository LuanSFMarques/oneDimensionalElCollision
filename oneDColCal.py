import time
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Function using physics to calculate the final speed after the collision
def collision_final_speed(mass_a, mass_b, initial_speed_a, initial_speed_b):
    final_speed_a = ((mass_a - mass_b) * initial_speed_a + 2 * mass_b * initial_speed_b) / (mass_a + mass_b)
    final_speed_a = round(final_speed_a)
    final_speed_b = (2 * mass_a * initial_speed_a + (mass_b - mass_a) * initial_speed_b) / (mass_a + mass_b)
    final_speed_b = round(final_speed_b)
    return final_speed_a, final_speed_b

# Animation
def print_ab_animation(va, ma, vb, mb, vel_a_final, vel_b_final):
    os.system('cls')
    num_lines = 10
    line_length = 100
    a_position = 0
    b_position = line_length
    reverse = False
    timez = 0
    
    stopa = False
    stopb = False
    while True:
        line = " " * line_length
        if a_position < b_position:
            line = line[:a_position] + "a" + line[a_position + 1:]
            line = line[:b_position] + "b" + line[b_position + 1:]
        elif a_position >= b_position:
            line = line[:b_position] + "ab" + line[b_position + 1:]
            reverse = True
        
        clear_screen()
        if a_position <= b_position:
            printz = True

            speedin = f"| Initial Vel A: {va}. Initial Vel B: -{vb}."
            speedfi = f"| Final Vel A:   {vel_a_final}. Final Vel B:   {vel_b_final}."
            mass = f"| Mass A: {ma}   Mass B: {mb}."
            speedin_space = " "*((line_length-len(speedin))-1) + "|"
            speedfi_space = " "*((line_length-len(speedfi))-1) + "|"
            mass_space = " "*((line_length-len(mass))-1) + "|"
            space = "|" + " "*(line_length-2) + "|"
            line_with_plus = "+" + "-" * (line_length-2) + "+"

            print("+" + "-"*(line_length-2) + "+" + f"\n{speedin}{speedin_space}\n{space}\n{speedfi}{speedfi_space}\n{space}\n{mass}{mass_space}")
            print(line_with_plus)
            print(line)
            print(line_with_plus)

        if not reverse:
            time.sleep(0.6)
            if a_position >= b_position:
                reverse = True  
                if timez == 0:
                    a_position = b_position-2
                    timez += 1
            else:
                if a_position >= 0 and a_position <= line_length:
                    if stopa == False:
                        a_position += va  
                if b_position <= line_length and b_position >= 0:
                    if stopb == False:
                        b_position -= vb
        else:
            time.sleep(0.6)
            a_position += vel_a_final
            if a_position <= 0:
                a_position = 0
                stopa = True
            if b_position >= line_length:
                b_position = (line_length-1)
                stopb = True
            elif stopb == False:
                b_position += vel_b_final
                if b_position >= line_length:
                    b_position = line_length-1
                b_stop = True
            if a_position <= 0 and b_position >= (line_length-1):
                finalprint = "a" + " " * (line_length - 2) + "b"
                break
            elif a_position >= line_length and b_position >= (line_length-1):
                finalprint = " " * (line_length - 2) + "ab"
                break
            elif a_position <= 0 and b_position <= 0:
                finalprint = "ab" + " " * (line_length - 2)
                break
            elif vel_a_final == 0 and b_position >= (line_length-1):
                finalprint = " "*(a_position) + "a" + " "*(line_length-(a_position+2)) + "b"
                break
            elif vel_b_final == 0 and a_position <= 0:
                finalprint = "a" + " "*(b_position-1) + "b" 
                break 
        print("\033[F" * (num_lines + 1)) 
    clear_screen()
    line = finalprint
    print("+" + "-"*(line_length-2) + "+" + f"\n{speedin}{speedin_space}\n{space}\n{speedfi}{speedfi_space}\n{space}\n{mass}{mass_space}")
    print(line_with_plus)
    print(line)
    print(line_with_plus)
va = 0
ma = 0
vb = 0
mb = 0

while va <= 0 or va >= 16:
    clear_screen()
    print("+--------------------------------------------------------------------------------------------------+")
    print("|                               1-D Elastic Collision Calculator                                   |")
    print("|                                                                                                  |")
    print("|   A Velocity: {:<8} | A Mass: {:<8} | B Speed: {:<8} | B Mass: {:<8}                 |".format(va, ma, vb, mb))
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("+--------------------------------------------------------------------------------------------------+")
    va = int(input("A Speed (max: 15): "))

while ma <= 0 or ma >= 51:
    clear_screen()
    print("+--------------------------------------------------------------------------------------------------+")
    print("|                               1-D Elastic Collision Calculator                                   |")
    print("|                                                                                                  |")
    print("|   A Velocity: {:<8} | A Mass: {:<8} | B Speed: {:<8} | B Mass: {:<8}                 |".format(va, ma, vb, mb))
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("+--------------------------------------------------------------------------------------------------+")
    ma = int(input("A Mass (max: 50): "))
    
while vb <= 0 or vb >= 16:
    clear_screen()
    print("+--------------------------------------------------------------------------------------------------+")
    print("|                               1-D Elastic Collision Calculator                                   |")
    print("|                                                                                                  |")
    print("|   A Velocity: {:<8} | A Mass: {:<8} | B Speed: {:<8} | B Mass: {:<8}                 |".format(va, ma, vb, mb))
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("+--------------------------------------------------------------------------------------------------+")
    vb = int(input("B Speed (max: 15): "))

while mb <= 0 or mb >= 51:
    clear_screen()
    print("+--------------------------------------------------------------------------------------------------+")
    print("|                               1-D Elastic Collision Calculator                                   |")
    print("|                                                                                                  |")
    print("|   A Velocity: {:<8} | A Mass: {:<8} | B Speed: {:<8} | B Mass: {:<8}                 |".format(va, ma, vb, mb))
    print("|                                                                                                  |")
    print("|                                                                                                  |")
    print("+--------------------------------------------------------------------------------------------------+")
    mb = int(input("B Mass (max: 50): "))

clear_screen()
finish = None

while finish != "exit":
    clear_screen()
    vel_a_final, vel_b_final = collision_final_speed(ma, mb, va, -abs(vb))
    print_ab_animation(va, ma, vb, mb, vel_a_final, vel_b_final)
    time.sleep(0.6)
    c = input("Submit any key to continue...")
    clear_screen()
    print("Submit \"any key\" for replay")
    print("Submit \"exit\" to exit")
    finish = input()
clear_screen()