
# loop through scores to find mins and increment rewards for students on increasing performance
# loop back through scores in reverse to increase reards for students of increasing performance and decide on lolcal max rewards

def minRewards(scores):
    rewards = []
    for idx, score in enumerate(scores):
        rewards.append(1)
        if idx == 0 :
            continue
        
        if score > scores[idx-1]:
            rewards[idx] = rewards[idx-1] + 1
    
    for idx, score in enumerate(reversed(scores)):
        real_idx = (len(scores)-1) - idx

        if idx == 0:
            continue
        
        if score > scores[real_idx + 1]:
            rewards[real_idx] = max(rewards[real_idx+1] + 1, rewards[real_idx]
        
        if score == scores[real_idx + 1]:
            rewards[real_idx], rewards[real_idx+1] = max(rewards[real_idx], rewards[real_idx+1])
        

    