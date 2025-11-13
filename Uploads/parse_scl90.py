import json

# SCL-90 sorularını tanımla
questions_text = """
1. Baş ağrısı
2. Sinirlilik ya da içinin titremesi
3. Zihinden atamadığınız tekrarlayıcı hoşa gitmeyen düşünceler
4. Baygınlık veya baş dönmesi
5. Cinsel arzu ve ilginin kaybı
6. Başkaları tarafından eleştirilme duygusu
7. Herhangi bir kimsenin düşüncelerinizi kontrol edebileceği duygusu
8. Sorunlarınızdan pek çoğu için başkalarının suçlanması gerektiği duygusu
9. Olayları anımsamada güçlük
10. Dikkatsizlik veya sakarlıkla ilgili endişeler
11. Kolayca gücenme, rahatsız olma hissi
12. Göğüs veya kalp bölgesinde ağrılar
13. Caddelerde veya açık alanlarda korku hissi
14. Enerjinizde azalma veya yavaşlama hali
15. Yaşamınızın sonlanması düşünceleri
16. Başka kişilerin duymadıkları sesleri duyma
17. Titreme
18. Çoğu kişiye güvenilmemesi gerektiği hissi
19. İştah azalması
20. Kolayca ağlama
21. Karşı cinsten kişilerle utangaçlık ve rahatsız olma hissi
22. Tuzağa düşürülmüş ya da yakalanmış olma hissi
23. Bir neden olmaksızın aniden korkuya kapılma
24. Kontrol edilemeyen öfke patlamaları
25. Evden dışarı yalnız çıkma korkusu
26. Olanlar için kendini suçlama
27. Belin alt kısmında ağrılar
28. İşlerin yapılmasında erteleme duygusu
29. Yalnızlık hissi
30. Karamsarlık hissi
31. Her şey için çok fazla endişe etme
32. Her şeye karşı ilgisizlik hali
33. Korku hissi
34. Duygularınızın kolayca incinebilmesi hali
35. Diğer insanların sizin özel düşüncelerinizi bilmesi
36. Başkalarının sizi anlamadığı ya da hissedemeyeceği duygusu
37. Başkalarının sizi sevmediği ya da dostça olmayan davranışlar gösterdiği hissi
38. İşlerin doğru yapıldığından emin olabilmek için çok yavaş yapmak
39. Kalbin çok hızlı çarpması
40. Bulantı ve midede rahatsızlık hissi
41. Kendini başkalarından aşağı görme
42. Adale (kas) ağrıları
43. Başkalarının sizi gözlediği veya hakkınızda konuştuğu hissi
44. Uykuya dalmada güçlük
45. Yaptığınız işleri bir yada birkaç kez kontrol etme
46. Karar vermede güçlük
47. Otobüs, tren, metro gibi araçlarla yolculuk etme korkusu
48. Nefes almada güçlük
49. Soğuk veya sıcak basması
50. Sizi korkutan belirli uğraş,yer ve nesnelerden kaçınma durumu
51. Hiçbir şey düşünmeme hali
52. Bedeninizin bazı kısımlarında uyuşma karıncalanma hali
53. Boğazınıza bir yumruk tıkanmış hissi
54. Gelecek konusunda ümitsizlik
55. Düşüncelerinizi bir konuya yoğunlaştırmada güçlük
56. Bedeninizin çeşitli kısımlarında zayıflık hissi
57. Gerginlik ve coşku hissi
58. Kol ve bacaklarda ağırlık hissi
59. Ölüm veya ölme düşünceleri
60. Aşırı yemek yeme
61. İnsanlar size baktığı ya da hakkınızda konuştuğu zaman rahatsızlık duyma
62. Size ait olmayan düşüncelere sahip olma
63. Bir başkasına vurmak, zarar vermek, yaralamak dürtülerinin olması
64. Sabahın erken saatlerinde uyanma
65. Yıkanma, sayma , dokunma gibi bazı hareketleri tekrarlama hali
66. Uykuda huzursuzluk, rahat uyuyamama
67. Bazı şeyleri kırıp dökme isteği
68. Başkalarının paylaşıp kabul etmediği inanç ve düşüncelerinin olması
69. Başkalarının yanında kendini çok sıkılgan hissetme
70. Çarşı, sinema gibi kalabalık yerlerde rahatsızlık hissi
71. Her şeyin bir yük gibi görünmesi
72. Dehşet ve panik nöbetleri
73. Toplum içinde yer veya içerken huzursuzluk hissi
74. Sık sık tartışmaya girme
75. Yalnız bırakıldığında sinirlilik hali
76. Başkalarının sizi başarılarınız için yeterince taktir etmediği duygusu
77. Başkalarıyla birlikte olunan durumlarda bile yalnızlık hissetme
78. Yerinizde duramayacak ölçüde rahatsızlık duyma
79. Değersizlik duygusu
80. Size kötü bir şey olacakmış duygusu
81. Bağırma yada eşyaları fırlatma
82. Topluluk içinde bayılacağınız korkusu
83. Eğer izin verirseniz insanların sizi sömüreceği duygusu
84. Cinsiyet konusunda sizi çok rahatsız eden düşüncelerin olması
85. Günahlarınızdan dolayı cezalandırılmanız gerektiği düşüncesi
86. Korkutucu türden düşünce ve hayaller
87. Bedeninizde ciddi bir rahatsızlık olduğu düşüncesi
88. Başka bir kişiye karşı asla yakınlık duymama
89. Suçluluk duygusu
90. Aklınızda bir bozukluğun olduğu düşüncesi
"""

