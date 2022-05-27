import re

a = ['Sehingga 8 Ogos 2021: Jumlah kes COVID-19 yang dilaporkan adalah 18,688 kes (1,262,540 kes)\n\nPecahan setiap negeri (Kumulatif):\n\nSelangor - 6,565 (465,015)\nWPKL - 1,883 (140,404)\nJohor - 1,308 (100,452)\nSabah -Lagi 1,379 (93,835)\nSarawak - 581 (81,328)\nNegeri Sembilan - 1,140 (78,777)\nKedah - 1,610 (56,598)\nPulau Pinang - 694 (52,368)\nKelantan - 870 (49,433)\nPerak - 861 (43,924)\nMelaka - 526 (35,584)\nPahang - 602 (29,125)\nTerengganu - 598 (20,696)\nWP Labuan - 2 (9,711)\nWP Putrajaya - 63 (4,478)\nPerlis - 6 (812)\n\n- KPK KKM']
b = ['Sehingga 9 Ogos 2021. Jumlah kes COVID-19 yang dilaporkan adalah 17,236 kes (1,279,776 kes).\n\nPecahan setiap negeri (Kumulatif):\n\nSelangor - 5,740 (470,755)\nWPKL - 1,567 (141,971)\nJohor - 1,232 (101,684)\nSabah -Lagi 1,247 (95,082)\nSarawak - 589 (81,917)\nNegeri Sembilan - 1,215 (79,992)\nKedah - 1,328 (57,926)\nPulau Pinang - 908 (53,276)\nKelantan - 914 (50,347)\nPerak - 935 (44,859)\nMelaka - 360 (35,944)\nPahang - 604 (29,729)\nTerengganu - 501 (21,197)\nWP Labuan - 8 (9,719)\nWP Putrajaya - 66 (4,544)\nPerlis - 22 (834)\n\n- KPK KKM']
out = []
for v in a:
    regex_list = re.findall(r"^(.*?\(.*?\)).\n|\n", v, flags=re.M)
    for g in regex_list:
        print(g)
        out.append(g.split(":")[0])
    print(*out[0])
        