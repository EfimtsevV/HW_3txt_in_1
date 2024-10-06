from src.Classes import Txt_merge

file_names = ['1.txt', '2.txt', '3.txt']
output_file = '3txt_in_1.txt'

txt_merge = Txt_merge()

txt_merge.merge_files(file_names, output_file)

