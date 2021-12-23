# tuple = ('a', 2)
# print (tuple)
# print (type(tuple))


# if 1>0 and 0>-1:
#     print ("a")


# val = {'0':0, '1':1}
# print(type(val))


# values=[0,3,1,2,4]
# print (max(values))
# print (sorted(values))
# print(values[::1])

# print('\n')
# print(values[-1])
# print(values[len(values)-1])


# values2=[1,423]

# print('\n')
# print (values+values2)


# values2=["1", "2"]
# print('\n')
# print(list(map(int, values2)))
# print([int(x) for x in values2])


# import sys
# import math
# from contextlib import redirect_stdout


# def compute_game_state(name_p1, name_p2, wins):
#     # Write your code here
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#     points = [[0, 0], [0, 0]]
#     for player in wins:
#         if player == name_p1:
#             if points[0][1] >= 2:
#                 points[0][0] += 10
#                 points[0][1] += 1
#             else:
#                 points[0][0] += 15
#                 points[0][1] += 1
#         else:
#             if points[1][1] >= 2:
#                 points[1][0] += 10
#                 points[1][1] += 1
#             else:
#                 points[1][0] += 15
#                 points[1][1] += 1
#     if points[0][1] == points[1][1]:
#         return "DEUCE"
#     elif points[0][1] >= 3 and points[1][1] >= 3 and abs(points[1][1] - points[0][1]) == 1:
#         if points[1][1] > points[0][1]: 
#             return f"{name_p1} ADVANTAGE" 
#         else:
#             return f"{name_p2} ADVANTAGE" 
#     elif abs(points[1][1] - points[0][1]) == 4 or abs(points[1][1] - points[0][1]) == 2:
#          if points[1][1] > points[0][1]: 
#             return f"WIN {name_p1}" 
#          else:
#             return f"WIN {name_p2}" 
#     else:
#         return (f"{name_p1} {points[0][0]} - {name_p2} {points[1][0]}")


# # Ignore and do not change the code below
# def main():
#     # pylint: disable = C, W
#     name_p1 = input()
#     name_p2 = input()
#     played_count = int(input())
#     wins = []
#     for i in range(played_count):
#         wins.append(input())
#     with redirect_stdout(sys.stderr):
#         game_state = compute_game_state(name_p1, name_p2, wins)
#     print(game_state)


# if __name__ == "__main__":
#     main()



from os import replace
from Scripts.moreFunctions import strings


def solution(string):
    # Your code goes here
    string = string.replace(" ", '\n')

print(solution('Hello you !'))