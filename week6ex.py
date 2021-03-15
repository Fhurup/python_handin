from webget import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class Book():
    _book_names = []
    counter = 1

    def __init__(self, url_list):
         self.url_list = url_list

    def downloadBook(self, url):
        try:
            download(url)
        except (NotFoundException) as e:
            print("NotFoundException", e)
    
    def multi_download(self, workers=5):
        with ThreadPoolExecutor(workers) as ex:
            ex.map(self.downloadBook, self.url_list)
            res = ex.map(self.names, self.url_list)
            self._book_names = list(res)
        return list(res)

    def names(self, url):
        filename = os.path.basename(urlparse(url).path)
        return filename

    def avg_vowels(self, file):
        avg_v_list = []

        with open(file) as f_obj:
            for line in f_obj:
                for word in line.split():
                    avg_v_list.append(self.count_vowels(word))
        avg = self.Average(avg_v_list)
        return avg
           
    def count_vowels(self, text):
        lowercase = text.lower()
        vowel_counts = {}

        for vowel in "aeiouy":
            count = lowercase.count(vowel)
            vowel_counts[vowel] = count
        
        counts = vowel_counts.values()
        total_vowels = sum(counts)
        return total_vowels

    def Average(self, lst): 
        return sum(lst) / len(lst) 

    def __iter__(self):
        return self

    def __next__(self):
        length = len(self._book_names)
        if self.counter <= length:
            self.counter += 1
            return self._book_names[self.counter-2]
        else:
            self.counter = 1
            raise StopIteration

    def urllist_generator(self):
        length = len(self._book_names)
        while self.counter <= length:
            yield self.url_list[self.counter-1]
            self.counter += 1
    
    def hardest(self):
        hardest = {}
        r_hard = {}
        books = self.multi_download()

        for b in self._book_names:
            hardest[b] = self.avg_vowels(b)

        values =  dict(sorted(hardest.items(), key=lambda item: item[1],reverse=True)).values()
        values_list = list(values)
        r_hard[next(iter(hardest))] = values_list[0]
        return r_hard
    
    def all_hard(self):
        hardest = {}
        books = self.multi_download()
        for b in self._book_names:
            hardest[b] = self.avg_vowels(b)
        return dict(sorted(hardest.items(), key=lambda item: item[1],reverse=True))

new_book = Book(["https://www.gutenberg.org/files/1232/1232-0.txt", "https://www.gutenberg.org/files/1342/1342-0.txt"])

##print(new_book.avg_vowels("1342-0.txt"))
##print(new_book.count_vowels("hejAyueiwq"))
hej = new_book.multi_download()
for i in new_book:
    print(i)
print(new_book.counter)
urls = new_book.urllist_generator()
print(urls)
for u in urls:
    print(u)

print(new_book.hardest())
print(new_book.all_hard())

##new_book.downloadBook("https://www.gutenberg.org/files/1232/1232-0.txt", "hedk.txt")cl