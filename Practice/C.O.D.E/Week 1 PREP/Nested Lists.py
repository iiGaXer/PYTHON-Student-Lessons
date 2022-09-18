def low_score(x, y):
    data = []
    names = x.copy()
    scores = y.copy()
    
    # names.append(x)
    # scores.append(y)
    
    sorted_scores = sorted(scores)
    for i in range(len(sorted_scores)):
        if sorted_scores[i] > sorted_scores[0] and sorted_scores[i] < sorted_scores[-1]:
            lowest_2nd_score = i
            copy_scores = sorted_scores.copy()
            copy_scores.remove(copy_scores[lowest_2nd_score])
            for j in range(len(copy_scores)):
                if copy_scores[j] == sorted_scores[i]:
                    lowest_2nd_score_2 = names[j - 1]
                    break
                elif copy_scores[j] <= sorted_scores[i] and copy_scores[j] != copy_scores[0]:
                    lowest_2nd_score_2 = names[j + 1]
                    break
                else:
                    lowest_2nd_score_2 = False
                    pass
            break
        else:
            pass
    
    lowest_name = names[lowest_2nd_score]

    low_data = [lowest_name, lowest_2nd_score_2]
    if low_data[1] != False:
        for i in range(len(low_data)):
            print(low_data[i])

    else:
        print(low_data[0])
            
def alt_solute():    
    if __name__ == '__main__':
        data_names = []
        data_scores = []
        # sub_data = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            
            data_names.append(name)
            data_scores.append(score)
            
        low_score(data_names, data_scores)
            
        #     sub_data.append(name)
        #     sub_data.append(score)
            
            
        # data = sorted(sub_data, reverse=True)
        # for item in data:
        #     print(item)

if __name__ == '__main__':
    students = {}
    names = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    
    
    
    for i in range(_):    
        students[i] = scores[i]
        
    for i in range(_):
        students[i].append(names[i])
        
    Low = []
    Grade = []
    Nothing = False        
    
    for i in range(_):
        print(students)
        
    # Grades = sorted(students)

    
    for i in range(_):
        if scores[0] < scores[i]:
            Low.append(i)
            Grade.append(scores[i])
            scores.remove(scores[i])
            
            for j in range(_*2):
                for a in range(_):
                    if scores[a] == Grade[i]:
                        Low.append(a)
                        Nothing = True
                        break
                    else:
                        pass
                        
                if not Nothing:
                    break
            
        else:
            pass
        
    
    Low_grades = []
    
    for i in range(_):
        for f in range(_):
            if students[f] == students[Low[i]]:
                Low_grades.append(students[i])