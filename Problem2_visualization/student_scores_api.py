#importing required libraries
import matplotlib.pyplot as plt
import requests
import numpy as np
import seaborn as sns

#fetching data from api
response=requests.get('https://dummyjson.com/users')

students=response.json().get('users',[])
names=[]
scores=[]

for student in students:
    name=student.get('firstName')
    score=student.get('age') # treating age as test score (assumption)
    
    if name is not None and score is not None:
        names.append(name)
        scores.append(score) 

# convert scores to numpy array
scores=np.array(scores)

# calculate average score
avg_score=np.mean(scores)

print(f'average test score is {avg_score}')



# create bar chart
plt.figure(figsize=(10,5))
# average line
plt.axhline(
    y=avg_score,
    linestyle='--',
    label=f"Average Score ({avg_score:.2f})",
    
)

plt.bar(names,scores)
plt.xlabel('Student names')
plt.ylabel('Test scores')
plt.title("Student Test Scores")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('scores_with_average.png')
plt.show()
