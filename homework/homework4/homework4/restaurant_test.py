###################
#Test file of restaurant module
###################
import restaurant as rs

ret = rs.Restaurant_list(2)
test_dict = [
        ['Mary', 3],
        ['John', 2],
        ['Alice', 1],
        ]
test_dict2 = [
        ['Mary', 2],
        ['John', 5],
        ['Alice', 3]
        ]
test_list = [rs.Guest(*x) for x in test_dict]
while test_list or flags_serve:
    print("test_list => {} \nret => {}".format(test_list, ret))
    flags_seat = ret.seat(test_list[0]) if test_list else False
    if flags_seat:
        test_list = test_list[1:]
    flags_serve = ret.serve()

print("==" * 20)
test_list = [rs.Guest(*x) for x in test_dict2]
while test_list or flag_serve:
    flag_seat = ret.seat(test_list[0]) if test_list else False
    if flag_seat:
        test_list = test_list[1:]
    flag_serve = ret.serve()
