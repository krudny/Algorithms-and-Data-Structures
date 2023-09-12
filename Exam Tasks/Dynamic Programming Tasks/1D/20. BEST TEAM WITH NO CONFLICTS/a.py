# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. 
# The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player.
# A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, 
# return the highest overall score of all possible basketball teams.

scores = [4,5,6,5]
ages = [2,1,2,1]

def team(scores, ages): 
    n = len(scores)
    A = []

    for i in range(n): 
        A.append((scores[i], ages[i]))

    A.sort()

    DP = [A[i][0] for i in range(n)] 

    for i in range(1, n): 
        for j in range(i): 
            if A[i][1] >= A[j][1]: 
                DP[i] = max(DP[i], A[i][0] + DP[j])
                
    return max(DP)


print(team(scores, ages))