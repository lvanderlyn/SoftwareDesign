    # # -*- coding: utf-8 -*-
    # """
    # Created on Sun Feb  2 11:24:42 2014
    
    # @author: Lindsey Vanderlyn
    # """
    
    # # you may find it useful to import these variables (although you are not required to use them)
    # from amino_acids import aa, codons
    # from random import shuffle
    # from load import load_seq, load_salmonella_genome
    
    # def collapse(L):
    #     """ Converts a list of strings to a string by concatenating all elements of the list """
    #     output = ""
    #     for s in L:
    #         output = output + s
    #     return output
    
    
    # def coding_strand_to_AA(dna):
    #     """ Computes the Protein encoded by a sequence of DNA.  This function
    #         does not check for start and stop codons (it assumes that the input
    #         DNA sequence represents an protein coding region).
            
    #         dna: a DNA sequence represented as a string
    #         returns: a string containing the sequence of amino acids encoded by the
    #                  the input DNA fragment
    #     """
              
    #     amino_acid = ""                         #Sets a blank string to be filled
    #     count = len(dna)/3                      #determines the number of actual codons         
    #     for iteration in range(count):
    #         #breaks string up into codons
    #         codon_start = iteration*3
    #         codon_stop = 3 + codon_start
    #         codon = dna[codon_start: codon_stop]
    #         length = len(codons)
    #         for index in range(length):
    #             #searches which amino acid matches the codon
    #             if codon in codons[index]:
    #                 amino_acid += aa[index]
    #     #print amino_acid
    #     return amino_acid
            
        
    # def coding_strand_to_AA_unit_tests():
    #     """ Unit tests for the coding_strand_to_AA function """
            
    #     print coding_strand_to_AA('TTTTTA')         #expected output should match 'FL'
        
    #     print coding_strand_to_AA('CGTCCGCCT')    #expected output should match 'RRG'
    
    # def get_reverse_complement(dna):
    #     """ Computes the reverse complementary sequence of DNA for the specfied DNA
    #         sequence
        
    #         dna: a DNA sequence represented as a string
    #         returns: the reverse complementary DNA sequence represented as a string
    #     """
    #     complement = ''                     #Sets up string to fill
    #     end = len(dna)
    #     for index in range(end):
    #         #Uses series of if statements to match the letter to compliment, going in reverse order through the string
    #         letter = dna[end-(index+1)]
    #         if letter == 'T':
    #             complement += 'A'
    #         elif letter == 'A':
    #             complement += 'T'
    #         elif letter == 'C':
    #             complement += 'G'
    #         elif letter == 'G':
    #             complement += 'C'
    #     return complement
            
        
    # def get_reverse_complement_unit_tests():
    #     """ Unit tests for the get_complement function """
            
    #     print get_reverse_complement('AAAGCGGGCAT')
    #     #expect to return 'ATGCCCGCTTT'
    #     print get_reverse_complement('TGAACGCGG')
    #     #expect to return 'CCGCGTTCA'
    # def rest_of_ORF(dna):
    #     """ Takes a DNA sequence that is assumed to begin with a start codon and returns
    #         the sequence up to but not including the first in frame stop codon.  If there
    #         is no in frame stop codon, returns the whole string.
            
    #         dna: a DNA sequence
    #         returns: the open reading frame represented as a string
    #     """
    #     ORF = ''
    #     count = len(dna)/3                      #determines the number of actual codons         
    #     for iteration in range(count):
    #         #breaks string up into codons
    #         codon_start = iteration*3
    #         codon_stop = 3 + codon_start
    #         codon = dna[codon_start: codon_stop]
    #         if codon != 'TAG' and codon != 'TGA' and codon != 'TAA':
    #             ORF += codon
    #         else:
    #             break
    #     return ORF
    
    # def rest_of_ORF_unit_tests():
    #     """ Unit tests for the rest_of_ORF function """
            
    #     print rest_of_ORF('ATGAAATGAA')    #expected output: 'ATGAAA'
            
    #     print rest_of_ORF('TGAAAAATGAGATAGG') #expected output: 'ATGAGA;
            
    # def find_all_ORFsoneframe(dna):
    #     """ finds all ORFs in one frame that are not nested within each other """    
        
    #     #sets up variables to be filled in rest of program
    #     all_ORFs = []
    #     index = 0
    #     ORF = ''
    #     Codon_list = []
    #     count = len(dna)/3
    
    #     #breaks string input up into codons    
    #     for value in range(count):
    #         codon = dna[value*3:3+value*3]
    #         Codon_list.append(codon)
            
    #     #Looks for all open ORFs in one reading frame iterating until end of list     
    #     while index < (count -1):
    #         if Codon_list[index] == 'ATG':              #finds start codon
    #             ORF = ''
    #             for place in range(index, count):       #adds from start until stop (exlculsive)
    #                 if Codon_list[place] != 'TAG' and Codon_list[place] != 'TGA' and Codon_list[place] != 'TAA':
    #                     ORF += Codon_list[place]
    #                     if place == count-1:            #If no end codon, closes ORF and adds to all_ORFs
    #                         all_ORFs.append(ORF)
    #                         index = place 
    #                         break
    #                 else:                               #closes ORF and adds codons to all_ORFs
    #                     all_ORFs.append(ORF)
    #                     index = place
    #                     break
    #         else:
    #             index += 1      #increases index to check next one for start codon
           
    #     return all_ORFs
        
    # #print find_all_ORFsoneframe('ATGCATGAATGTAG')     
    # def find_all_ORFs_oneframe_unit_tests():
    #     """ Unit tests for the find_all_ORFs_oneframe function """
        
    #     print find_all_ORFsoneframe('CATTGGGATGCATGAATGTAGATAGATGTGCCG') 
    #     #expected output:['ATGCATGAATGTAGA', 'ATGTGCCG']
    
    # def find_all_ORFs(dna):
    #     """ Finds all non-nested open reading frames in the given DNA sequence in all 3
    #         possible frames and returns them as a list.  By non-nested we mean that if an
    #         ORF occurs entirely within another ORF and they are both in the same frame,
    #         it should not be included in the returned list of ORFs.
       
    #         dna: a DNA sequence
    #         returns: a list of non-nested ORFs
    #     """
        
    #     All_ORFs = []
    #     for shift in range(3):
    #         segment = dna[shift:]
    #         Frame = find_all_ORFsoneframe(segment)
    #         if len(Frame) >= 1:                     #checks to make sure frame is not empty
    #             All_ORFs+=(Frame)
            
    #     return All_ORFs
        
    # #print find_all_ORFs('ATGCGAATGTAGCATCAAA', 1) 
    
    # def find_all_ORFs_unit_tests():
    #     """ Unit tests for the find_all_ORFs function """
        
    #     print find_all_ORFs('TTTATGCATGAATGTAG')    
    #     #Expected output is [['ATGCATGAATGT'], ['ATGAATGTA'], ['ATG']]
    
    # def find_all_ORFs_both_strands(dna):
    #     """ Finds all non-nested open reading frames in the given DNA sequence on both
    #         strands.
            
    #         dna: a DNA sequence
    #         returns: a list of non-nested ORFs
    #     """
    #     All_reading_frames = []             #initializes list to store reading frames in
    #     ORF = find_all_ORFs(dna)
    #     All_reading_frames += (ORF)         #adds all reading frames from normal dna
    #     reverse = get_reverse_complement(dna)
    #     All_reading_frames += (find_all_ORFs(reverse))  #adds reading frames of reverse dna
    #     return All_reading_frames
        
    # #print find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
    
    # def find_all_ORFs_both_strands_unit_tests():
    #     """ Unit tests for the find_all_ORFs_both_strands function """
    
    #     print find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
    #     #Expected output = ['ATGCGAATG'], [ATGCTACATTCGCAT']
    
    # def longest_ORF(dna):
    #     """ Finds the longest ORF on both strands of the specified DNA and returns it
    #         as a string"""
    #     Reading_frames = find_all_ORFs_both_strands(dna)        #Gets list of all open reading frames (forward and reverse)
    #     length = len(Reading_frames)                            #finds length of list ot set end of for loop
    #     longest = []
    #     for index in range(length):
    #     #goes through comparing the lengths of each ORF and keeping the higher one for the next interation
    #         Compare = Reading_frames[index]
    #         if len(Compare) > len(longest):
    #             longest = Compare
    #         else:
    #             longest = longest
    #     return longest                                          #after it has compared all ORFs the longest is returned
        
    # #print longest_ORF('ATGCGAATGTAGCATCAAA')
            
    
    # def longest_ORF_unit_tests():
    #     """ Unit tests for the longest_ORF function """
    
    #     print longest_ORF('ATGCGAATGTAGCATCAAA')
    #     #should return 'ATGCTACATTCGCAT'
    
    #     print longest_ORF('ATGCCAATGAAATGA')
    #     #should return 'ATGCCAATGAAA'
    
    # def longest_ORF_noncoding(dna, num_trials):
    #     """ Computes the maximum length of the longest ORF over num_trials shuffles
    #         of the specfied DNA sequence
            
    #         dna: a DNA sequence
    #         num_trials: the number of random shuffles
    #         returns: the maximum length longest ORF """
    
    #     DNA = list(dna)                                 #converst dna into a mutable list
    #     longest_frame = []              
    #     for iteration in range(num_trials):             #cycles through num_trials number of iterations recording the length of the longest ORF
    #         longest_frame.append(longest_ORF(DNA))
    #         shuffle(DNA)
    #     compare = []
    #     for index in range(len(longest_frame)):         #cycles through num_trials number of indexes comparing to find longest ORF
    #         if len(longest_frame[index]) > len(compare):
    #             compare = longest_frame[index]
    #         else:
    #             compare = compare
    #     return len(compare)
            
    # #print longest_ORF_noncoding('ATGCGAATGTAGCATCAAA', 30)
    
    # def gene_finder(dna, threshold):
    #     """ Returns the amino acid sequences coded by all genes that have an ORF
    #         larger than the specified threshold.
            
    #         dna: a DNA sequence
    #         threshold: the minimum length of the ORF for it to be considered a valid
    #                   gene.
    #         returns: a list of all amino acid sequences whose ORFs meet the minimum
    #                  length specified.
    #     """
    #     amino_acids = []
    #     all_frames = find_all_ORFs_both_strands(dna)
    #     for index in range(len(all_frames)):                            #if the length of ORF is above the threshold, adds it to list
    #         if len(all_frames[index]) > threshold:
    #             amino_acids.append(coding_strand_to_AA(all_frames[index])) #finds amino acids coresponding to codons from above list
    #     return amino_acids
    # if __name__ == '__main__':
    #     dna = load_seq('./data/X73525.fa') 
    #     gene_finder(dna,600)    
    #     print(gene_finder(dna, 600))


    # -*- coding: utf-8 -*-
    """
    Created on Sun Feb  2 11:24:42 2014
    
    @author: Lindsey Vanderlyn
    """
    
    # you may find it useful to import these variables (although you are not required to use them)
    from amino_acids import aa, codons
    from random import shuffle
    from load import load_seq, load_salmonella_genome
    
    def collapse(L):
        """ Converts a list of strings to a string by concatenating all elements of the list """
        output = ""
        for s in L:
            output = output + s
        return output
    
    
    def coding_strand_to_AA(dna):
        """ Computes the Protein encoded by a sequence of DNA.  This function
            does not check for start and stop codons (it assumes that the input
            DNA sequence represents an protein coding region).
            
            dna: a DNA sequence represented as a string
            returns: a string containing the sequence of amino acids encoded by the
                     the input DNA fragment
        """
              
        amino_acid = ""                         #Sets a blank string to be filled
        count = len(dna)/3                      #determines the number of actual codons         
        for iteration in range(count):
            #breaks string up into codons
            codon_start = iteration*3
            codon_stop = 3 + codon_start
            codon = dna[codon_start: codon_stop]
            length = len(codons)
            for index in range(length):
                #searches which amino acid matches the codon
                if codon in codons[index]:
                    amino_acid += aa[index]
        #print amino_acid
        return amino_acid
            
        
    def coding_strand_to_AA_unit_tests():
        """ Unit tests for the coding_strand_to_AA function """
            
        print coding_strand_to_AA('TTTTTA')         #expected output should match 'FL'
        
        print coding_strand_to_AA('CGTCCGCCT')    #expected output should match 'RRG'
    
    def get_reverse_complement(dna):
        """ Computes the reverse complementary sequence of DNA for the specfied DNA
            sequence
        
            dna: a DNA sequence represented as a string
            returns: the reverse complementary DNA sequence represented as a string
        """
        complement = ''                     #Sets up string to fill
        end = len(dna)
        for index in range(end):
            #Uses series of if statements to match the letter to compliment, going in reverse order through the string
            letter = dna[end-(index+1)]
            if letter == 'T':
                complement += 'A'
            elif letter == 'A':
                complement += 'T'
            elif letter == 'C':
                complement += 'G'
            elif letter == 'G':
                complement += 'C'
        return complement
            
        
    def get_reverse_complement_unit_tests():
        """ Unit tests for the get_complement function """
            
        print get_reverse_complement('AAAGCGGGCAT')
        #expect to return 'ATGCCCGCTTT'
        print get_reverse_complement('TGAACGCGG')
        #expect to return 'CCGCGTTCA'
    def rest_of_ORF(dna):
        """ Takes a DNA sequence that is assumed to begin with a start codon and returns
            the sequence up to but not including the first in frame stop codon.  If there
            is no in frame stop codon, returns the whole string.
            
            dna: a DNA sequence
            returns: the open reading frame represented as a string
        """
        ORF = ''
        count = len(dna)/3                      #determines the number of actual codons         
        for iteration in range(count):
            #breaks string up into codons
            codon_start = iteration*3
            codon_stop = 3 + codon_start
            codon = dna[codon_start: codon_stop]
            if codon != 'TAG' and codon != 'TGA' and codon != 'TAA':
                ORF += codon
            else:
                break
        return ORF
    
    def rest_of_ORF_unit_tests():
        """ Unit tests for the rest_of_ORF function """
            
        print rest_of_ORF('ATGAAATGAA')    #expected output: 'ATGAAA'
            
        print rest_of_ORF('TGAAAAATGAGATAGG') #expected output: 'ATGAGA;
            
    def find_all_ORFsoneframe(dna):
        """ finds all ORFs in one frame that are not nested within each other """    
        
        #sets up variables to be filled in rest of program
        all_ORFs = []
        index = 0
        ORF = ''
        Codon_list = []
        count = len(dna)/3
    
        #breaks string input up into codons    
        for value in range(count):
            codon = dna[value*3:3+value*3]
            Codon_list.append(codon)
            
        #Looks for all open ORFs in one reading frame iterating until end of list     
        while index < (count -1):
            if Codon_list[index] == 'ATG':              #finds start codon
                ORF = ''
                for place in range(index, count):       #adds from start until stop (exlculsive)
                    if Codon_list[place] != 'TAG' and Codon_list[place] != 'TGA' and Codon_list[place] != 'TAA':
                        ORF += Codon_list[place]
                        if place == count-1:            #If no end codon, closes ORF and adds to all_ORFs
                            all_ORFs.append(ORF)
                            index = place 
                            break
                    else:                               #closes ORF and adds codons to all_ORFs
                        all_ORFs.append(ORF)
                        index = place
                        break
            else:
                index += 1      #increases index to check next one for start codon
           
        return all_ORFs
        
    #print find_all_ORFsoneframe('ATGCATGAATGTAG')     
    def find_all_ORFs_oneframe_unit_tests():
        """ Unit tests for the find_all_ORFs_oneframe function """
        
        print find_all_ORFsoneframe('CATTGGGATGCATGAATGTAGATAGATGTGCCG') 
        #expected output:['ATGCATGAATGTAGA', 'ATGTGCCG']
    
    def find_all_ORFs(dna):
        """ Finds all non-nested open reading frames in the given DNA sequence in all 3
            possible frames and returns them as a list.  By non-nested we mean that if an
            ORF occurs entirely within another ORF and they are both in the same frame,
            it should not be included in the returned list of ORFs.
       
            dna: a DNA sequence
            returns: a list of non-nested ORFs
        """
        
        All_ORFs = []
        for shift in range(3):
            segment = dna[shift:]
            Frame = find_all_ORFsoneframe(segment)
            if len(Frame) >= 1:                     #checks to make sure frame is not empty
                All_ORFs+=(Frame)
            
        return All_ORFs
        
    #print find_all_ORFs('ATGCGAATGTAGCATCAAA', 1) 
    
    def find_all_ORFs_unit_tests():
        """ Unit tests for the find_all_ORFs function """
        
        print find_all_ORFs('TTTATGCATGAATGTAG')    
        #Expected output is [['ATGCATGAATGT'], ['ATGAATGTA'], ['ATG']]
    
    def find_all_ORFs_both_strands(dna):
        """ Finds all non-nested open reading frames in the given DNA sequence on both
            strands.
            
            dna: a DNA sequence
            returns: a list of non-nested ORFs
        """
        All_reading_frames = []             #initializes list to store reading frames in
        ORF = find_all_ORFs(dna)
        All_reading_frames += (ORF)         #adds all reading frames from normal dna
        reverse = get_reverse_complement(dna)
        All_reading_frames += (find_all_ORFs(reverse))  #adds reading frames of reverse dna
        return All_reading_frames
        
    #print find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
    
    def find_all_ORFs_both_strands_unit_tests():
        """ Unit tests for the find_all_ORFs_both_strands function """
    
        print find_all_ORFs_both_strands('ATGCGAATGTAGCATCAAA')
        #Expected output = ['ATGCGAATG'], [ATGCTACATTCGCAT']
    
    def longest_ORF(dna):
        """ Finds the longest ORF on both strands of the specified DNA and returns it
            as a string"""
        Reading_frames = find_all_ORFs_both_strands(dna)        #Gets list of all open reading frames (forward and reverse)
        length = len(Reading_frames)                            #finds length of list ot set end of for loop
        longest = []
        for index in range(length):
        #goes through comparing the lengths of each ORF and keeping the higher one for the next interation
            Compare = Reading_frames[index]
            if len(Compare) > len(longest):
                longest = Compare
            else:
                longest = longest
        return longest                                          #after it has compared all ORFs the longest is returned
        
    #print longest_ORF('ATGCGAATGTAGCATCAAA')
            
    
    def longest_ORF_unit_tests():
        """ Unit tests for the longest_ORF function """
    
        print longest_ORF('ATGCGAATGTAGCATCAAA')
        #should return 'ATGCTACATTCGCAT'
    
        print longest_ORF('ATGCCAATGAAATGA')
        #should return 'ATGCCAATGAAA'
    
    def longest_ORF_noncoding(dna, num_trials):
        """ Computes the maximum length of the longest ORF over num_trials shuffles
            of the specfied DNA sequence
            
            dna: a DNA sequence
            num_trials: the number of random shuffles
            returns: the maximum length longest ORF """
    
        DNA = list(dna)                                 #converst dna into a mutable list
        longest_frame = []              
        for iteration in range(num_trials):             #cycles through num_trials number of iterations recording the length of the longest ORF
            longest_frame.append(longest_ORF(DNA))
            shuffle(DNA)
        compare = []
        for index in range(len(longest_frame)):         #cycles through num_trials number of indexes comparing to find longest ORF
            if len(longest_frame[index]) > len(compare):
                compare = longest_frame[index]
            else:
                compare = compare
        return len(compare)
            
    #print longest_ORF_noncoding('ATGCGAATGTAGCATCAAA', 30)
    
    def gene_finder(dna, threshold):
        """ Returns the amino acid sequences coded by all genes that have an ORF
            larger than the specified threshold.
            
            dna: a DNA sequence
            threshold: the minimum length of the ORF for it to be considered a valid
                       gene.
            returns: a list of all amino acid sequences whose ORFs meet the minimum
                     length specified.
        """
        amino_acids = []
        all_frames = find_all_ORFs_both_strands(dna)
        for index in range(len(all_frames)):                            #if the length of ORF is above the threshold, adds it to list
            if len(all_frames[index]) > threshold:
                amino_acids.append(coding_strand_to_AA(all_frames[index])) #finds amino acids coresponding to codons from above list
        return amino_acids
    if __name__ == '__main__':
        dna = load_seq('./data/X73525.fa') 
        gene_finder(dna,600)    
        print(gene_finder(dna, 600))
