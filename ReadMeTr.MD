Kullandığım kütüphaneleri buradaki komut ile indirebilirsiniz : pip install sounddevice sciPy

FindMax kütüphanesinde peak noktası bulunuyor.

Switch string içindeki stringler ses arrayi ile aynı sırada ikisini beraber değiştirmeyi unutmayın

Ses kayıt sample rate'ini veya kaydetme süresini fs ve seconds değişkenleri ile değiştirebilirsiniz.

35. satırdaki dtype'ı değiştirerek kaydın tipini değiştirebilirsiniz.

Write'ın içindeki output ismini değiştirerek kaydettiğiniz sesin ismini değiştirebilirsiniz.

Read değişkeni ile sample alabilirsiniz.

En sondaki print'i değiştirerek en son çıktıyı değiştirebilirsiniz

En sonda çıkan değerler kaydettiğiniz ses ile kayıtlı sesler arasındaki öklid uzaklığını ölçüyor.

For'un içindeki print'i silerek sadece tahmini görebilirsiniz.

### TL;DR : soundDivice kütüphanesiyle sesi kaydedip wavfile kütüphanesi ile sample alıp peak noktalarından sesi tanımaya çalıştım.

FindMax( Array int ) : Find max kütüphanesi verilen arrayin (örneğin sesElma) içindeki peak noktayı buluyor. 
Program şu anda tek peak nokası buluyor fakat bu fonksiyonun içini değiştirerek bu sayı arttırılabilir. Max tepenin x ve y değerlerini döndürüyor.

SwitchToString( int ) : sadece girilen değere karşılık gelen string ismini söyleyen switch case fonskiyonu. En sonda çıktı alırken kullandım

Sample rate’i 44100 alarak kendi sesimi 1 saniye uzunluğunda kaydettim. Değerleri int16 değerinde kaydettim.

Kaydetmiş olduğum 10 kelimeyi ayrı ayrı read fonksiyonu ile örnekledim. Ardından her birini bir değişkene atadım (sesFoo, sesBar) 
sonra bunları tekrardan ses arrayine atadım ve jagged array yaptım.

10 kere çalışacak bir for döngüsü oluşturdum. 0 dan başlayarak ses arrayinin içindeki değişkenlerin 
peak noktasını mevcut kaydedilen ses dosyasının peak noktasıyla Öklid teoremi kullanarak karşılaştırıyor.
En küçük değeri minRangeToRecorded’e ve hangi index olduğunu tempHolder’a kaydettikten sonra döngüden çıkıyor ve print ediyor.

Test sonuçları : Kod tek peak noktası ve az kontrol yaptığım için fazla verimli çalışmıyor. 
Ses kaydına başlama ve bitiş süreleri, birden fazla peak noktası ve bir kelime için birden fazla kayıt kullanılarak verimlilik yükseltilebilir.
 
