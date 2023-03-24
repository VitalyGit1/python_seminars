"""
Задание 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под
номером 32 и заканчивая 127-м включительно.
"""

def print_ascii_table(start, end, count=0):
    if start > end:
        return
    print(f"{start} - {chr(start)}", end=" ")
    count += 1
    if count == 10:
        count = 0
        print()
    print_ascii_table(start+1, end, count)

print_ascii_table(32,127)
