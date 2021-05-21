def get_target_noparens(nums, target):
    operations = ["+", "-", "*", "/"]
    value_1 = 0
    value_2 = 0

    if len(nums) == 1:
        if nums[0] == target:
            return target
    elif sum(nums) == target:
        return str(str(nums[0]) + "+" + str(nums[1]) + "+" + str(nums[2]))
    else:
        for c1 in nums:
            for c2 in nums:
                for c3 in nums:
                    if c1 != c2 and c2 != c3 and c3 != c1:
                        for operation1 in operations:
                            if operation1 == "+":
                                value_1 = c1 + c2
                                for operation2 in operations:
                                    if operation2 == "+":
                                        value_2 = value_1 + c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "-":
                                        value_2 == value_1 - c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "*":  
                                        value_2 = value_1 * c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "/":
                                        value_2 = value_1/c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                            elif operation1 == "-":
                                value_1 == c1 - c2
                                for operation2 in operations:
                                    if operation2 == "+":
                                        value_2 = value_1 + c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "-":
                                        value_2 == value_1 - c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "*":
                                        value_2 = value_1 * c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "/":
                                        value_2 = value_1/c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                            elif operation1 == "*":
                                value_1 = c1 * c2
                                for operation2 in operations:
                                    if operation2 == "+":
                                        value_2 = value_1 + c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "-":
                                        value_2 == value_1 - c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "*":
                                        value_2 = value_1 * c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "/":
                                        value_2 = value_1/c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                            elif operation1 == "/":
                                value_1 = c1/c2
                                for operation2 in operations:
                                    if operation2 == "+":
                                        value_2 = value_1 + c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "-":
                                        value_2 == value_1 - c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "*":
                                        value_2 = value_1 * c3 
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))
                                    elif operation2 == "/":
                                        value_2 = value_1/c3
                                        if value_2 == target:
                                            return str(str(c1) + str(operation1) + str(c2) + str(operation2) + str(c3))