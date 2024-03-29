from typing import List

# for Part I
# conditioner_unit = 1 

# for Part II
conditioner_unit = 5

# From the day2 challenge
def advanced_computer(intcode: str) -> int:

    intcode = [int(el) for el in intcode.split(',')]

    i = 0
    while i < len(intcode):
        opcode = intcode[i]
        # print(opcode)
        print(f"i = {i}, IntCode: {intcode}")

        if not opcode == 99:

            if opcode == 1:
                input1 = intcode[i+1]
                input2 = intcode[i+2]
                target = intcode[i+3]

                intcode[target] = intcode[input1] + \
                    intcode[input2]
                
                i += 4

            elif opcode == 2:
                input1 = intcode[i+1]
                input2 = intcode[i+2]
                target = intcode[i+3]

                intcode[target] = intcode[input1] * \
                    intcode[input2]

                i += 4

            elif opcode == 3:
                target = intcode[i+1]
                intcode[target] = conditioner_unit
                i += 2

            elif opcode == 4:
                target = intcode[i+1]
                output = intcode[target]
                print(f'Output (position): {output}')
                i += 2

            elif opcode > 100:
                new_opcode = int(str(opcode)[-1])

                if new_opcode == 1 or new_opcode == 2:
                    if len(str(opcode)) == 3:
                        full_opcode = '00' + str(opcode)
                    elif len(str(opcode)) == 4:
                        full_opcode = '0' + str(opcode)
                    else:
                        raise RuntimeError("wrong length of opcode: {opcode}")

                    mode3, mode2, mode1, _, new_opcode = full_opcode
                    new_opcode = int(new_opcode)
                    mode1 = int(mode1)
                    mode2 = int(mode2)
                    mode3 = int(mode3)

                    param1 = intcode[i+1]
                    param2 = intcode[i+2]
                    target = intcode[i+3]
                    value = intcode[i+4]

                    if new_opcode == 1:
                        operator = '+'
                    elif new_opcode == 2:
                        operator = '*'
                    else:            
                        raise RuntimeError("Wrong opcode!")
                
                    if mode1 == 0 and mode2 == 0:
                        param1 = intcode[param1]
                        param2 = intcode[param2]
                        intcode[target] = eval(f'{param1}{operator}{param2}')
                    elif mode1 == 0 and mode2 == 1:
                        param1 = intcode[param1]
                        intcode[target] = eval(f'{param1}{operator}{param2}')                        
                    elif mode1 == 1 and mode2 == 0:
                        param2 = intcode[param2]
                        intcode[target] = eval(f'{param1}{operator}{param2}')
                    else:
                        intcode[target] = eval(f'{param1}{operator}{param2}')
    
                    i += 4

                elif new_opcode == 4:
                    mode1 = int(str(opcode)[0])
                    target = intcode[i+1]

                    if mode1 == 1:
                        output = target
                        print(f'Output (immediate): {output}')
                    else:
                        raise RuntimeError(f"Mode Zero!! {mode1}")

                    i += 2
                
                # immediate modes
                elif new_opcode in [5, 6, 7, 8]:
                    if len(str(opcode)) == 3:
                        full_opcode = '00' + str(opcode)
                    elif len(str(opcode)) == 4:
                        full_opcode = '0' + str(opcode)
                    else:
                        raise RuntimeError("wrong length of opcode: {opcode}")

                    mode3, mode2, mode1, _, new_opcode = full_opcode
                    new_opcode = int(new_opcode)
                    mode1 = int(mode1)
                    mode2 = int(mode2)
                    mode3 = int(mode3)

                    param1 = intcode[i+1]
                    param2 = intcode[i+2]

                    if new_opcode == 5:
                        if mode1 == 0 and mode2 == 0:
                            if intcode[param1] != 0:
                                i = intcode[param2]
                            else:
                                i += 3
                            
                        elif mode1 == 0 and mode2 == 1:
                            if intcode[param1] != 0:
                                i = param2
                            else:
                                i += 3
                                                    
                        elif mode1 == 1 and mode2 == 0:
                            if param1 != 0:
                                i = intcode[param2]
                            else:
                                i += 3
                        else:
                            if param1 != 0:
                                i = param2
                            else:
                                i += 3   

                    elif new_opcode == 6:

                        if mode1 == 0 and mode2 == 0:
                            if intcode[param1] == 0:
                                i = intcode[param2]
                            else:
                                i += 3
                            
                        elif mode1 == 0 and mode2 == 1:
                            if intcode[param1] == 0:
                                i = param2
                            else:
                                i += 3
                                                    
                        elif mode1 == 1 and mode2 == 0:
                            if param1 == 0:
                                i = intcode[param2]
                            else:
                                i += 3
                        else:
                            if param1 == 0:
                                i = param2
                            else:
                                i += 3   

                    elif new_opcode == 7:

                        param3 = intcode[i+3]

                        if mode1 == 0 and mode2 == 0:
                            if intcode[param1] < intcode[param2]:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                            
                        elif mode1 == 0 and mode2 == 1:
                            if intcode[param1] < param2:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                                                    
                        elif mode1 == 1 and mode2 == 0:
                            if param1 < intcode[param2]:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                        else:
                            if param1 < param2:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                        
                        i += 4

                    elif new_opcode == 8:

                        param3 = intcode[i+3]

                        if mode1 == 0 and mode2 == 0:
                            if intcode[param1] == intcode[param2]:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                            
                        elif mode1 == 0 and mode2 == 1:
                            if intcode[param1] == param2:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                                                    
                        elif mode1 == 1 and mode2 == 0:
                            if param1 == intcode[param2]:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0
                        else:
                            if param1 == param2:
                                intcode[param3] = 1
                            else:
                                intcode[param3] = 0

                        i += 4

            # position modes
            elif opcode == 5:
                param1 = intcode[i+1]
                param2 = intcode[i+2]
                if intcode[param1] != 0:
                    i = intcode[param2]
                else:
                    i += 3

            elif opcode == 6:
                param1 = intcode[i+1]
                param2 = intcode[i+2]
                if intcode[param1] == 0:
                    i = intcode[param2]
                else:
                    i += 3

            elif opcode == 7:
                param1 = intcode[i+1]
                param2 = intcode[i+2]
                param3 = intcode[i+3]

                if intcode[param1] < intcode[param2]:
                    intcode[param3] = 1
                else:
                    intcode[param3] = 0

                i += 4

            elif opcode == 8:
                param1 = intcode[i+1]
                param2 = intcode[i+2]
                param3 = intcode[i+3]

                if intcode[param1] == intcode[param2]:
                    intcode[param3] = 1
                else:
                    intcode[param3] = 0

                i += 4

            else:
                raise RuntimeError(f"Wrong opcode: {opcode}")

        else:
            return output


# print(advanced_computer("3,0,4,0,99"))

with open('data/day5.txt') as f:
    intcodes = f.read()

TEST = """3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,\
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,\
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"""
# assert advanced_computer(TEST) == 1001

print(advanced_computer(intcodes))