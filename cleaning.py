import re
log = """
 ██████╗██╗     ███████╗ █████╗ ███╗   ██╗██████╗ 
██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║██╔══██╗
██║     ██║     █████╗  ███████║██╔██╗ ██║██║  ██║
██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║██║  ██║
╚██████╗███████╗███████╗██║  ██║██║ ╚████║██████╔╝
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 
"""
print(log)

path = input("파일의 경로를 적어 주세요 : ").strip()
try:
    with open(path, 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"오류: '{path}' 파일을 찾을 수 없습니다.")
    exit(1)
except Exception as e:
    print(f"파일을 읽는 중 오류가 발생했습니다: {e}")
    exit(1)

hex_values = []
for line in lines:
    pattern = r'([0-9A-Fa-f]{1,2})h'
    matches = re.findall(pattern, line)
    if '.data:' in line and 'db' in line:
        db_part = line.split('db')[-1]
        matches = re.findall(pattern, db_part)
    elif not '.data:' in line:
        matches = re.findall(pattern, line)
    hex_values.extend(matches)

for i in range(0, len(hex_values), 11):
    chunk = hex_values[i:i+11]
    formatted_values = [f"0x{val}" for val in chunk]
    if i + 11 >= len(hex_values):
        print(", ".join(formatted_values))
    else:
        print(", ".join(formatted_values) + ",")