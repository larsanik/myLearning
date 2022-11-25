scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

lenght = len(scores)

high_score = 0

for i in range(lenght):
    print('Пузырьковый раствор #' + str(i), '- результат:', scores[i])
    if scores[i] > high_score:
        high_score = scores[i]

print('Пузырьковых тестов:', lenght)
print('Наибольший результат:', high_score)

best_solutions = []
for i in range(lenght):
    if scores[i] == high_score:
        best_solutions.append(str(i))

print('Растворы с наибольшим результатом:', best_solutions)

cost = 100.0
most_effective = 0

for i in range(len(best_solutions)):
    index = int(best_solutions[i])
    if costs[index] < cost:
        most_effective = index
        cost = costs[index]
print('Раствор', most_effective, 'самый выгодный. Его цена -', costs[most_effective])
print('END')
