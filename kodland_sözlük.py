meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ADDS": "(additional enemies) ekstra düşman anlamına gelir ve boss savaşlarında ortaya çıkan düşmanları ifade eder",
            "AFK": "oyun oynayan kişinin bilgisayar başında olmadığı anlamına gelir.",
            "DPS": "saniye başı hasar anlamına gelir",
            "FOV": "Oyunlardaki görüş açısını ifade eden (field of view)"
            }
kelime = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if kelime in meme_sozlugu.keys():
    print("kelime sözlükte var")
else:
    print("kelime sözlükte yok")
