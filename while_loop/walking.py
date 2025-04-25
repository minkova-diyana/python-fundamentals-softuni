steps = 0

goal_steps = 10000
while steps < goal_steps:
    walked_steps = input()
    if walked_steps == 'Going home':
        steps += int(input())
        break
    steps += int(walked_steps)

diff = abs(goal_steps - steps)
if steps >= goal_steps:
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    print(f'{diff} more steps to reach goal.')

