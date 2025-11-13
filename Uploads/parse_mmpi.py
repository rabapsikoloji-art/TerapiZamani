import json
import re

# MMPI sorularını parse et
questions_text = """
1	 Teknik yazılardan hoşlanırım
2	 İştahım iyidir
3	 Çok defa sabahları dinç ve dinlenmiş olarak uyanırım
4	 Kütüphaneci olarak çalışmayı seveceğimi sanıyorum
5	 Gürültüden kolayca uyanırım
6	 Cinayet haberlerini okumaktan hoşlanırım
7	 Çoğu zaman el ve ayaklarımın sıcaklığı iyidir
8	 Günlük hayatım beni ilgilendirecek şeylerle doludur
9	 Bugün de hemen hemen eskisi kadar iyi çalışabiliyorum
10	 Çoğu zaman boğazım tıkanır gibi olur
11	 İnsan rüyalarını anlamaya çalışmalı ve kendini onlara göre ayarlamalıdır
12	 Polis romanlarından ya da esrarengiz yazılardan hoşlanırım
13	 Büyük bir sinir gerginliği içinde çalışırım
14	 Ayda iki defa ishal olurum
15	 Ara sıra söylenemeyecek kadar ayıp şeyler düşünürüm
16	 hayatta kötülükler hep beni bulur
17	 Babam iyi bir adamdır
18	 Pek seyrek kabız olurum
19	 Yeni bir işe girince kimin gözüne girmek gerektiğini öğrenmek isterim
20	 Cinsel yaşamımdan memnunum
21	 Zaman zaman evi bırakıp gitmek istemişimdir
22	 Ara sıra kontrol edemediğim gülme ve ağlama nöbetlerine tutulurum
23	 Mide bulantısı ve kusmadan sıkıntı çekerim
24	 Kimse beni anlamıyor
25	 Şarkıcı olmayı isterim
26	 Başım derde girince susmayı tercih ederim
27	 Bazen kötü ruhların beni etkileri altına aldığını hissederim
28	 Kötülüğe kötülükle karşılık vermek benim prensibimdir
29	 haftada çok defa midem ekşir
30	 Bazen canım küfretmek ister
31	 Sık sık geceleri kabus geçiririm
32	 Zihnimi bir iş üzerinde toplamada güçlük çekerim
33	 Başımdan çok garip ve tuhaf şeyler geçti
34	 Çoğu zaman öksürüğüm vardır
35	 Başkaları engel olmasaydı daha çok başarılı olurdum
36	 Sağlığım beni pek kaygılandırmaz
37	 Cinsel yaşamım yüzünden başım hiç derde girmedi
38	 Gençliğimde bir devre ufak tefek şeyler çaldım
39	 Bazen içimden bir şeyler kırmak isteği geçer
40	 Başka bir şey yapmaktansa çoğu zaman oturup hayal kurmayı severim
41	 Kendimi toparlayamadığım için günler, haftalar hatta aylarca hiçbir şeye el sürmediğim oldu
42	 Ailem seçtiğim (veya seçmek istediğim) mesleği beğenmiyor
43	 Kuşkulu ve rahatsız uyurum
44	 Çoğu zaman başımın her tarafı ağrır
45	 her zaman doğruyu söylemem
46	 Şimdi her zamankinden daha iyi düşünüp tartabiliyorum
47	 Ortada hiç bir neden yokken haftada bir yada sık sık birden bire her yanımı ateş basar
48	 Başkaları ile bir arada iken kulağıma çok garip şeyler gelmesinden rahatsız olurum
49	 Kanunların hemen hepsi kaldırılsa daha iyi olur
50	 Bazen ruhum vücudumdan ayrılır
51	 Sağlığım bir çok arkadaşımınki kadar iyidir
52	 Uzun zamandan beri görmediğim okul arkadaşlarım ya da tanıdıklarım,önce benimle konuşmazlarsa onları görmezden gelmeyi tercih ederim
53	 hocaların dua okuyup üflemesi hastalığı iyileştirir
54	 Tanıdıklarımın çoğu beni sever
55	 Kalp ve göğüs ağrılarından hemen hemen hiç şikayetim yoktur
56	 Çocukken okuldan kaçtığım için bir iki defa cezalandırıldım
57	 İnsanlarla çabuk kaynaşırım
58	 Kuran'ın buyurdukları bir bir çıkmaktadır
59	 Çok defa benden az bilenlerle çalışmak zorunda kaldım
60	 her gün gazetelerin baş yazılarını okumam
61	 Gerektiği gibi bir hayat yaşayamadım
62	 Vücudumun bazı yerlerinde çok defa yanma,gıdıklanma,karıncalanma veya uyuşukluk hissederim
63	 Büyük abdest yapmada yada tutmada hiçbir güçlük çekmem
64	 Bazen başkalarının sabrını tüketecek kadar bir şeye saplanır kalırım
65	 Babamı severim
66	 Etrafımda başkalarının görmedikleri eşya,hayvanlar veya insanlar görürüm
67	 Başkalarının mutlu göründüğü kadar mutlu olmayı isterdim
68	 Ensemde nadiren ağrı hissederim
69	 Kendi cinsimden olanları oldukça çekici bulurum
70	 Körebe oyunundan hoşlanırım
71	 Birçok kimseler başkalarının ilgi ve yardımını sağlamak için talihsizliklerini abartırlar
72	 hemen hemen her gün mide ağrılarından rahatsız olurum
73	 Ben önemli bir kimseyim
74	 Çoğu zaman kız olmayı isterdim
75	 Ara sıra öfkelenirim
76	 Çoğu zaman kendimi hüzünlü hissederim
77	 Aşk romanları okumaktan hoşlanırım
78	 Şiiri severim
79	 Kolay incinmem
80	 Bazen hayvanlara rahat vermem
81	 Orman bekçiliği gibi işlerden hoşlanacağımı zannediyorum
82	 Tartışmalarda çabucak yenilirim
83	 Çok çalışabilen ya da çalışmak isteyen kişinin başarılı olma şansı yüksektir
84	 Bugünlerde artık hiç ilerleme umudum kalmamış gibi hissediyorum
85	 Kullanamayacak bile olsam bazen başkalarının ayakkabı, eldiven gibi özel eşyaları o kadar hoşuma gider ki dokunmak ve aşırmak isterim
86	 Kendime hiç güvenim yoktur
87	 Çiçek satıcısı olmayı isterdim
88	 Genel olarak hayatın yaşamaya değer olduğu kanısındayım
89	 İnsanlara gerçeği kabul ettirmek güçtür
90	 Bugün yapmam gereken işleri ara sıra yarına bıraktığım olur
91	 Benimle alay edilmesine aldırmam
92	 hemşire olmayı isterdim
93	 Yükselmek için birçok kimse yalan söylemekten çekinmez
94	 Sonradan pişman olacağım pek çok şeyi yaptığım olur
95	 Namazımı hemen hemen muntazaman kılarım
96	 Ailemle pek az kavga ederim
97	 Bazen zararlı ya da çok kötü işler yapmak için içimde çok güçlü bir istek duyarım
98	 Kıyamet gününe inanıyorum
99	 Gürültülü eğlencelere katılmaktan hoşlanıyorum
100	 Bildiğim bir konuda bir kimse saçma sapan ya da cahilce konuşursa onu hemen düzeltirim
101	 Bence cinsel yönden kadınlar da erkekler kadar serbest olmalıdır
102	 En büyük mücadelemi kendimle yaparım
103	 Vücudumda pek az seğrilme ve kasılma olur
104	 Başıma ne gelirse gelsin aldırmıyorum
105	 Keyfim yerinde olmadığı zaman tersliğim üzerimdedir
106	 Çoğu zaman büyük bir hata ya da kötülük yaptığım duygusuna kapılırım
107	 Çoğu zaman mutluyumdur
108	 Çoğu zaman bana, kafam şişmiş ya da burnum tıkanmış gibi gelir
109	 Bazı kimseler o kadar amirane davranırlar ki, haklı bile olsalar, içimden dediklerinin aksini yapmak gelir
110	 Bana kötülük etmek isteyen biri var
111	 Sırf heyecanlanmak için tehlikeli bir işe girişmedim
112	 Doğru bildiğim şeyler için çoğu zaman direnmek zorunda kalırım
113	 Kanunların uygulanması gerektiğine inanırım
114	 Çoğu zaman başımı sıkı bir çember içindeymiş gibi hissederim
115	 Ahrete inanırım
116	 Bahse girdiğim yarış veya oyunlardan daha çok zevk alırım
117	 Bir çok kimseler bana yakalanmaktan korktukları için dürüsttürler
118	 Dersten kaçtığım için ara sıra müdüre gönderildiğim oldu
119	 Konuşma tarzım her zamanki gibidir
120	 Evde sofra adabına dışarıdaki kadar dikkat etmem
121	 Aleyhimde bazı tertipler kurulduğuna inanıyorum
122	 Tanıdığım insanların çoğu kadar becerikli ve zeki olduğumu sanıyorum
123	 Beni takip edenler olduğuna inanıyorum
124	 Birçokları kaybetmektense çıkarlarını korumak için pek doğru olmayan yollara başvururlar
125	 Midemden oldukça rahatsızım
126	 Tiyatrodan hoşlanırım
127	 Dertlerimin çoğundan kimin sorumlu olduğunu biliyorum
128	 Kan görünce korkmam ya da fenalaşmam
129	 Bazen ters ve suratsız olurum
130	 hiçbir zaman kan kusmadım ya da kan tükürmedim
131	 hastalığa yakalanacağım diye kaygılanmam
132	 Çiçek koleksiyonu yapmayı ve evde çiçek yetiştirmeyi severim
133	 hiçbir zaman normal olmayan cinsel ilişkilere girişmedim
134	 Bazen kafamdaki düşünceler o kadar hızlıdır ki söylemeyi yetiştiremem
135	 Fark edilmeyeceğimden emin olsam sinemaya biletsiz girerdim
136	 Bana iyilik yapan kimselerin genel olarak gizli bir amacı olabileceğini düşünürüm
137	 Aile hayatımın, tanıdığım kimselerin çoğunun ki kadar iyi olduğuna inanıyorum
138	 Eleştiri beni çok kırar
139	 Bazen sanki kendimi ya da başkasını incitmek zorundaymışım gibi hissederim
140	 Yemek pişirmeyi severim
141	 Davranışlarımı çoğu zaman etrafımdakilere göre ayarlarım
142	 Bazen hiçbir işe yaramadığımı düşünürüm
143	 Çocukken başlarına ne gelirse gelsin aralarındaki birliği koruyan bir gruptaydım
144	 Asker olmak isterdim
145	 Bazen biriyle yumruk yumruğa kavgaya girişmeyi istediğim olur
146	 Seyahat edip, gezip, tozmadıkça mutlu olamam
147	 Çabuk karar vermediğim için çok fırsat kaçırdım
148	 Önemli bir iş üzerinde çalışırken başkalarının işimi yarıda kesmeleri sabrımı taşırır
149	 hatıra defteri tutardım
150	 Oyunda kaybetmektense kazanmayı tercih ederim
151	 Biri beni zehirlemeye çalışıyor
152	 Çoğu geceler zihnimi hiçbir şey kurcalamadan uykuya dalarım
153	 Son bir kaç yıl içinde sağlığım çoğu zaman iyi idi
154	 hiç sinir nöbeti ya da havale geçirmedim
155	 Ne şişmanlıyorum ne de zayıflıyorum
156	 Bir şeyler yapıp sonra ne yaptığımı hatırlayamadığım zamanlar oldu
157	 Çoğu kez sebepsiz yere cezalandırıldım
158	 Çabuk ağlarım
159	 Okuduğumu eskisi kadar iyi anlayamıyorum
160	 hayatımda hiçbir zaman kendimi şimdiki kadar iyi hissetmedim
161	 Bazen başımda bir sızı hissederim
162	 Birisinin bana kurnazca bir oyun etmesine çok içerlerim
163	 Çabucak yorulmam
164	 Üzerinde çalıştığım konularda okumayı ve incelemelerde bulunmayı severim
165	 Önemli kimseleri tanımayı severim, Çünkü böylece kendimi de önemli bir kimse gibi görürüm
166	 Yüksek bir yerden aşağıya bakmaya korkarım
167	 Ailemden herhangi birinin mahkemelik olması beni rahatsız etmez
168	 Zihnimde bir gariplik var
169	 Parayı ellemeye korkmam
170	 Başkalarının hakkımda ne düşündükleri beni rahatsız etmez
171	 Bir eğlencede başkaları yapsalar bile, ben taşkınlık yapmaktan rahatsız olurum
172	 Çok kez utangaçlığımı örtbas etmek ihtiyacını duyarım
173	 Okulu severdim
174	 hiç bayılma nöbeti geçirmedim
175	 Pek az başım döner ya da hiç dönmez
176	 Yılandan büyük bir korkum yoktur
177	 Annem iyi bir kadındır
178	 hafızam genellikle iyidir
179	 Cinsel konularda sıkıntım vardır
180	 Yeni tanıştığım kimselerle konuşma konusu bulmada güçlük çekerim
181	 Canım sıkılınca heyecan yaratmayı severim
182	 Aklımı oynatmaktan korkuyorum
183	 Dilencilere para vermeyi doğru bulmam
184	 Sık sık nereden geldiğini bilmediğim sesler duyarım
185	 herkes kadar iyi işitirim
186	 Bir şeyler yapmaya girişince ellerimin çok defa titrediğini fark ederim
187	 Ellerimde beceriksizlik ya da sakarlık başlamadı
188	 Gözlerim yorulmadan uzun süre okuyabilirim
189	 Çoğu zaman bütün vücudumda bir halsizlik duyarım
190	 Başım pek az ağrır
191	 Bazen utanınca çok ağlarım
192	 Yürürken dengemi hemen hemen hiç kaybetmem
193	 Saman nezlesi ya da astım nöbetlerim yoktur
194	 hareketlerimi ve konuşmamı kontrol edemediğim fakat etrafımda olup bitenden haberdar olduğum nöbetler geçirdiğim oldu
195	 Tanıdığım herkesi sevmem
196	 hiç görmediğim yerlere gitmekten hoşlanırım
197	 Biri beni soymaya (her şeyimi almaya) çalışıyor
198	 Çok az hayal kurarım
199	 Çocuklara cinsiyetle ilgili temel gerçekler öğretilmelidir
200	 Fikir ve düşüncelerimi çalmak isteyen biri var
201	 Keşke bu kadar utangaç olmasam
202	 Kendimi cezayı hak etmiş suçlu bir insan olarak görüyorum
203	 Gazeteci olmak isterdim
204	 Gazeteci olsaydım daha çok tiyatro haberleri yazmaktan hoşlanırdım
205	 Bazen çalmaktan ya da dükkanlardan eşya aşırmaktan kendimi alamam
206	 Birçok kimselerden daha çok dindarımdır
207	 Çeşitli oyun ve eğlencelerden hoşlanırım
208	 Flört etmeyi severim
209	 Günahlarımın affedilmeyeceğine inanıyorum
210	 her şeyin tadı aynı geliyor
211	 Gündüzleri uyuyabilirim ancak geceleri uyuyamam
212	 Evdekiler bana çocuk muamelesi yapıyor
213	 Yürürken kaldırımdaki yarıklara basmamaya dikkat ederim
214	 Cildimde üzülmeye değer kabarıklık ya da sivilce yok
215	 Çok içki kullandım
216	 Başka ailelere göre bizim evde sevgi ve arkadaşlık pek azdır
217	 Sık sık kendime bir şeyler dert edinirim
218	 hayvanların eziyet çektiğini görmek beni üzmez
219	 İnşaat müteahhitliğinden hoşlanacağımı sanıyorum
220	 Annemi çok severim
221	 Bilimden hoşlanırım
222	 Karşılığını veremeyeceğim durumlarda bile arkadaşlarımdan yardım istemekte güçlük çekmem
223	 Avlanmayı çok severim
224	 Annem-babam, hep beraber olduğum kimselerden çok defa hoşlanmıyorlar
225	 Bazen biraz dedikodu yaptığım olur
226	 Ailemdeki bazı kişilerde canımı çok sıkan alışkanlıklar var
227	 Uykuda gezdiğimi söylerler
228	 Bazen alışılmamış bir kolaylıkla karar verebileceğimi hissediyorum
229	 Çeşitli kulüp ve derneklere üye olmayı isterim
230	 Kalbimin hızlı çarptığını hemen hemen hiç hissetmem ve çok seyrek nefesim tıkanır
231	 Cinsiyet hakkında konuşmayı severim
232	 Bazen üzerime çok fazla iş alırım
233	 Pek çok insan karşı çıksa da kendi fikrimi sonuna kadar savunurum
234	 Çabuk kızar ve çabuk unuturum
235	 Aile kurallarından oldukça bağımsız ve özgürüm
236	 Sıklıkla kara kara düşünürüm
237	 Akrabalarımın hemen hepsi bana karşı anlayış gösterir
238	 Zaman zaman yerinde duramayacak kadar huzursuzluk duyduğum devreler olur
239	 Aşkta hayal kırıklığına uğradım
240	 Görünüşüme hiç aldırmam
241	 Kendi içimde tutup başkalarına söylenemeyen şeyler hakkında sık sık rüya görürüm
242	 Birçoklarından daha sinirli sayılmam
243	 hemen hiç ağrı ve sızım yok
244	 Davranışlarım başkalarınca yanlış anlaşılmaya elverişlidir
245	 Ailem beni olduğundan daha hatalı bulur
246	 Boynumda sık sık kırmızı lekeler olur
247	 Kimseden sevgi görmüyorum
248	 Bazen ortada hiç bir neden yokken hatta işler kötüye gittiği zaman bile kendimi fazlası ile mutlu hissederim 
249	 Öbür dünyada şeytan ve cehennem olduğuna inanırım
250	 hayatta önüne her geleni kapmaya çalışan insanları suçlamam
251	 Kendimi kaybedip yaptığım işi aksattığım ve etrafımda olup bitenlerin farkında olmadığım zamanlar oldu
252	 hiç kimse başkasının derdine aldırış etmiyor
253	 hatalı davranışlarını görsem bile insanlara arkadaşça davranabilirim
254	 Birbiriyle şakalaşan kimseler arasında olmayı severim
255	 Seçimlerde bazen oyumu pek az tanıdığım kimselere veririm
256	 Gazetelerin ilgi çeken tek yeri resimli mizah sayfasıdır
257	 Yaptığım işlerde genel olarak başarı elde edeceğime inanırım
258	 Allah'ın varlığına inanırım
259	 İşe başlamada güçlük çekerim
260	 Okulda iken ağır öğrenenlerden biriydim
261	 Ressam olsaydım çiçek resimleri yapardım
262	 Daha güzel olmamam beni rahatsız etmez
263	 Soğuk günlerde bile kolayca terlerim
264	 Kendime tam anlamıyla güvenim vardır
265	 hiç kimseye güvenmemek en iyisidir
266	 haftada bir ya da daha sık, çok heyecanlanırım
267	 Topluluk içinde olduğumda üzerinde konuşacak uygun konular bulmada güçlük çekerim
268	 Karamsar olduğum zaman heyecanlı bir olay hemen beni bu durumdan çıkarır
269	 Bazen zevk için başkalarını kendimden korkuturum
270	 Evden çıkarken kapının kilitli ve pencerenin kapalı olup olmadığı aklıma takılmaz
271	 Başkalarının saflığını kendi çıkarına kullanan kimseleri ayıplamam
272	 Bazen kendimi enerji dolu hissederim
273	 Derimin bazı yerlerinde uyuşukluk hissederim
274	 Görme gücüm eskisi kadar kuvvetlidir
275	 Birisi zihnimi kontrol ediyor
276	 Çocukları severim
277	 Bazen bir madrabazın kurnazlığı beni o kadar eğlendirir ki yakayı ele vermemesini dilerim
278	 Çok defa tanımadığım kimselerin bana eleştirici bir gözle baktıklarını hissederim
279	 her gün gereğinden fazla su içerim
280	 Bir çok kimseler kendilerine yararı dokunacağı için arkadaş edinirler
281	 Kulaklarım pek az çınlar ya da uğuldar
282	 Genellikle sevdiğim aile üyelerine karşı bazen nefret duyarım
283	 Gazete muhabiri olsaydım en çok spor haberleri yazmayı isterdim
284	 hakkımda çok konuşulduğundan eminim
285	 Ara sıra, açık saçık bir fıkraya güldüğüm olur
286	 En çok yalnız olduğum zaman mutlu olurum
287	 Arkadaşlarıma kıyasla beni korkutan şeyler çok azdır
288	 Mide bulantısı ve kusma nöbetlerine tutulurum
289	Bir suçlu avukatının becerikliliği sayesinde cezadan kurtulunca kanunlara karşı daima nefret duyarım
290	 Çok gergin bir hava içinde çalışıyorum
291	 hayatımda bir ya da bir kaç kere birisinin beni hipnotize ederek bana bir şeyler yaptığını hissettim
292	 Başkaları benimle konuşuncaya kadar ben onlarla konuşmaya başlamam
293	 Birisi zihnimi etkilemeye çalışıyor
294	 Masal okumayı severim
295	 hiçbir neden yokken kendimi son derece neşeli hissettiğim zamanlar olur
296	 Kanunla hiç başım derde girmedi
297	 Cinsiyetle ilgili düşünceler beni rahatsız eder
298	 Birkaç kişinin birlikte başları derde girince en iyisi yakalarını kurtarmak için aynı hikayeyi uydurmak ve bundan caymamaktır
299	 Duygularımın bir çok kimselerden yoğun olduğunu düşünürüm
300	 hayatımda hiçbir zaman bebek oynamaktan hoşlanmadım
301	 Çoğu zaman hayat benim için bir yüktür
302	 Cinsel davranışlarımdan dolayı hiçbir zaman başım derde girmedi
303	 Bazı konularda o kadar alınganım ki onlar hakkında konuşamam bile
304	 Okulda sınıf karşısında konuşmak bana çok güç gelirdi
305	 Başkaları ile beraber olduğum zaman bile kendimi yalnız hissederim
306	 Bana karşı mümkün olan anlayış gösteriliyor
307	 İyi beceremediğim oyunları oynamaya yanaşmam
308	 Zaman zaman evi bırakıp gitmek istemişimdir
309	 Birçokları kadar çabuk arkadaş edinebildiğimi sanıyorum
310	 Cinsel hayatım doyurucudur
311	 Gençlik yıllarımda bir devre ufak tefek şeyler çaldım
312	 İnsanların arasında olmaktan hiç hoşlanmam
313	 Değerli eşyasını tedbirsizce ortada bırakıp çalınmasına neden olan kimse bunu çalan kadar hatalıdır
314	 Ara sıra söylenemeyecek kadar kötü şeyler düşünürüm
315	 hayatın hep kötü tarafları bana nasip olmuştur
316	 hemen herkesin, başını derde sokmamak için yalan söyleyebileceğine inanırım
317	 Birçok kimselerden daha hassasım
318	 Günlük hayatım beni ilgilendiren şeylerle dolu
319	 Birçok insanlar başkalarına yardım için zahmet çekmekten hoşlanmazlar
320	 Rüyalarımın çoğu cinsel konularla ilgilidir
321	 Kolaylıkla mahcup olurum
322	 Para ve işi kendime dert ederim
323	 Başımdan çok tuhaf ve acayip yaşantılar geçmiştir
324	 hiç kimseye aşık olmadım
325	 Ailemin yaptığı bazı şeyler beni korkutmuştur
326	 Bazen kontrol edemediğim gülme ve ağlama nöbetlerine tutulurum
327	 Annem ya da babam çok defa beni makul bulmadığım emirlere bile itaat ettirdiler
328	 Zihnimi bir konu ya da iş üzerinde toplamakta güçlük çekerim
329	 hemen hiç rüya görmem
330	 hiç felç geçirmedim ya da kaslarımda olağanüstü bir halsizlik duymadım
331	 Eğer insanlar sırf düşmanlık olsun diye beni engellemeseler daha başarılı olurdum
332	 Bazen nezle olmadığım halde sesim çıkmaz ya da değişir
333	 Beni hiç kimse anlamıyor
334	 Bazen tuhaf kokular duyarım
335	 Zihnimi bir konu üzerinde toplayamam
336	 İnsanlara karşı sabrım çabuk tükenir
337	 Çoğunlukla bir takım şeyler, kimseler için meraklanıp huzursuzlaşırım
338	 hayatımın çoğu, kimselerininkinden daha fazla tasa ve kaygı içinde geçtiğinden eminim
339	 Çoğu zaman ölmüş olmayı isterdim
340	 Bazen o kadar heyecanlanırım ki uykuya dalmam güçleşir
341	 Bazen beni rahatsız edecek kadar iyi işitirim
342	 Bana söylenenleri hemen unuturum
343	 Önemsiz ufak şeylerde bile karar verip işe girişmeden önce durur ve düşünürüm
344	 Gördüğüm bir kimseyle karşılaşmamak için sıklıkla yolumu değiştiririm
345	 Sıklıkla olup bitenler bana gerçek değilmiş gibi gelir
346	 Reklamlardaki ampuller gibi önemsiz şeyleri sayma alışkanlığım vardır
347	 Bana gerçekten kötülük yapmak isteyen hiç bir düşmanım yoktur
348	 Bana umduğumdan fazla dostluk gösteren insanlara karşı tetikte bulunmaya çalışırım
349	 Acayip ve tuhaf düşüncelerim vardır
350	 Yalnızken garip sesler duyarım
351	 Küçük bir seyahat için bile evden ayrılırken telaşlanır ve kaygılanırım
352	 Beni incitmeyeceğini bildiğim şeylerden ya da insanlardan bile korktuğum oldu
353	 Başkalarının daha önce toplanıp konuştuğu bir odaya girmekten çekinmem
354	 Bıçak gibi çok keskin ve sivri şeyler kullanmaktan korkarım
355	 Sevdiğim kimseleri bazen incitmekten hoşlanırım
356	 Dikkatimi bir konu üzerinde toplamada birçoklarından fazla güçlük çekerim
357	 Yeteneğimi küçümsediğim için birçok defalar başladığım işi yarıda bıraktım
358	 Kötü ve çok korkunç kelimeler zihnimi kurcalar ve bunlardan kendimi kurtaramam
359	 Bazen önemsiz düşünceler aklımdan geçer ve beni günlerce rahatsız eder
360	 hemen her gün beni korkutan bir şey olur
361	 her şeyi kötüye yorma eğilimindeyim
362	 Birçok kimselerden çok daha hassasım
363	 Bazen sevdiğim kimselerin beni incitmesinden hoşlandığım oldu
364	 hakkımda onur kırıcı ve kötü sözler söylüyorlar
365	 Kapalı yerlerde huzursuzluk duyarım
366	 İnsanlar arasında bile olsam çok defa kendimi yalnız hissederim
367	 Yangından korkmam
368	 Sonradan pişman olacağım şeyler yapmak ya da söylemek korkusuyla bazen bir kimseden uzak durduğum olur
369	 Çalışırken acele etmek zorunda olmaktan nefret ederim
370	 Kararsızlığım yüzünden yapılması gerekli bir çok işi yapamamışımdır
371	 Aşırı derecede kendini dinleyen bir insan değilim
372	 Elimdeki işi en iyi şekilde yapmayı isterdim
373	 Yalnızca bir tek doğru din olduğundan eminim
374	 Ara sıra zihnim her zamankinden daha ağır işler
375	 Çok mutlu olduğum ve iyi çalıştığım zamanlarda neşesiz veya dertli bir insanla karşılaşmak keyfimi tamamen kaçırır
376	 Polisler genellikle dürüsttür
377	 Toplantılarda karışmaktan çok yalnız başıma oturur ya da bir tek kişiyle ahbaplık ederim
378	 Kadınları sigara içerken görmekten hoşlanmam
379	 Çok nadiren karamsarlığa kapılırım
380	 Ne yapsam zevk alamıyorum
381	 Kolay öfkelenen biri olduğumu söylerler
382	 Yapmak istediğim şeylere karar verirken, başkalarının ne düşüneceğini dikkate almam
383	 İnsanlar çoğu zaman beni hayal kırıklığına uğratırlar
384	 Kendimle ilgili her şeyi anlatabileceğim hiç kimse yok
385	 Şimşek çakması da korkularımdan biridir
386	 Çok tertipli ve titizim
387	 Ailem her davranışıma fazla karışıyor
388	 Karanlıkta yalnız kalmaktan korkarım
389	 Tasarlamış olduğum planlar çok defa o kadar güçlüklerle dolu göründü ki bunlardan vazgeçmek zorunda kaldım
390	 Birinin hatasını önleme gayretimin yanlış anlaşılmasına çok üzülürüm
391	 Dansa gitmeyi severim
392	 Fırtınadan çok korkarım
393	 Yük çekmeyen atlar dövülmeli ya da kamçılanmalıdır
394	 Başkalarına sık sık akıl danışırım
395	 Gelecek, bir insanın planlar yapamayacağı kadar belirsizdir
396	 İşler yolunda gittiği zaman bile çoğu kez her şeye karşı bir aldırmazlık içinde olduğumu hissederim
397	 Bazen güçlükler öylesine üst üste gelir ki onlarla baş edemeyecekmişim gibi hissederim
398	 Çoğu kez "keşke tekrar çocuk olsaydım" diye düşünürüm
399	 Kolay kolay kızmam
400	 Eğer bana fırsat verilse dünya için çok yararlı işler yapabilirim
401	 Sudan hiç korkmam
402	 Ne yapacağıma karar vermeden önce uzun uzun düşünürüm
403	 Çok şeylerin olup bittiği bu devirde yaşamak hoş bir şey
404	 hatalarını düzelterek kendilerine yardım etmeye çalıştığım insanlar amacımı çoğu kez yanlış anlarlar
405	 Yutkunmakta güçlük çekmem
406	 Uzman dendiği halde benden pek fazla bilgili olmayan insanlarla sıklıkla karşılaşırım
407	 Genel olarak sakinim ve kolay sinirlenmem
408	 Bazı konular hakkında hislerimi o kadar gizleyebilirim ki, insanlar bilmeden beni incitebilirler
409	 Elimde olmadan çok ufak şeyden münakaşa çıkarıp karşımdakini kırıyorum
410	 Madrabazı kendi silahı ile alt etmekten hoşlanırım
411	 İyi tanıdığım bir kimsenin başarısını duyduğum zaman adeta kendimi başarısızlığa uğramış hissederim
412	 hastalık yüzünden doktora gitmekten korkmam
413	 Günahlarım için ne kadar ağır ceza görsem iyidir
414	 hayal kırıklıklarını o kadar ciddiye alırım ki bunları zihnimden söküp atamam
415	 Fırsat verilse iyi bir önder olurum
416	 Yakınlarımın sağlığından çok endişe ederim
417	 Sırada beklerken biri önüme geçmeye kalkışırsa ona çıkışırım
418	 Bazen hiçbir işe yaramadığımı düşünürüm
419	 Küçükken okuldan sık sık kaçardım
420	 Başımdan din ile ilgili olağanüstü yaşantılar geçti
421	 Ailemde çok sinirli insanlar var
422	 Ailemden bazı kişilerin yapmış olduğu bazı işler beni utandırmıştır
423	 Balık tutmayı çok severim
424	 hemen her zaman açlık duyarım
425	 Sık sık rüya görürüm
426	 Kaba ya da can sıkıcı insanlara karşı bazen sert davrandığım olur
427	 Açık saçık hikayelerden utanıp rahatsız olurum
428	 Gazetelerin baş yazılarını okumaktan hoşlanırım
429	 Ciddi konular üzerinde verilen konferansları dinlemekten hoşlanırım
430	 Karşı cinsten olanları çekici bulurum
431	 Başa gelebilecek talihsizlikler beni oldukça telaşlandırır
432	 Kuvvetli siyasi fikirlerim vardır
433	 Bir zamanlar hayali arkadaşlarım vardı
434	 Otomobil yarışçısı olmayı isterdim
435	 Genel olarak kadınlarla çalışmayı tercih ederim
436	 İnsanlar genel olarak başkalarının haklarına saygı göstermekten çok kendi haklarına saygı gösterilmesini isterler
437	 Kanuna aykırı davranmadan, kanunun bir gediğinden yararlanmakta zarar yoktur
438	 Bazı insanlardan o kadar nefret ederim ki ettiklerini bulunca içimden oh derim
439	 Beklemek zorunda kalmak beni sinirlendirir
440	 Başkalarına anlatmak için hoş fıkraları hatırımda tutmaya çalışırım
441	 Uzun boylu kadınlardan hoşlanırım
442	 Üzüntü yüzünden uyuyamadığım zamanlar oldu
443	 Başkalarının gereği gibi yapamadığımı sandığı şeyleri yapmaktan vazgeçtiğim oldu
444	 Başkalarının cahilce inançlarını düzeltmeye çalışmam
445	 Küçükken heyecan veren şeyler yapmaktan hoşlanırdım
446	 Az para ile oynanan kumardan hoşlanırım
447	 Mastürbasyonda kendi cinsimle ilgili hayal beni tahrik eder
448	 Sokakta, otobüs ve dükkanda bana bakan insanlardan rahatsız olurum
449	 İnsanlarla bir arada olmayı sağladığı için toplantı ve davetleri severim
450	 Kalabalığın verdiği coşkudan hoşlanırım
451	 Neşeli arkadaşlar arasına karışınca üzüntülerimi unuturum
452	 Arkadaş edinemiyorum
453	 Küçükken mahalledeki arkadaş ya da akran gruplarına katılmaktan hoşlanmazdım
454	 Orman ya da dağdaki bir kulübede tek başıma yaşamaktan mutlu olabilirdim
455	 İçinde bulunduğum grubun dedikodularına ve konuşmalarına sıklıkla konu olmam
456	 İnsan makul bulmadığı kanunlara aykırı hareketlerinden dolayı cezalandırılmamalıdır
457	 Bence insan hiçbir zaman alkollü bir içkiyi ağzına almamalıdır
458	 Çocukken benimle en fazla ilgilenen erkek baba, üvey baba vb bana karşı çok sert davranırdı
459	 Çaba göstermekle yenemeyeceğimi bildiğim bazı kötü alışkanlıklarım var
460	 Az içki kullandım ya da hiç kullanmadım
461	 Kısa bir zaman için bile olsa başladığım işi bir kenara bırakmak bana güç gelir
462	 Küçük abdestimi yapmada ya da tutmada güçlük çekmem
463	 Sek sek oyunu oynamaktan hoşlanırdım
464	 hiç hayal görmedim
465	 Bir kaç kez hayatım boyunca yaptığım işte hevesimi yitirdiğim olmuştur
466	 Doktor önerisi dışında hiçbir ilaç ya da uyku ilacı kullanmadım
467	 Çok defa (otomobil plaka numarası gibi) hiç önemi olmayan numaraları ezberledim
468	 Sıklıkla sinirli ve asık suratlı olurum
469	 Onlardan önce düşündüğüm için başkaları, benim fikirlerimi kıskanıyorlar
470	 Cinsiyetle ilgili şeylerden nefret ederim
471	 Okulda, hal ve gidişten kırık not alırdım
472	 Yangın karşısında büyülenmiş gibi olurum
473	 Mümkün olduğu kadar kalabalıktan uzak kalmaya çalışırım
474	 Başkalarından daha sık abdeste çıkmam
475	 Sıkıştırıldığım zaman gerçeğin ancak bana zarar vermeyecek kısmını söylerim
476	 Tanrı bana özel bir görev vermiştir
477	 Arkadaşlarımla birlikte işlediğim bir suçtan eşit şekilde suçlu olduğum zaman onları ele vermektense bütün suçu üzerime almayı tercih ederim
478	 Çok daha değişik bir aile ortamından gelmiş olmayı isterdim
479	 Yabancılarla tanışmaktan kaçınmam
480	 Karanlıktan çok defa korkarım
481	 Bir şeyden kurtulmak için hasta numarası yaptığım olmuştur
482	 Trende,otobüste vb rastladığım kimselerle çok defa konuşurum
483	 Peygamberimiz göğe çıkma gibi mucizeler göstermiştir
484	 homoseksüelliği çok iğrenç bulurum
485	 Bir erkek bir kadınla beraber olunca genel olarak onun cinsiyetiyle ilgili şeyler düşünür
486	 İdrarımda hiçbir zaman kan görmedim
487	 Uğraştığım iş yolunda gitmeyince hemen vazgeçerim
488	 Sık sık dua ederim
489	 Yaşamı yalnızca üzüntülü,sıkıntılı tarafları ile benimseyen insanlara sempati duyarım
490	 haftada birkaç kere Kuran okurum
491	 Sadece bir tek dinin doğruluğuna inananlara tahammül edemem
492	 Zelzele düşüncesi beni çok korkutur
493	 Tam dikkat isteyen işleri,beni dikkatsizliğe sürükleyen işlere tercih ederim
494	 Kapalı ve küçük yerlerde bulunmaktan çok rahatsız olurum
495	 Kusurlarını düzeltmeye çalıştığım insanlarla genel olarak gayet açık konuşurum
496	 Eşyayı hiçbir zaman çift görmem
497	 Macera hikayelerinden hoşlanırım
498	 Açık sözlü olmak her zaman iyidir
499	 Gerçekten önemsiz olan bir şey üzerinde bazen sebepsiz olarak haddinden fazla üzüldüğüm olur
500	 Bana parlak gelen bir fikre hemen kapılır giderim
501	 Başkalarından yardım beklemektense genel olarak bir işi kendi başıma yapmayı tercih ederim
502	 herhangi bir olay hakkındaki görüşümü başkalarına açıkça belirtmekten hoşlanırım
503	 Başkalarının hareketlerini çok beğenip beğenmediğimi pek belli etmem
504	 Değersiz gördüğüm ya da acıdığım kimseye bu duygularımı belli etmekten çekinmem
505	 Zaman zaman kendimi öyle güçlü ve enerjik hissederim ki böyle zamanlarda günlerce uykuya ihtiyaç duymadığım olur
506	 Sinirleri çok gergin bir insanım
507	 İşler iyi gidince aslan payını kendilerine alan fakat hata yapılınca bunu başkalarının üzerine atan insanlarla karşılaştım
508	 Koku alma duyum, herkes kadar iyidir
509	 Bazen çekingenliğim yüzünden hakkımı arayamam
510	 Pislik ve kir beni ürkütüp iğrendirir
511	 herkesten gizli tuttuğum bir hayal dünyam var
512	 Yıkanmaktan hoşlanmam
513	 Kış mevsimini severim
514	 Erkek gibi davranan kadınlardan hoşlanırım
515	 Evimizde daima ihtiyaç maddeleri bulunurdu
516	 Ailemde çabuk kızan kimseler var
517	 hiçbir şeyi iyi yapamam
518	 Bazı durumlarda olduğundan daha fazla üzüntülü görünmeye çalıştığım olmuştur
519	 Cinsel organlarımda bir bozukluk var
520	 Genel olarak görüşlerimi kuvvetle savunurum
521	 Bir grup içinde konuşma yapmam ve çok iyi bildiğim bir konuda fikrimi söylemem istenince kaygılanmam
522	 Örümcekten korkmam
523	 Yüzüm hemen hemen hiç kızarmaz
524	 Kapı tokmaklarından hastalık veya mikrop alacağımdan korkmam
525	 Bazı hayvanlardan ürkerim
526	 Gelecek bana ümitsiz görünüyor
527	 Ailem ve yakın akrabalarım birbirleri ile oldukça iyi geçinirler
528	 Yüzüm başkalarından daha sık kızarmaz
529	 Pahalı elbiseler giymeyi isterim
530	 Sebepsiz yere sık sık içim sıkılıyor ve ağlamak istiyorum
531	 Bir konu üzerinde karar verdiğimi zannetsem bile başka biri fikrimi kolayca değiştirebilir
532	 Acıya başkaları kadar ben de dayanabilirim
533	 Sık sık geğirmekten şikayetim yoktur
534	 Çoğunlukla başladığım işten en son vazgeçen ben olurum
535	 hemen her zaman ağzımda kuruluk olur
536	 Beni acele ettirenlere kızarım
537	 Afrika'da aslan avına çıkmak isterdim
538	 Terzilikten hoşlanabileceğimi sanıyorum
539	 Fareden korkmam
540	 Yüzüme hiç felç inmedi
541	 Cildime ufak bir şeyin dokunmasından çok huylanırım
542	 Şimdiye kadar rengi kapkara büyük abdest yapmadım
543	 haftada birkaç kez, korkunç bir şey olacakmış duygusuna kapılırım
544	 Çoğu zaman yorgunluk hissederim
545	 Bazen aynı rüyayı tekrar tekrar görürüm
546	 Tarih okumaktan hoşlanırım
547	 Toplantı ve kalabalık eğlencelerden hoşlanırım
548	 Elimdeyse açık saçık numaraların yapıldığı eğlence yerlerine gitmem
549	 Karşıma çıkacak güçlüklerden korkar ve kaçarım
550	 Kapı mandallarını onarmaktan hoşlanırım
551	 Bazen başkalarının kafamın içindekilerini okuduğundan eminim
552	 Bilimsel yayınları okumaktan hoşlanırım
553	 Açık yerlerde ya da geniş meydanlarda tek başıma kalmaktan korkarım
554	 Sıkıntım oldukça alkol alırım
555	 Bazen çıldıracakmış gibi olurum
556	 Kılık kıyafetime çok itina ederim
557	 hayatı fazla ciddiye almıyorum
558	 Birçok kimseler kötü cinsel faaliyetlerinden dolayı suçludurlar
559	 Gece yarısı çoğunlukla korkuya kapıldığım olur
560	 Bir şeyi nereye koyduğumu unutmaktan çok şikayetçiyim
561	 Ailem benim için büyük bir dayanaktır
562	 Çocukken en fazla bağlandığım ve hayran kaldığım kimse bir kadındı
563	 Macera hikayelerini aşk hikayelerinden daha çok severim
564	 Yapmak istediğim fakat başkalarının beğenmediği bir işten kolayca vazgeçerim
565	 Yüksek bir yerde iken içimden atlama isteği gelir
566	 Sinemalarda aşk sahnelerini severim
"""

