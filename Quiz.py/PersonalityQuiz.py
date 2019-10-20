from Questions import Question

questionPrompts = [
    "__ Likes Authority   __ Enthusiastic        __ Sensitive Feelings      __ Likes Instructions \n",
    "__ Takes Charge      __ Takes Risks         __ Loyal                   __ Accurate \n",
    "__ Determined        __ Visionary           __ Calm,Even Keel          __ Consistent \n",
    "__ Enterprising      __ Very Verbal         __ Enjoys Routine          __ Predictable \n",
    "__ Competitive       __ Promoter            __ Dislikes Change         __ Practical \n",
    "__ Problem Solver    __ Enjoys Popularity   __ Gives In To Others      __ Factual \n",
    "__ Productive        __ Fun-Loving          __ Avoids Confrontations   __ Conscientious \n",
    "__ Bold              __ Likes Variety       __ Sympathetic             __ Perfectionist \n",
    "__ Decision Maker    __ Spontaneous         __ Nurturing               __ Detail-Oriented \n",
    "__ Persistent        __ Inspirational       __ Peacemaker              __ Analytical \n"
]

questions = [
    Question(questionPrompts[0], []),
    Question(questionPrompts[1], []),
    Question(questionPrompts[2], []),
    Question(questionPrompts[3], []),
    Question(questionPrompts[4], []),
    Question(questionPrompts[5], []),
    Question(questionPrompts[6], []),
    Question(questionPrompts[7], []),
    Question(questionPrompts[8], []),
    Question(questionPrompts[9], []),
]

def take_test(questions):
    score = [0, 0, 0, 0]
    currentScore = [0, 0, 0, 0]
    for question in questions:
        answers = input(question.prompt)
        score1 = [int(i) for i in str(answers)]
        for i in range(0, len(score1)):
            currentScore = ((score[0] + score1[0]), (score[1] + score1[1]), (score[2] + score1[2]), (score[3] + score1[3]))
        score = currentScore
    print(get_house(currentScore))

def get_house(currentScore): 
    print("\nI've done this job for centuries\nOn every student's head I've sat\nOf thoughts I take inventories\nFor I'm the famous Sorting Hat\n\nI've sorted high, I've sorted low,\nI've done the job through thick and thin\nSo put me on and you will know\nwhich house you should be in...\n\nBetter be...\n")
    if currentScore[0] > currentScore[1] and currentScore[0] > currentScore[2] and currentScore[0] > currentScore[3]:
        print("\nSLYTHERIN!!!\n\n")
    elif currentScore[1] > currentScore[0] and currentScore[1] > currentScore[2] and currentScore[1] > currentScore[3]:
        print("\nGRYFFINDOR!!!\n\n")
    elif currentScore[2] > currentScore[0] and currentScore[2] > currentScore[1] and currentScore[2] > currentScore[3]:
        print("\nHUFFLEPUFF!!!\n\n")
    elif currentScore[3] > currentScore[0] and currentScore[3] > currentScore[1] and currentScore[3] > currentScore[2]:
        print("\nRAVENCLAW!!!\n\n")
    else:
        print("\nI can't figure you out...must be a dementor.")

print('\nWelcome to the five minute personality test!\n')
print('For each line, put the number 4 for the word that describes you the best, a 3 for the word that describes you the next best,\na 2 for the next, and a 1 for the word that describes you the least.')
print('\nFor each horizontal line of words, you will have one 4, one 3, one 2, and one 1.\n')
print('For example: \n')
print('__ Cute        __ Funny        __ Smart       __ Organized ')
print('3421\n')
print("Get it? Let's begin!\n\n")
take_test(questions)