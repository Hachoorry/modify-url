#無法處裡中文！

import subprocess
import re

def copy2clip(txt):
    txt = re.sub(r'\W','-',txt).strip('-') # 所有非英文跟數字的都變成'-'
    txt = re.sub(r'-+','-',txt).lower()    # 把重複的'-'整理乾淨
    cmd='echo '+txt+'|clip'
    print(f"轉換完畢，並已貼入剪貼簿：\t{txt}\n\n==========\n")
    return subprocess.check_call(cmd, shell=True)  # 執行cmd

  
txt = input("輸入要轉換的東東：\t")
copy2clip(txt)
while True:
    txt = input("繼續輸入下一筆：\t")
    copy2clip(txt)
