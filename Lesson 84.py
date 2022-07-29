#Упражнение 84. Подбрасываем монетку.
import random

sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l1 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l2 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l3 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l4 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l5 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l6 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l7 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l8 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l9 = len(sim_0)
sim_0 = []
while sim_0[len(sim_0)-3:len(sim_0)] not in [['O', 'O', 'O'], ['P', 'P', 'P']]:
    sim_0.append(random.choice(['O', 'P']))
print(" ".join(map(str, sim_0)), ' (попыток: ', len(sim_0), ')', sep="")
l10 = len(sim_0)
print('Среднее количество попыток: ', (l1+l2+l3+l4+l5+l6+l7+l8+l9+l10)/10, '.')