# Soruları parse et
lines = questions_text.strip().split('\n')
questions = []
for line in lines:
    if line.strip():
        parts = line.split('\t', 1)
        if len(parts) == 2:
            q_id = int(parts[0].strip())
            q_text = parts[1].strip()
            questions.append({
                "id": q_id,
                "text": q_text,
                "options": [
                    {"value": 1, "label": "Doğru"},
                    {"value": 2, "label": "Yanlış"},
                    {"value": 0, "label": "Boş"}
                ]
            })

# Ölçek tanımlamaları
scales = {
    "L": {
        "name": "Yalan Ölçeği (Lie Scale)",
        "description": "Kendini olduğundan daha iyi gösterme eğilimini ölçer",
        "questionIds": [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 195, 225, 255, 285],
        "scoringA": [],
        "scoringB": [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 195, 225, 255, 285]
    },
    "F": {
        "name": "Geçerlilik Ölçeği (Validity Scale)",
        "description": "Test alma tutumunu ve nadir verilen cevapları değerlendirir",
        "questionIds": [14, 23, 27, 31, 34, 35, 40, 42, 48, 49, 50, 53, 56, 66, 85, 121, 123, 139, 146, 151, 156, 168, 184, 197, 200, 202, 205, 206, 209, 210, 211, 215, 218, 227, 245, 246, 247, 252, 256, 269, 275, 286, 291, 293, 17, 20, 54, 65, 75, 83, 112, 113, 115, 164, 169, 177, 185, 196, 199, 220, 257, 258, 272, 276],
        "scoringA": [14, 23, 27, 31, 34, 35, 40, 42, 48, 49, 50, 53, 56, 66, 85, 121, 123, 139, 146, 151, 156, 168, 184, 197, 200, 202, 205, 206, 209, 210, 211, 215, 218, 227, 245, 246, 247, 252, 256, 269, 275, 286, 291, 293],
        "scoringB": [17, 20, 54, 65, 75, 83, 112, 113, 115, 164, 169, 177, 185, 196, 199, 220, 257, 258, 272, 276]
    },
    "K": {
        "name": "Düzeltme Ölçeği (Correction Scale)",
        "description": "Savunuculuk ve kendini saklama eğilimini ölçer",
        "questionIds": [96, 30, 39, 71, 89, 124, 129, 134, 138, 142, 148, 160, 170, 171, 180, 183, 217, 234, 267, 272, 296, 316, 322, 374, 383, 397, 398, 406, 461, 502],
        "scoringA": [96],
        "scoringB": [30, 39, 71, 89, 124, 129, 134, 138, 142, 148, 160, 170, 171, 180, 183, 217, 234, 267, 272, 296, 316, 322, 374, 383, 397, 398, 406, 461, 502]
    },
    "HS": {
        "name": "Hipokondri (Hypochondriasis)",
        "description": "Bedensel şikayetler ve sağlık kaygısı",
        "questionIds": [23, 29, 43, 62, 72, 108, 114, 125, 161, 189, 273, 2, 3, 7, 9, 18, 51, 55, 63, 68, 103, 130, 153, 155, 163, 175, 188, 190, 192, 230, 243, 274, 281],
        "scoringA": [23, 29, 43, 62, 72, 108, 114, 125, 161, 189, 273],
        "scoringB": [2, 3, 7, 9, 18, 51, 55, 63, 68, 103, 130, 153, 155, 163, 175, 188, 190, 192, 230, 243, 274, 281],
        "kCorrection": "K+5"
    },
    "D": {
        "name": "Depresyon (Depression)",
        "description": "Depresif duygudurum, umutsuzluk, karamsarlık",
        "questionIds": [5, 13, 23, 32, 41, 43, 52, 67, 86, 104, 130, 138, 142, 158, 159, 182, 189, 193, 236, 259, 2, 8, 9, 18, 30, 36, 39, 46, 51, 57, 58, 64, 80, 88, 89, 95, 98, 107, 122, 131, 145, 152, 153, 154, 155, 160, 178, 191, 207, 208, 233, 241, 242, 248, 263, 270, 271, 272, 285, 296],
        "scoringA": [5, 13, 23, 32, 41, 43, 52, 67, 86, 104, 130, 138, 142, 158, 159, 182, 189, 193, 236, 259],
        "scoringB": [2, 8, 9, 18, 30, 36, 39, 46, 51, 57, 58, 64, 80, 88, 89, 95, 98, 107, 122, 131, 145, 152, 153, 154, 155, 160, 178, 191, 207, 208, 233, 241, 242, 248, 263, 270, 271, 272, 285, 296]
    },
    "HY": {
        "name": "Histeri (Hysteria)",
        "description": "Stres karşısında fiziksel semptomlara yönelme",
        "questionIds": [10, 23, 32, 43, 44, 47, 76, 114, 179, 186, 189, 238, 253, 2, 3, 6, 7, 8, 9, 12, 26, 30, 51, 55, 71, 89, 93, 103, 107, 109, 124, 128, 129, 136, 137, 141, 147, 153, 160, 162, 163, 170, 172, 174, 175, 180, 188, 190, 192, 201, 213, 230, 234, 243, 265, 267, 274, 279, 289, 292],
        "scoringA": [10, 23, 32, 43, 44, 47, 76, 114, 179, 186, 189, 238, 253],
        "scoringB": [2, 3, 6, 7, 8, 9, 12, 26, 30, 51, 55, 71, 89, 93, 103, 107, 109, 124, 128, 129, 136, 137, 141, 147, 153, 160, 162, 163, 170, 172, 174, 175, 180, 188, 190, 192, 201, 213, 230, 234, 243, 265, 267, 274, 279, 289, 292]
    },
    "PD": {
        "name": "Psikopati (Psychopathic Deviate)",
        "description": "Sosyal uyumsuzluk, otorite ile sorunlar",
        "questionIds": [16, 21, 24, 32, 33, 35, 38, 42, 61, 67, 84, 94, 102, 106, 110, 118, 127, 215, 216, 224, 239, 244, 245, 284, 8, 20, 37, 82, 91, 96, 107, 134, 137, 141, 155, 170, 171, 173, 180, 183, 201, 231, 235, 237, 248, 267, 287, 289, 294, 296],
        "scoringA": [16, 21, 24, 32, 33, 35, 38, 42, 61, 67, 84, 94, 102, 106, 110, 118, 127, 215, 216, 224, 239, 244, 245, 284],
        "scoringB": [8, 20, 37, 82, 91, 96, 107, 134, 137, 141, 155, 170, 171, 173, 180, 183, 201, 231, 235, 237, 248, 267, 287, 289, 294, 296],
        "kCorrection": "K+4"
    },
    "MF_Erkek": {
        "name": "Erkeklik-Kadınlık (Masculinity-Femininity) - Erkek Formu",
        "description": "Cinsiyet rolü davranış kalıpları - Erkekler için",
        "questionIds": [4, 25, 69, 70, 74, 77, 78, 87, 92, 126, 132, 134, 140, 149, 179, 187, 203, 204, 217, 226, 231, 239, 261, 278, 282, 295, 297, 299, 1, 19, 26, 28, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 133, 144, 176, 198, 213, 214, 219, 221, 223, 229, 249, 254, 260, 262, 264, 280, 283, 300],
        "scoringA": [4, 25, 69, 70, 74, 77, 78, 87, 92, 126, 132, 134, 140, 149, 179, 187, 203, 204, 217, 226, 231, 239, 261, 278, 282, 295, 297, 299],
        "scoringB": [1, 19, 26, 28, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 133, 144, 176, 198, 213, 214, 219, 221, 223, 229, 249, 254, 260, 262, 264, 280, 283, 300]
    },
    "MF_Kadin": {
        "name": "Erkeklik-Kadınlık (Masculinity-Femininity) - Kadın Formu",
        "description": "Cinsiyet rolü davranış kalıpları - Kadınlar için",
        "questionIds": [4, 25, 70, 74, 77, 78, 87, 92, 126, 132, 134, 140, 149, 187, 203, 204, 217, 226, 239, 261, 278, 282, 295, 299, 133, 1, 19, 26, 28, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 144, 176, 198, 213, 214, 219, 221, 223, 229, 249, 254, 260, 262, 264, 280, 283, 300, 69, 179, 231, 297],
        "scoringA": [4, 25, 70, 74, 77, 78, 87, 92, 126, 132, 134, 140, 149, 187, 203, 204, 217, 226, 239, 261, 278, 282, 295, 299, 133],
        "scoringB": [1, 19, 26, 28, 79, 80, 81, 89, 99, 112, 115, 116, 117, 120, 144, 176, 198, 213, 214, 219, 221, 223, 229, 249, 254, 260, 262, 264, 280, 283, 300, 69, 179, 231, 297]
    },
    "PA": {
        "name": "Paranoya (Paranoia)",
        "description": "Kuşkuculuk, güvensizlik, zulüm fikirleri",
        "questionIds": [15, 16, 22, 24, 27, 35, 110, 121, 123, 127, 151, 157, 158, 202, 275, 284, 291, 293, 299, 305, 317, 338, 341, 364, 365, 93, 107, 109, 111, 117, 124, 268, 281, 294, 313, 316, 319, 327, 347, 348],
        "scoringA": [15, 16, 22, 24, 27, 35, 110, 121, 123, 127, 151, 157, 158, 202, 275, 284, 291, 293, 299, 305, 317, 338, 341, 364, 365],
        "scoringB": [93, 107, 109, 111, 117, 124, 268, 281, 294, 313, 316, 319, 327, 347, 348]
    },
    "PT": {
        "name": "Psikasteni (Psychasthenia)",
        "description": "Anksiyete, obsesif düşünceler, kompulsif davranışlar",
        "questionIds": [10, 15, 22, 32, 41, 67, 76, 86, 94, 102, 106, 142, 159, 182, 189, 217, 238, 266, 301, 304, 305, 317, 321, 336, 337, 340, 342, 343, 344, 346, 349, 351, 352, 356, 357, 358, 359, 360, 361, 3, 8, 36, 122, 152, 164, 178, 329, 353],
        "scoringA": [10, 15, 22, 32, 41, 67, 76, 86, 94, 102, 106, 142, 159, 182, 189, 217, 238, 266, 301, 304, 305, 317, 321, 336, 337, 340, 342, 343, 344, 346, 349, 351, 352, 356, 357, 358, 359, 360, 361],
        "scoringB": [3, 8, 36, 122, 152, 164, 178, 329, 353],
        "kCorrection": "K+1"
    },
    "SC": {
        "name": "Şizofreni (Schizophrenia)",
        "description": "Tuhaf düşünceler, sosyal izolasyon, realite testinin zayıflaması",
        "questionIds": [15, 16, 21, 22, 24, 33, 35, 38, 40, 41, 47, 52, 76, 97, 104, 121, 156, 157, 159, 168, 179, 182, 194, 202, 210, 238, 241, 251, 259, 266, 273, 282, 291, 297, 301, 303, 305, 307, 312, 320, 324, 325, 332, 334, 335, 339, 341, 345, 349, 350, 352, 354, 355, 356, 360, 363, 364, 32, 212, 8, 17, 20, 37, 65, 103, 119, 177, 178, 187, 192, 196, 220, 276, 281, 306, 309, 322, 330],
        "scoringA": [15, 16, 21, 22, 24, 33, 35, 38, 40, 41, 47, 52, 76, 97, 104, 121, 156, 157, 159, 168, 179, 182, 194, 202, 210, 238, 241, 251, 259, 266, 273, 282, 291, 297, 301, 303, 305, 307, 312, 320, 324, 325, 332, 334, 335, 339, 341, 345, 349, 350, 352, 354, 355, 356, 360, 363, 364, 32, 212],
        "scoringB": [8, 17, 20, 37, 65, 103, 119, 177, 178, 187, 192, 196, 220, 276, 281, 306, 309, 322, 330],
        "kCorrection": "K+1"
    },
    "MA": {
        "name": "Hipomani (Hypomania)",
        "description": "Aşırı enerji, düşünce uçması, ajitasyon",
        "questionIds": [11, 13, 21, 22, 59, 64, 73, 97, 100, 109, 127, 134, 143, 156, 157, 167, 181, 194, 212, 222, 226, 228, 232, 233, 238, 240, 250, 251, 263, 266, 268, 271, 277, 279, 298, 101, 105, 111, 119, 120, 148, 166, 171, 180, 267, 289],
        "scoringA": [11, 13, 21, 22, 59, 64, 73, 97, 100, 109, 127, 134, 143, 156, 157, 167, 181, 194, 212, 222, 226, 228, 232, 233, 238, 240, 250, 251, 263, 266, 268, 271, 277, 279, 298],
        "scoringB": [101, 105, 111, 119, 120, 148, 166, 171, 180, 267, 289],
        "kCorrection": "K+2"
    },
    "SI": {
        "name": "Sosyal İçedönüklük (Social Introversion)",
        "description": "Sosyal geri çekilme, utangaçlık, içedönüklük",
        "questionIds": [32, 67, 82, 111, 117, 124, 138, 147, 171, 172, 180, 201, 236, 267, 278, 292, 304, 316, 321, 332, 336, 342, 357, 377, 383, 398, 411, 427, 436, 455, 473, 487, 549, 564, 25, 33, 57, 91, 99, 119, 126, 143, 193, 208, 229, 231, 254, 262, 281, 296, 309, 353, 359, 371, 391, 400, 415, 440, 446, 449, 450, 451, 462, 469, 479, 481, 482, 505, 521, 547],
        "scoringA": [32, 67, 82, 111, 117, 124, 138, 147, 171, 172, 180, 201, 236, 267, 278, 292, 304, 316, 321, 332, 336, 342, 357, 377, 383, 398, 411, 427, 436, 455, 473, 487, 549, 564],
        "scoringB": [25, 33, 57, 91, 99, 119, 126, 143, 193, 208, 229, 231, 254, 262, 281, 296, 309, 353, 359, 371, 391, 400, 415, 440, 446, 449, 450, 451, 462, 469, 479, 481, 482, 505, 521, 547]
    }
}

