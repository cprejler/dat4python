# Create a module containing a class with the following methods:

# init(self, url_list)
# download(url,filename) raises NotFoundException when url returns 404
# multi_download() uses threads to download multiple urls as text and stores filenames as a property
# iter() returns an iterator
# next() returns the next filename (and stops when there are no more)
# urllist_generator() returns a generator to loop through the urls
# avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.
import requests
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import glob
import os


class NotFoundException(Exception):
    def __init__(self, message, status_code):
        error_message = f"Error message : {message}. status code : {status_code}"
        super().__init__(error_message)


class BookData:

    def __init__(self, url_list, filenames):
        self.url_list = url_list
        self.filenames = filenames

    def __iter__(self, start=0):
        self.count = start

    def __next__(self):
        if self.count < len(self.url_list):
            self.count += 1
            return self.url_list[self.count - 1]
        else:
            raise StopIteration

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def download(self, url, filename):
        r = requests.get(url)

        if r.status_code == '404':
            raise NotFoundException("Couldn't find resource", r.status_code)
        os.chdir('/home/casper/notebooks/exercise_06/books/')
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)

    def multi_download(self):
        pool = ThreadPoolExecutor(len(self.url_list))
        pool.map(lambda x, y: self.download(x, y),
                 self.url_list, self.filenames)

    def avg_vowels(self, text):
        vowels = "AaEeIiOoUu"
        count = len([char for char in text if char in vowels])
        return count

    def get_file_contents(self, filename):
        os.chdir('/home/casper/notebooks/exercise_06/books/')
        with open(filename) as file:
            contents = file.read()
            return contents

    def hardest_read(self):
        books = []
        file_list = []
        for file in self.filenames:
            contents = self.get_file_contents(file)
            books.append(contents)
            file_list.append(file)           
        with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
            res = executor.map(self.avg_vowels, books)
        
        vowels = list(res)
        results = dict(zip(file_list, vowels))
            
        return (results)
            
        
        

        

url_list = ["https://www.gutenberg.org/files/2701/2701-0.txt", "https://www.gutenberg.org/files/209/209-0.txt",
            "https://www.gutenberg.org/files/46/46-0.txt", "https://www.gutenberg.org/files/42108/42108-0.txt"]

filenames = ["Moby Dick", "The Turn of the Screw",
             "A Christmas Carol", "The Slang Dictionary"]


#book_data = BookData(url_list, filenames)
# book_data.download(url_list[1])
#book_data.multi_download()

#hardest_books = book_data.hardest_read()

#print(hardest_books)