# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 11:27:51 2022

@author: kaosa
"""

import random
import time as t

def rand_chromo(size): 
    return [ random.randint(1, Nq) for _ in range(Nq) ]

def fitness(chromosome):
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2
    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    
    return int(maxFitness - (horizontal_collisions + diagonal_collisions)) 

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
    
        if upto + w >= r:
            return c
        upto += w
        
    assert False, "Shouldn't get here"
        
def reproduce(x, y): 
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) #best 1
        y = random_pick(population, probabilities) #best 2
        child = reproduce(x, y) 
        if random.random() < mutation_probability:
            child = mutate(child)
        print_chrom(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
    return new_population

def print_chrom(chrom):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chrom), fitness(chrom)))

if __name__ == "__main__":
    Nq = int(input("Enter Number of Queens: "))
    
    startTime = t.time()
    maxFitness = (Nq*(Nq-1))/2  
    population = [rand_chromo(Nq) for _ in range(100)]
    
    generation = 1

    while not maxFitness in [fitness(chrom) for chrom in population]:
        print("=== Epoch {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        print("Maximum Fitness = {}".format(max([fitness(n) for n in population])))
        generation += 1
    chrom_out = []
    print("Solved in Generation {}".format(generation-1))
    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("");
            print("Best solution: ")
            chrom_out = chrom
            print_chrom(chrom)
    endTime = t.time()        
            
    board = []

    for x in range(Nq):
        board.append(["x"] * Nq)
        
    for i in range(Nq):
        board[Nq-chrom_out[i]][i]="Q"
            

    def print_board(board):
        for row in board:
            print (" ".join(row))
            
    print()
    print_board(board)
    print("Total time Taken:  ", endTime - startTime)
    
#%%
#Back Trackig
import time

n = int(input("Enter the value of N: "))
print("Results: ")
cnt=0

#starting time
starting_time = time.time()

def solveNQueens(n):
    
        col = set()
        posDiag = set() # (r+c)
        negDiag = set() # (r-c)
        
        board = [-1] * n 
        
        def backtrack(r):
            global cnt
            if r==n:              
                print(board)
                cnt+=1
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r]=c
           
                backtrack(r+1)
       
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r]=-1
             
        backtrack(0)
        return

solveNQueens(n)

# Ending Time
ending_time = time.time()

# get the execution time
elapsed_time = ending_time - starting_time

print("Total no. of Solutions: ", cnt)
print("Execution time:", elapsed_time, "seconds")
                
    
 