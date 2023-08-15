#!/usr/bin/python3

#!/usr/bin/python3
from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path = 'test.pdf', language = 'ru'):
    """
        Конвертируйте любые книги и журналы формата pdf в mp3 формат для аудио-прослушивания, чтобы не отвлекаясь заниматься основной работой и при этом слушать прочтение любимых книг.
    """
    
    if Path(file_path).is_file() and Path(file_path).suffix =='.pdf':
        
        print(f'[+] Оригинальный файл: {Path(file_path).name}')
        print('[+] Процесс запущен...')
        
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            
        text = ''.join(pages)
        text = text.replace('\n', '')
        
        my_audio = gTTS(text = text, lang = language, slow = False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        
        return f'[+] {file_name}.mp3 создан успешно!'
    else:
        return 'Файл не существует!'
        
    def main():
        tprint('PDF>>TO>>MP3', font = 'bulbhead')
        
        file_path = input('\nВведи путь до файла: ')
        language = input("Выбери язык, например 'en' или 'ru': ")
        print(pdf_to_mp3(file_path = file_path, language = language))
        #print(pdf_to_mp3(file_path = '/home/nimda/Desktop/PDF_to_MP3/pdf2mp3/Ничего_личного.pdf'))
    
#if __name__ == '__main__':
    #main()
        

