import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import random

raw = pd.read_excel('training_test_0514.xlsx').iloc[:,1:]

data = []
w = 1
c1 = 1
c2 = 1
xid_save_pl1 = []
xid_save_pl4 = []

gbest_score = 0
New_Vid_pl1 = 0
New_Vid_pl4 = 0
New_Xid_pl1 = 0
New_Xid_pl4 = 0

### Init data
for i in range(10):
    data.append(raw.sample(5))  # 1 cycle = 5 data
# print(data)


### Calculate Vid & Xid
##      new_vid = w * vid + c1 * rnd() * (pbest_xid - xid)  + c2 * rnd() * (gbest_xd-xid)
##      new_xid = xid + new_vid

for i in range(10):
    # pbest
    pbest_pl1 = data[i].iloc[:, 0].reset_index()  
    pbest_pl4 = data[i].iloc[:, 3].reset_index()
    
    # gbest
    gbest_score_cycle = data[i]['3dmarkscore'].max()  # max score in cycle
    gbest_score = np.where(gbest_score_cycle > gbest_score, gbest_score_cycle, gbest_score)  # update gbest score
    
    if gbest_score == gbest_score_cycle:  # row of gbest 
        gbest = data[i].loc[data[i]['3dmarkscore'] == gbest_score]
        
    gbest_pl1 = gbest.iloc[:,0].reset_index().iloc[0,1]
    gbest_pl4 = gbest.iloc[:,3].reset_index().iloc[0,1]

#     print(pbest_pl1)
#     print('gbest_score_cycle:', gbest_score_cycle)
#     print('gbest_score:', gbest_score)
#     print('gbest',gbest)
#     print(gbest_pl1)
#     print(gbest_pl4)
    
    for j in range(5):
        R1 = random.uniform(0,1)
        R2 = random.uniform(0,1)
    
        Xid_pl1 = New_Xid_pl1
        Xid_pl4 = New_Xid_pl4
        Vid_pl1 = New_Vid_pl1
        Vid_pl4 = New_Vid_pl4
        #print(Xid_pl1)
        
        New_Vid_pl1 = w*Vid_pl1 + c1*R1*(pbest_pl1.iloc[j,1] - Xid_pl1) + c2*R2*(gbest_pl1 - Xid_pl1)
        New_Vid_pl4 = w*Vid_pl4 + c1*R1*(pbest_pl4.iloc[j,1] - Xid_pl4) + c2*R2*(gbest_pl4 - Xid_pl4)
        New_Xid_pl1 = Xid_pl1 + New_Vid_pl1
        New_Xid_pl4 = Xid_pl4 + New_Vid_pl4
        #print(pbest_pl1.iloc[j,1])
        
        xid_save_pl1.append(New_Xid_pl1)
        xid_save_pl4.append(New_Xid_pl4)
        
        # Process of cycle
#         print('Vid_pl1:', round(Vid_pl1, 2), ' Vid_pl4:', round(Vid_pl4, 2))
#         print('Xid_pl1:', round(Xid_pl1, 2), ' Xid_pl4:',round(Xid_pl4, 2))
#         print('New_Vid_pl1:', round(New_Vid_pl1, 2), ' New_Vid_pl4:', round(New_Vid_pl4, 2))    
#         print('New_Xid_pl1:', round(New_Xid_pl1, 2), ' New_Xid_pl4:', round(New_Xid_pl4, 2))
#         print('')
    

xid_save_pl1 = list(np.around(np.array(xid_save_pl1),2))
xid_save_pl4 = list(np.around(np.array(xid_save_pl4),2))
# print('PL_1:', xid_save_pl1)
# print('PL_4:', xid_save_pl4)

result = DataFrame({'PL_1': xid_save_pl1, 
                    'PL_4': xid_save_pl4})
result