# Soruları parse et
lines = questions_text.strip().split('\n')
questions = []
for line in lines:
    if line.strip():
        parts = line.split('.', 1)
        if len(parts) == 2:
            q_id = int(parts[0].strip())
            q_text = parts[1].strip()
            questions.append({
                "id": q_id,
                "text": q_text,
                "options": [
                    {"value": 0, "label": "Hiç"},
                    {"value": 1, "label": "Çok Az"},
                    {"value": 2, "label": "Orta Derecede"},
                    {"value": 3, "label": "Oldukça Fazla"},
                    {"value": 4, "label": "İleri Derecede Fazla"}
                ]
            })

# Alt ölçekleri tanımla
scales = {
    "SOM": {
        "name": "Somatizasyon (Somatization)",
        "description": "Kardiyovasküler, gastrointestinal, solunum sistemi ve diğer sistemlere ait bedensel yakınmaları içerir",
        "questionIds": [1, 4, 12, 27, 40, 42, 48, 49, 52, 53, 56, 58],
        "totalItems": 12
    },
    "OC": {
        "name": "Obsesif-Kompulsif (Obsessive-Compulsive)",
        "description": "Bireyin istemiyle kontrol edemediği düşünce, dürtü ve davranışları içerir",
        "questionIds": [3, 9, 10, 28, 38, 45, 46, 51, 55, 65],
        "totalItems": 10
    },
    "INT": {
        "name": "Kişilerarası Duyarlılık (Interpersonal Sensitivity)",
        "description": "Başkaları ile birlikte olduğunda hissedilen tedirginlik ve yetersizlik duyguları",
        "questionIds": [6, 21, 34, 36, 37, 41, 61, 69, 73],
        "totalItems": 9
    },
    "DEP": {
        "name": "Depresyon (Depression)",
        "description": "Çökkünlük, motivasyon ve enerji kaybı, umutsuzluk, intihar düşünceleri",
        "questionIds": [5, 14, 15, 20, 22, 26, 29, 30, 31, 32, 54, 71, 79],
        "totalItems": 13
    },
    "ANX": {
        "name": "Anksiyete (Anxiety)",
        "description": "Belirgin gerginlik, huzursuzluk, panik atakları ve korku",
        "questionIds": [2, 17, 23, 33, 39, 57, 72, 78, 80, 86],
        "totalItems": 10
    },
    "HOS": {
        "name": "Hostilite (Hostility)",
        "description": "Düşmanlık, öfke, sinirlilik ve agresif düşünceler",
        "questionIds": [11, 24, 63, 67, 74, 81],
        "totalItems": 6
    },
    "PHOB": {
        "name": "Fobik Anksiyete (Phobic Anxiety)",
        "description": "Agorafobi, sosyal fobi, belirli nesnelere karşı fobi",
        "questionIds": [13, 25, 47, 50, 70, 75, 82],
        "totalItems": 7
    },
    "PAR": {
        "name": "Paranoid Düşünce (Paranoid Ideation)",
        "description": "Kuşkuculuk, kendini referans alma, kontrol edilme düşünceleri",
        "questionIds": [8, 18, 43, 68, 76, 83],
        "totalItems": 6
    },
    "PSY": {
        "name": "Psikotizm (Psychoticism)",
        "description": "Yalnızlık, içe kapanıklık, düşünce yayılması, halüsinasyonlar",
        "questionIds": [7, 16, 35, 62, 77, 84, 85, 87, 88, 90],
        "totalItems": 10
    },
    "ADDITIONAL": {
        "name": "Ek Maddeler (Additional Items)",
        "description": "Herhangi bir alt ölçeğe dahil olmayan maddeler",
        "questionIds": [19, 44, 59, 60, 64, 66, 89],
        "totalItems": 7
    }
}

