Liver_data=open('C:/Users/deand/Downloads/reproduce_liver_analysis/Table_S1.txt','r')
lines_of_Liver_data=Liver_data.readlines()
list=[]
count=0
# loop over each measured gene
for line in lines_of_Liver_data:
    count=count+1
    line=line.split('\t')
    line.append(count)
    genes=line[0]
    genes=genes.split(';')
    sub_count = 0
    #split the genes names of each gene and add to new list as it's own gene
    # however record where it came from
    for gene in genes:
        sub_count=sub_count+1
        data=line
        data[0]=gene
        data[-2]=data[-2].strip('\n')
        level=("{}!{}").format(count,sub_count)
        data[-1]=level
        with open("C:/Users/deand/Downloads/reproduce_liver_analysis/raw_expression_counts_liver_lobules_genes_splitted_with_counted_number_of_subgenes.txt", "a") as output:
            output.write(str(data))
            output.write('\n')
