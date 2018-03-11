from Bio import SeqIO

# Создаем класс с информацией о kmers.
class Kmer:
    
    sequence = ''
    
    # Создаем функции с атрибутами класса(счетчик встречаемости,
    # последовательность, место в хромосоме).
    def __init__(self,kmer_name):
    
        self.sequence = kmer_name
        self.counter = 1
        self.locus = []
    # Эта функция будет увеличивать счетчик встречаемости камера.    
    def increase(self):
        self.counter += 1
    # Эта функция будет увеличивать список локусов каждого камера.
    def add_loc(self, m):
        self.locus.append(m)
    # Эта функция будет печатать локусы камера и их хромосому.    
    def printloc(self, chrom, locus): 
        print('chrom_name:', chrom, 'locus:',locus)


with open('/home/gospozha/forpython/2 /seq_y_pestis.fasta', "r") as handle:
        # Читаем fasta файл, содержимое записываем в переменную.
        records = list(SeqIO.parse(handle, "fasta"))
        handle.close() 
# Записываем в переменные последовательность хромосомы и ее имя.                           
seq = str(records[0].seq)
chrom = str(records[0].name)
# Отбираем для удобства 100000 нуклеотидов
seq = seq[100000:200000]
seq_lng = len(seq)
# Длина камера, который будем искать
kmer_size = 23
kmer_dict = {}
# Берем каждый камер (последовательно сдвигаемся на 1 нуклеотид и запоминаем 
# последовательность из 23 нуклеотидов.)
for index in range(seq_lng-kmer_size+1):
    current_kmer = seq[index:(index+kmer_size)] 
    # Если камер уже в словаре камеров, увеличиваем его счетчик встречаемости 
    # еще на 1. Если нет, записываем в словарь камеров.      
    if current_kmer in kmer_dict:
        kmer_dict[current_kmer].increase()
    else:
        kmer_dict[current_kmer] = Kmer(current_kmer) 
    # Добавляем экземпляру класса Kmer значение объекта locus.
    kmer_dict[current_kmer].add_loc(index)
# Составляем список всех значений счетчиков камеров, ищем максимальное.      
arr = []
for key in kmer_dict.keys():    
    arr.append(kmer_dict[key].counter)
a = max(arr)

# Вытаскиваем все камеры с этим максимальным значением счетчика, для каждого
# печатам информацию.
for key in kmer_dict.keys():
    if kmer_dict[key].counter == a:
        print('kmer:',key)
        print('locus_list:',kmer_dict[key].locus)
        print('Details:')
        for i in range(a):
            kmer_dict[key].printloc(chrom, kmer_dict[key].locus[i])
        print('')
        