# JSON yapısını oluştur
scl90_data = {
    "testName": "Belirti Tarama Listesi (SCL-90-R)",
    "testCode": "SCL-90-R",
    "version": "Türkçe Uyarlama (Arda Tuna 2004)",
    "description": "SCL-90-R, bireylerin yaşadıkları psikolojik belirtileri ve rahatsızlık düzeylerini değerlendirmek için kullanılan 90 maddelik bir kendini değerlendirme ölçeğidir. Son bir ay içindeki yakınmaları 5'li Likert tipi ölçek üzerinde değerlendirir.",
    "totalQuestions": 90,
    "questions": questions,
    "scales": scales,
    "globalIndices": {
        "GSI": {
            "name": "Genel Şiddet İndeksi (Global Severity Index)",
            "description": "Bireyin psikolojik rahatsızlığının genel düzeyini yansıtır. Tüm maddelerin puanlarının toplamının toplam madde sayısına bölünmesiyle elde edilir.",
            "calculation": "Toplam puan / 90"
        },
        "PST": {
            "name": "Pozitif Belirti Toplamı (Positive Symptom Total)",
            "description": "Hiç cevabı dışında herhangi bir puan verilen (1-4 arası) madde sayısını gösterir.",
            "calculation": "0'dan büyük puan verilen madde sayısı"
        },
        "PSDI": {
            "name": "Pozitif Belirti Rahatsızlık İndeksi (Positive Symptom Distress Index)",
            "description": "Belirtilerin yoğunluk düzeyini değerlendirir. Pozitif belirti gösteren maddelerin ortalama puanıdır.",
            "calculation": "Toplam puan / PST"
        }
    },
    "scoring": {
        "method": "Her madde 0-4 arası puanlanır. Alt ölçek puanları, o ölçekteki maddelerin puanlarının toplamının madde sayısına bölünmesiyle elde edilir. Yüksek puanlar daha fazla psikolojik rahatsızlık gösterir.",
        "responseFormat": {
            "0": "Hiç - Belirtinin hiç yaşanmadığı",
            "1": "Çok Az - Belirtinin hafif düzeyde yaşandığı",
            "2": "Orta Derecede - Belirtinin orta düzeyde yaşandığı",
            "3": "Oldukça Fazla - Belirtinin yoğun yaşandığı",
            "4": "İleri Derecede Fazla - Belirtinin çok yoğun yaşandığı"
        },
        "interpretation": {
            "cutoffNote": "Türk örneklemi için kesme puanları belirlenmiştir. Klinik değerlendirme için profesyonel görüş gereklidir.",
            "scaleRange": "Her alt ölçek 0-4 arası ortalama puan alır",
            "clinicalSignificance": "Yüksek puanlar psikopatolojik belirtilerin varlığını gösterir"
        }
    },
    "instructions": "Aşağıda, zaman zaman herkeste olabilecek yakınma ve sorunların bir listesi vardır. Lütfen her birini dikkatlice okuyunuz. Sonra bu durumun bugün de dahil olmak üzere son bir ay içinde sizi ne ölçüde huzursuz ve tedirgin ettiğini karşısındaki ölçekte derecelendiriniz.",
    "timeFrame": "Son bir ay",
    "reference": "Derogatis, L. R. (1977). SCL-90-R: Administration, Scoring, and Procedures Manual-I. Baltimore: Clinical Psychometric Research. Türkçe uyarlama: Dağ, İ. (1991)."
}

# JSON dosyasına kaydet
with open('/home/ubuntu/scl90_test.json', 'w', encoding='utf-8') as f:
    json.dump(scl90_data, f, ensure_ascii=False, indent=2)

print("SCL-90-R testi başarıyla JSON formatına dönüştürüldü!")
print(f"Toplam soru sayısı: {len(questions)}")
print(f"Toplam alt ölçek sayısı: {len(scales)}")
print(f"Global indeks sayısı: {len(scl90_data['globalIndices'])}")
