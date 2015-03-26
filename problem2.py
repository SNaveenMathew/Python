# Problem 2
# Finding dictionary rank of a combination of letters. 
#
# Your function should do the following: 
#
# Given an array of letters as input, first find all permutations of those letters (without using a permutation library). 
# Next, for each permutation, a resulting word that one can be formed through combining all the letters (it doesn't need to be an actual english word). Create a sorted array of all these words. 
# Finally, it should also take a word as input, and find its rank in that sorted array. 
#
# The output of your function should be the position of the word whose rank you need to output. 
#
# Hence, your function / input could be the following: 
#
# function ( ['c', 'a', 'r'], 'arc')
#
# Output would be position of 'arc' in the following --- in this case, 2. 
#
# acr 
# arc
# car
# cra
# rac
# rca


# Solution:
# Assumptions: All n! permutations will be stored, but ranking will be calculated after removing repetitions

# This function sorts the list containing all permutations
# Selection sort algorithms is used
def sort(nextlist,len2) :
    a=0
    while(a<len2) :
        small=nextlist[a]
        b=a+1
        k=a
        while(b<len2) :
            if(nextlist[b]<small) :
                small=nextlist[b]
                k=b
            b=b+1
        if(k!=a) :
            small=nextlist[a]
            nextlist[a]=nextlist[k]
            nextlist[k]=small
        a=a+1


# Checks whether the contents of the list and the string are same
def compare(list1,string1) :
    length=len(list1)
    i=0
    prod=1
    while(i<length) :
        prod=prod*(list1[i]==string1[i])
        i=i+1
    return prod


# This function is used to generate all permutations
def permute(list1,i,n,k,nextlist) :
    # Complete permutation is generated if the following condition is met
    if(i==n) :
        nextlist[k[0]]=['a']*(n+1)
        j=0
        while(j<=n) :
            nextlist[k[0]][j]=list1[j]
            j=j+1
        k[0]=k[0]+1

    else :
        j=i
        while(j<=n) :
            prevlist=list1
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
            # Repeat the next step till a permutation is generated
            permute(list1,i+1,n,k,nextlist)
            # This step is called backtracking
            temp=list1[i]
            list1[i]=list1[j]
            list1[j]=temp
            j=j+1


# This function is used to calculate the factorial of a number
def factorial(num) :
    prod=1
    i=1
    while(i<=num) :
        prod*=i
        i=i+1
    return prod


# This function returns the rank of the string in the sorted list
def ranking(nextlist,string1,k) :
    m=0
    sub=0
    ret=0
    while(m<k[0]) :
        if(m==0) :
            sub=sub+1
            if(compare(nextlist[m],string1)) :
                ret=1
        else :
            if((m!=0)*(nextlist[m]!=nextlist[m-1])) :
                sub=sub+1
                if(compare(nextlist[m],string1)) :
                    ret=sub
        m=m+1
    return ret
            


# This function performs the preprocessing required for ranking and calls the necessary function
def rank(list1,string1) :
    k=[0]
    length=len(list1)
    len2=factorial(length)
    nextlist=['a']*len2
    # Preprocessing steps: Generate all permutations, sort the list and find rank
    permute(list1,0,(length-1),k,nextlist)
    sort(nextlist,len2)
    rank1=ranking(nextlist,string1,k)
    print(nextlist)
    print(rank1)


# Taking an example to evaluate
list1=['c','a','r','a']
rank(list1,"craa")
