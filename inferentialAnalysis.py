import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Extract the data. Return both the raw data and dataframe
def generateDataset(filename):
    data = pd.read_csv(filename)
    df = data[0:]
    df = df.dropna()
    return data, df


# Run a t-test 
def runTTest(ivA, ivB, dv): 
    ttest = scipy.stats.ttest_ind(ivA[dv], ivB[dv])
    print(ttest)

#Run NOVA 
def runAnova(data, formula):
    model = ols(formula, data).fit()
    aov_table = sm.stats.anova_lm(model, typ=2)
    print (aov_table)
    

# Run the analysis 
rawData, df = generateDataset('simpsons_paradox.csv')

print ("Does gender correlate with admissions?")
men =df[(df['Gender']=='Male')]
women = df[(df['Gender']=='Female')]
runTTest(men, women, 'Admitted')

print("Does department correlate with admissions?")
simpleFormula = 'Admitted ~ C(Department)'
runAnova(rawData, simpleFormula)

print("Do gender and department correlate with admissions?")
moreComplex = 'Admitted ~C(Department) + C(Gender)'
runAnova(rawData, moreComplex)














########################
#MONDAY WORK 
########################

#Question 1 
#A) Does a student's current year (e.g., freshman, sophomore, etc.) effect their GPA?
    #independent variable - current year 
    
    #dependent variable - GPA 
    
    #Stat test - T test because the current year it categorical and the other is continuous 
    
    
#B) Has the amount of snowfall in the mountains changed over time? 
    # independent - snow fall  
    
    #dependent -  time 
    
    #stat test - generialize regression when you have have 
    
#C) Over the last 10 years, have there been more hikers on average in Estes Park in the spring or summer? 
    # independent- season cat.
    
    #dependent - number of hikers  cont. 
    
    #stat test - T test 
    
#D) Does a student's home state predict their highest degree level?
    #indep -home state cat. 
    
    #dep - grade level cat. 
    
    # stat test - chi squared 
    
#Question 2 
    

