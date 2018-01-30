Data and script for extracting rate of gene gain/loss and pseudogenes from the branches of an ML tree.

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

Folder structure:
	temporalFreq.py: A script to generate the matrix used for the curve plot in Figure S2. 
	events.onBranch: The input for temporalFreq.py. This input is generated based on Additional Data 12 and 13. 
	ParatyphiC.island.mat: The matrix that is used to generat Figure S2A. 
	ParatyphiC.pseudogene.mat: The matrix that is used to generat Figure S2B. 

Requirements:
	pip packages: 
		dendropy
		numpy
	

Commands to generate the matrices :
	python temporalFreq.py events.onBranch island FA1062AA HA1701AA Br_437 1400 > ParatyphiC.island.mat
	python temporalFreq.py events.onBranch pseudogene FA1062AA HA1701AA Br_437 1400 > ParatyphiC.pseudogene.mat

Usage:
	python temporalFreq.py <input.file> <y.category> <start.tip> <end.tip> <MRCA.branch> <year.range> > <output.filt>
		input.file: specialized input file. Example: "events.onBranch"
		y.category: the category of events to be recorded. 
		start.tip: the first strain in the target sub-lineage. 
		end.tip: the last strain in the target sub-lineage. 
		MRCA.branch: the name of the branch before the MRCA of the sub-lineage. Events before the MRCA will not be recorded. 
		year.range: The range of the tip-to-root year (X axis)
		output.file: The output is redirected from standard output. 
