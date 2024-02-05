def sum_pairs(arr, sum):

    answer_key = []
    for element in range(0,len(arr),+1):
        for element2 in range(element+1, len(arr),+1):
            if(arr[element] + arr[element2] == sum):
                answer_key.append(arr[element])
                answer_key.append(arr[element2])
    if len(answer_key) == 0:
        print('unable to find pairs')
    else:
        print(answer_key)

sum_pairs([1,2,3,4,5], 9) # [[4,5]]
sum_pairs([1,2,3,4,5], 7) # [[2,5], [3,4]]
sum_pairs([3, 1, 5, 8, 2], 27) # 'unable to find pairs'