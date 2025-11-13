import json

# Otomatik Düşünceler Ölçeği sorularını tanımla
questions_data = [
    "Tüm dünya bana karşıymış gibi geliyor",
    "Hiç bir işe yaramıyorum",
    "Neden hiç başarılı olamıyorum",
    "Beni hiç kimse anlamıyor",
    "Başkalarını düş kırıklığına uğrattığım oldu",
    "Devam edebileceğimi sanmıyorum",
    "Keşke daha iyi bir insan olsaydım",
    "Öyle güçsüzüm ki ...",
    "Hayatım istediğim gibi gitmiyor",
    "Kendimi düş kırıklığına uğrattım",
    "Artık hiçbir şeyin tadı kalmadı",
    "Artık dayanamayacağım",
    "Bir türlü harekete geçemiyorum",
    "Neyim var benim",
    "Keşke başka bir yerde olsaydım",
    "Hiçbir şeyin iki ucunu bir araya getiremiyorum",
    "Kendimden nefret ediyorum",
    "Değersiz bir insanım",
    "Keşke birden yok olabilseydim",
    "Ne zorum var benim",
    "Hayatta hep kaybetmeye mahkûmum",
    "Hayatım karmakarışık",
    "Başarısızım",
    "Hiç bir zaman başaramayacağım",
    "Kendimi çok çaresiz hissediyorum",
    "Bir şeylerin değişmesi gerek",
    "Bende mutlaka bir bozukluk olmalı",
    "Geleceğim kasvetli",
    "Hiç bir şey için uğraşmaya değmez",
    "Hiçbir şeyi bitiremiyorum"
]

# Soruları yapılandır
questions = []
for idx, q_text in enumerate(questions_data, 1):
    questions.append({
        "id": idx,
        "text": q_text,
        "options": [
            {"value": 1, "label": "Hiç aklımdan geçmedi"},
            {"value": 2, "label": "Ender olarak aklımdan geçti"},
            {"value": 3, "label": "Arada sırada aklımdan geçti"},
            {"value": 4, "label": "Sık sık aklımdan geçti"},
            {"value": 5, "label": "Hep aklımdan geçti"}
        ]
    })

# Alt ölçekleri tanımla (literatüre göre)
scales = {
    "KISISEL_UYUMSUZLUK_CARESIZLIK": {
        "name": "Kişisel Uyumsuzluk ve Çaresizlik",
        "description": "Bireyin kendini değersiz, yetersiz ve çaresiz hissetmesini yansıtan düşünceler",
        "questionIds": [2, 3, 6, 7, 8, 10, 13, 14, 17, 18, 23, 24, 25, 27, 30],
        "totalItems": 15
    },
    "OLUMLU_BEKLENTI_AZALMASI": {
        "name": "Olumsuz Benlik Algısı ve Olumsuz Beklentiler",
        "description": "Gelecekle ilgili olumsuz beklentiler ve benlik algısındaki negatiflik",
        "questionIds": [9, 11, 12, 15, 19, 20, 21, 22, 26, 28, 29],
        "totalItems": 11
    },
    "DUZENLEME_GUCLUGU": {
        "name": "Düzenleme ve Yönelim Güçlüğü",
        "description": "Yaşamı düzenleme ve hedef belirleme konusundaki güçlükler",
        "questionIds": [1, 4, 5, 16],
        "totalItems": 4
    }
}

# JSON yapısını oluştur
otomatik_dusunceler_data = {
    "testName": "Otomatik Düşünceler Ölçeği",
    "testCode": "ODO",
    "version": "Türkçe Uyarlama",
    "description": "Otomatik Düşünceler Ölçeği, bireylerin depresyonla ilişkili negatif otomatik düşüncelerinin sıklığını değerlendirmek için kullanılan 30 maddelik bir öz-bildirim ölçeğidir. Bilişsel Terapi yaklaşımına dayalı olarak geliştirilmiştir.",
    "totalQuestions": 30,
    "questions": questions,
    "scales": scales,
    "scoring": {
        "method": "Her madde 1-5 arası puanlanır. Toplam puan, tüm maddelerin puanlarının toplamıdır. Yüksek puanlar, olumsuz otomatik düşüncelerin daha sık yaşandığını gösterir.",
        "totalScoreRange": {
            "minimum": 30,
            "maximum": 150
        },
        "responseFormat": {
            "1": "Hiç aklımdan geçmedi - Düşüncenin hiç yaşanmadığı",
            "2": "Ender olarak aklımdan geçti - Düşüncenin nadiren yaşandığı",
            "3": "Arada sırada aklımdan geçti - Düşüncenin bazen yaşandığı",
            "4": "Sık sık aklımdan geçti - Düşüncenin sıklıkla yaşandığı",
            "5": "Hep aklımdan geçti - Düşüncenin sürekli yaşandığı"
        },
        "interpretation": {
            "highScore": "Yüksek puanlar depresif düşünce örüntülerinin varlığını ve şiddetini gösterir",
            "lowScore": "Düşük puanlar olumsuz otomatik düşüncelerin az yaşandığını gösterir",
            "clinicalNote": "Klinik değerlendirme için profesyonel görüş gereklidir"
        },
        "cutoffScores": {
            "note": "Kesme puanları araştırmalara göre değişkenlik gösterebilir",
            "suggestion": "Yüksek puanlar (örn. >70) klinik düzeyde depresif düşünceler olabileceğini gösterir"
        }
    },
    "instructions": "Aşağıda kişilerin zaman zaman aklına gelen bazı düşünceler sıralanmıştır. Lütfen her birini okuyarak, bu düşüncelerin SON BİR HAFTA içinde aklınızdan ne kadar sıklıkla geçtiğini işaretleyiniz. Lütfen her bir maddeyi dikkatle okuyunuz ve maddelerin yanındaki uygun sayıyı işaretleyiniz.",
    "timeFrame": "Son bir hafta",
    "theoreticalBackground": "Bilişsel Terapi - Aaron T. Beck'in bilişsel modeline dayalı olarak geliştirilmiştir. Otomatik düşünceler, bireyin farkında olmadan zihninden geçen, hızlı ve istem dışı düşüncelerdir.",
    "reference": "Hollon, S. D., & Kendall, P. C. (1980). Cognitive self-statements in depression: Development of an Automatic Thoughts Questionnaire. Cognitive Therapy and Research, 4(4), 383-395. Türkçe uyarlama: Şahin, N. H., & Şahin, N. (1992).",
    "website": "www.bilisseldavranisci.org"
}

# JSON dosyasına kaydet
with open('/home/ubuntu/otomatik_dusunceler_test.json', 'w', encoding='utf-8') as f:
    json.dump(otomatik_dusunceler_data, f, ensure_ascii=False, indent=2)

print("Otomatik Düşünceler Ölçeği başarıyla JSON formatına dönüştürüldü!")
print(f"Toplam soru sayısı: {len(questions)}")
print(f"Toplam alt ölçek sayısı: {len(scales)}")
print(f"Puan aralığı: {otomatik_dusunceler_data['scoring']['totalScoreRange']['minimum']} - {otomatik_dusunceler_data['scoring']['totalScoreRange']['maximum']}")
