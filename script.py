from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from random import randrange
import time

driver = webdriver.Chrome()
link =  'https://www.nytimes.com/games/wordle/index.html'
driver.get(link)
driver.find_element_by_tag_name('body').click()


letters = {
'A': 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(2)")',
'B' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(6)")',
'C' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(4)")',
'D' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(4)")',
'E' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(3)")',
'F' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(5)")',
'G' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(6)")',
'H' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(7)")',
'I' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(8)")',
'J' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(8)")',
'K' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(9)")',
'L' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(10)")',
'M' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(8)")',
'N' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(7)")',
'O' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(9)")',
'P' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(10)")',
'Q' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(1)")',
'R' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(4)")',
'S' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(2) > button:nth-child(3)")',
'T' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(5)")',
'U' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(7)")',
'V' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(5)")',
'W' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(2)")',
'X' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(3)")',
'Y': 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(1) > button:nth-child(6)")',
'Z' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(2)")',
'ENTER' : 'return  document.querySelector("body > game-app").shadowRoot.querySelector("#game > game-keyboard").shadowRoot.querySelector("#keyboard > div:nth-child(3) > button:nth-child(1)")',

}

blanks = {
'r0_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r0_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r0_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r0_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r0_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(1)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

'r1_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(2)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r1_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(2)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r1_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(2)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r1_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(2)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r1_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(2)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

'r2_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(3)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r2_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(3)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r2_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(3)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r2_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(3)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r2_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(3)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

'r3_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(4)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r3_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(4)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r3_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(4)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r3_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(4)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r3_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(4)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

'r4_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(5)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r4_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(5)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r4_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(5)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r4_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(5)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r4_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(5)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

'r5_c0':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(6)").shadowRoot.querySelector("div > game-tile:nth-child(1)")',
'r5_c1':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(6)").shadowRoot.querySelector("div > game-tile:nth-child(2)")',
'r5_c2':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(6)").shadowRoot.querySelector("div > game-tile:nth-child(3)")',
'r5_c3':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(6)").shadowRoot.querySelector("div > game-tile:nth-child(4)")',
'r5_c4':  'return document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(6)").shadowRoot.querySelector("div > game-tile:nth-child(5)")',

}

words = open('wordle.txt', 'r')
lines = words.readlines()
words.close()

wordle = pd.DataFrame(columns={
    'word'
})
wordle.word = lines
wordle.word = wordle.word.map(lambda w: w.replace('\n', ''))
wordle = wordle[wordle.word != '']
wordle = wordle.sort_values('word').reset_index()
del wordle['index']

wordle['w0'] = wordle.word.map(lambda w: w[0:1])
wordle['w1'] = wordle.word.map(lambda w: w[1:2])
wordle['w2'] = wordle.word.map(lambda w: w[2:3])
wordle['w3'] = wordle.word.map(lambda w: w[3:4])
wordle['w4'] = wordle.word.map(lambda w: w[4:])

blanks_status = {
0 : 'r{}_c0',
1 : 'r{}_c1',
2 : 'r{}_c2',
3 : 'r{}_c3',
4 : 'r{}_c4'
}

absent = []
present = []
correct = ['', '' , '' , '' ,'']
incorrect = []

def random_selection(wordle):
    try:
        del wordle['index']
        del wordle['level_0']
    except:
        pass
    i = randrange(len(wordle) - 1)
    attempt = wordle[wordle.index == i].reset_index()
    return attempt


def check_attempt(r, wordle,absent, present,correct, incorrect):
    if r == 0:
        common = wordle.copy()#wordle[(wordle.word.str.contains('m')) & (wordle.word.str.contains('o')) & (wordle.word.str.contains('t')) & (wordle.word.str.contains('n'))].reset_index()
        i = randrange(len(common) - 1)
        first_attempt = common[common.index == i].reset_index()

        word = {
        0 : first_attempt.iloc[0].w0.upper(),
        1 : first_attempt.iloc[0].w1.upper(),
        2 : first_attempt.iloc[0].w2.upper(),
        3 : first_attempt.iloc[0].w3.upper(),
        4 : first_attempt.iloc[0].w4.upper(),
        }

        driver.execute_script(letters[word[0]]).click()
        driver.execute_script(letters[word[1]]).click()
        driver.execute_script(letters[word[2]]).click()
        driver.execute_script(letters[word[3]]).click()
        driver.execute_script(letters[word[4]]).click()
        driver.execute_script(letters['ENTER']).click()

        for k in blanks_status:
            status = driver.execute_script(blanks[blanks_status[k].format(r)]).get_attribute('evaluation')
            if status == 'absent':
                absent.append(word[k].lower())
            elif status == 'present':
                present.append(word[k].lower())
            elif status == 'correct':
                correct[k] = word[k].lower()
    else:
        if len(absent) > 0:
            for l in absent:
                wordle = wordle[~wordle.word.str.contains(l)]
        if len(present) > 0:
            for l in present:
                wordle = wordle[wordle.word.str.contains(l)]

        for i in range(5):
            if correct[i] != '':
                wordle = wordle[wordle['w' + str(i)] == correct[i]] 
        try:
            del wordle['index']
            del wordle['level_0']
        except:
            pass
        try:
            wordle = wordle.reset_index()
        except:
            pass

        find_word = True
        while find_word == True:
            attempt = random_selection(wordle)
            if attempt.word[0] not in incorrect:
                find_word = False
        
        incorrect.append(attempt.word[0])

        

        word = {
            0 : attempt.iloc[0].w0.upper(),
            1 : attempt.iloc[0].w1.upper(),
            2 : attempt.iloc[0].w2.upper(),
            3 : attempt.iloc[0].w3.upper(),
            4 : attempt.iloc[0].w4.upper(),
            }

        driver.execute_script(letters[word[0]]).click()
        driver.execute_script(letters[word[1]]).click()
        driver.execute_script(letters[word[2]]).click()
        driver.execute_script(letters[word[3]]).click()
        driver.execute_script(letters[word[4]]).click()
        driver.execute_script(letters['ENTER']).click()
        
        for k in blanks_status:
            status = driver.execute_script(blanks[blanks_status[k].format(r)]).get_attribute('evaluation')
            if status == 'absent':
                absent.append(word[k].lower())
            elif status == 'present':
                present.append(word[k].lower())
            elif status == 'correct':
                correct[k] = word[k].lower()
        
    for a  in absent:
        if a in present or a in correct:
            absent.remove(a)
            
    return wordle,absent, present,correct, incorrect
                        

            
                    
try:
    wordle,absent, present,correct, incorrect = check_attempt(0, wordle,absent, present,correct, incorrect)
    time.sleep(2)
    wordle,absent, present,correct, incorrect = check_attempt(1, wordle,absent, present,correct, incorrect)
    time.sleep(2)
    wordle,absent, present,correct, incorrect = check_attempt(2, wordle,absent, present,correct, incorrect)
    time.sleep(2)
    wordle,absent, present,correct, incorrect = check_attempt(3, wordle,absent, present,correct, incorrect)
    time.sleep(2)
    wordle,absent, present,correct, incorrect = check_attempt(4, wordle,absent, present,correct, incorrect)
    time.sleep(2)
    wordle,absent, present,correct, incorrect = check_attempt(5, wordle,absent, present,correct, incorrect)
except:
    pass


