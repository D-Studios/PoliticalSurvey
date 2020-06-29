
'''
8values
Economic   Diplomatic   Civil       Societal
equality   nation       liberty     tradition   + positive
market     world        authority   progress    - negative
'''

# Initalization starts everything at neutrality
def initialization():
    global economic, diplomatic, civil, societal, neutral, mininum, maximum
    # In a range of 0-100, 50 is neutral.
    economic = 50
    diplomatic = 50
    civil = 50
    societal = 50
    # Mininum is strongly disagree, while maximum is strongly agree.
    mininum = 1
    maximum = 7
    neutral = (mininum + maximum) / 2

#This function debugs the values for some variables.
def debug():
    global economic, diplomatic, civil, societal
    print("Economic: "+str(economic))
    print("Diplomatic: "+str(diplomatic))
    print("Civil: "+str(civil))
    print("Societal: "+str(societal))

# This function asks questions and gives points to appropiate categories
def question_asker(question, issue, answer, weight=1):
    global economic, diplomatic, civil, societal, neutral, mininum, maximum
    # The points are calculated depending on how strong the position is.
    if answer<neutral:
        points=-pow(2, abs(answer-neutral)-1)*weight
    elif answer==neutral:
        points=0
    else:
        points=pow(2, abs(answer-neutral)-1)*weight
    '''Issues:
       1. Economic
       2. Diplomatic
       3. Civil
       4. Societal'''
    if issue is "equality":
        economic += points
    if issue is "market":
        economic-=points
    if issue is "nation":
        diplomatic+=points
    if issue is "world":
        diplomatic-=points
    if issue is "liberty":
        civil+=points
    if issue is "authority":
        civil-=points
    if issue is "tradition":
        societal+=points
    if issue is "progress":
        societal-=points
    #The values for economic, diplomatic, civil, and societal are clamped.
    economic=clamp(economic)
    diplomatic=clamp(diplomatic)
    civil=clamp(civil)
    societal=clamp(societal)
    #This function will be used to find the values of economic, diplomatic, civil, and societal.
    debug()

#This function clamps values to be within a range.
def clamp(val, min=0, max=100):
    if val<min:
        return min
    elif val>max:
        return max
    else:
        return val
# This is the main function.
def main():
    # Intialize the program.
    initialization()
    '''
    economic   diplomatic  civil       societal
    equality   nation      liberty     tradition
    market     world       authority   progress    
    '''
    question_asker("Nigg","market",1)
# The main function is called to execute the program.
main()