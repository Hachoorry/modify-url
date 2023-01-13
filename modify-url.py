import subprocess
import re

def copy2clip(txt):
    txt = re.sub(r'\W','-',txt).strip('-') # 所有非英文跟數字的都變成'-'
    txt = re.sub(r'-+','-',txt).lower()    # 把重複的'-'整理乾淨
    cmd='echo '+txt+'|clip'
    print(f"轉換完畢，以貼入剪貼簿：\n\n{txt}\n\n==========")
    return subprocess.check_call(cmd, shell=True)  # 執行cmd
    
txt = input("輸入要轉換的東東")
copy2clip(txt)