# JSON yapısını oluştur
mmpi_data = {
    "testName": "Minnesota Çok Yönlü Kişilik Envanteri (MMPI)",
    "testCode": "MMPI",
    "version": "Türkçe Uyarlama",
    "description": "MMPI, kişilik özellikleri ve psikopatolojileri değerlendirmek için kullanılan 566 soruluk kapsamlı bir kişilik testidir. Test, birden fazla klinik ölçek ve geçerlilik ölçeği içerir.",
    "totalQuestions": 566,
    "questions": questions,
    "scales": scales,
    "scoring": {
        "method": "Her ölçek için ham puanlar hesaplanır. Ölçek A soruları için 'Doğru' (1) cevapları, Ölçek B soruları için 'Yanlış' (2) cevapları puan olarak sayılır. Bazı ölçeklere K düzeltmesi uygulanır (HS+5K, PD+4K, PT+1K, SC+1K, MA+2K). Ham puanlar, cinsiyete göre T-puanlarına dönüştürülür (M=50, SD=10).",
        "responseFormat": "1 = Doğru, 2 = Yanlış, 0 = Boş (Geçersiz)",
        "validityNote": "30'dan fazla boş cevap testin geçerliliğini sorgulatabilir.",
        "tScoreInterpretation": {
            "below30": "Çok düşük - Testin geçerliliğini sorgulayın",
            "30-40": "Düşük",
            "40-60": "Normal aralık",
            "60-70": "Orta derecede yüksek - Klinik önem taşıyabilir",
            "70-80": "Yüksek - Klinik olarak anlamlı",
            "above80": "Çok yüksek - Ciddi psikopatoloji göstergesi olabilir"
        }
    },
    "instructions": "Doğru için '1', Yanlış için '2', Boş için '0' yazınız. Mümkün olduğunca sorulara cevap veriniz. 30 boş (0) cevaptan sonra testin sonuçlarının doğruluğunu anlamak mümkün olmamaktadır. Olabildiğince 1 veya 2 işareti koymaya çalışınız.",
    "reference": "Hathaway, S. R., & McKinley, J. C. (1943). The Minnesota Multiphasic Personality Inventory. Minneapolis: University of Minnesota Press."
}

# JSON dosyasına kaydet
with open('/home/ubuntu/mmpi_test.json', 'w', encoding='utf-8') as f:
    json.dump(mmpi_data, f, ensure_ascii=False, indent=2)

print("MMPI testi başarıyla JSON formatına dönüştürüldü!")
print(f"Toplam soru sayısı: {len(questions)}")
print(f"Toplam ölçek sayısı: {len(scales)}")
