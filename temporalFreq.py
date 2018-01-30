import os, sys, dendropy as dp, numpy as np

'''
The script is designed with special parameters and inputs for the Extended Data 6 in the manuscript :
Title: Millennia of genomic stability within the invasive Para C Lineage of Salmonella enterica. 
Authors: Zhemin Zhou, Inge Lundstrøm, Alicia Tran-Dien, Sebastián Duchêne, Nabil-Fareed Alikhan, 
         Martin J. Sergeant, Gemma Langridge, Anna K. Fotakis, Satheesh Nair, Hans K. Stenøien, 
         Stian S. Hamre, Sherwood Casjens, Axel Christophersen, Christopher Quince, Nicholas R. Thomson, 
         François-Xavier Weill, Simon Y. W. Ho, M. Thomas P. Gilbert, Mark Achtman

Copyright Zhemin Zhou, Mark Achtman (2017)
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but without
any warranty; without even the implied warranty of merchantability or fitness
for a particular purpose. See the GNU General Public License for more details. 
'''

xs = ['SNP']
if __name__ == '__main__' :
    event, y, strain_start, strain_end, branch_end, max_year = sys.argv[1:]
    max_year = (int(max_year) + 50)*10
    ys = y.split(',')
    branches, gis = {}, {}

    recording = 0
    with open(event) as fin :
        for line in fin :
            part = line.strip().split()
            if part[0] == strain_start: recording = 1
            if recording == 0 :
                continue

            events = [p.split(',') for p in part[1].split(';')]
            
            branches[part[0]] = []
            for path in events :
                branches[part[0]].append([])
                for t, n in zip(*[path[i::2] for i in xrange(2)]) :
                    if path[0] == branch_end :
                        break
                    
                    if t in xs :
                        branches[part[0]][-1].append([t, 'x', int(n)])
                    else :
                        if n.find(":") >= 0 :
                            name, num = n.split(':')
                        else :
                            name, num = n, 1
                        if t in ys :
                            branches[part[0]][-1].append([t, name, int(num)])
                            gis[name] = 1
                    if path[0] == branch_end :
                        break
                    
            if part[0] == strain_end: recording = 0
            
    acc = np.zeros([1000, max_year])
    
    for ite in xrange(1000) :
        p = set(np.random.choice(gis.keys(), len(gis)))
        a = np.zeros(max_year)
        for br, events in branches.iteritems() :
            c = 0
            for event in events :
                x_move, y_move = 0, 0.
                for t, n, nn in event :
                    if t in xs :
                        x_move += nn
                    elif n in p :
                        y_move += nn
                if y_move > 0 :
                    if x_move > 0 :
                        y_move = y_move/x_move
                x_move = int(float(x_move)*10./4850000/9.4e-8)
                a[c:(c+x_move)] += y_move
                c += x_move
                if c >= max_year : break
        acc[ite] = a/len(branches)
    for i in np.arange(0, max_year, 500) :
        s = np.sum(acc.T[i:(i+500)], 0)/500.0
        s.sort()
        print i/10, np.mean(s), s[25], s[975]