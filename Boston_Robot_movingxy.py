#AÇIKLAMALAR :(Bu açıklamalarda başta kendim olmak üzere, benim gibi olanların iç sesini yansıtmaya çalıştım)
# BOSTON DYNAMİCS robot sorusu. robot ilk başladığı yerden ne kadar uzakta.
# Bu tür sorularda ilk olarak bulunduğumuz başlangıç noktasını referans almamız gerekiyor.
#Ben X VE Y koordinatında neredeyim. right giderken + , left gittiğim kadar - , up  kadar +
# down kadar y ekseninde  -  işlemi  yapıyorum. ardından x ve y toplama işlemi yapıyorum, konumu buluyorum.
# işlemleri yaparken özellikle LİST kullanıyorum. listenin index alma rahatlığı bana işlemlerimde kolaylık sağlıyor.
# daha rahat for döngüsüne sokabiliyorum. ekleme çıkarma, parçalara ayırma, birleştirme ve sayısaıllaştırma işlemi kolay oluyor.
# Burada şunu söylemek istiyorum.soruyu, problemi görünce kafamızda ilk olarak bu soruyu çözmek için  liste mi, tuple mı
# dict. veya set mi kullanmalıyım ın şekillenmesi gerekiyor. Bunun için de çok soru çözüp, "hangi durumda ne yaparım" ın
# meleke haline gelmesi gerekiyor. veya genel bir metodlaştırma işlemi yaparak; "şu durumlarda şunu tercih et" şeklinde
# bir çalışma yapılması gerekiyor. Bunu orta vadede yapacağım!!!!!!belki bunu benden önce düşünüp yapmış olan vardır.ben bulamadım.
#
# ------------------------şimdi soruyu irdeleyelim--- spesifik açıklamalar adım adım yanlarındadır.--------------


x=y=0  # önce başlangıç noktasını tanımladım.robot süpürgelere de önce odayı tanıtıyoruz.
# böylece sürekli x ve y koordinatında mesafe ölçerek konumunu buluyor.

command =["right 20", "right 30", "left 50", "up 10", "down 20"] # komutları liste şeklinde girdik. evirip çevirmek kolay olsun.
# index leyip for içinde teker teker kullanıcam. burda problem şu. sayıları nasıl alıp işlem yaptırıcam.????

for i in range(len(command)) : # liste içindeki elementleri len ile saydırıyoruz indexliyoruz.Bana nedense bu kısmı çok zevkli geliyor.
# index 0= "right 20", index 1= "right 30",.......tamam güzel de. içinden sayıyı çekip nasıl işlem yaptırıcam.
    if command[i].startswith("r"): x=  x + int(command[i].split()[1]) # dananın, yarısı kopan kuyruğunun tamamı kopuyor.
# eger index 0 dan 5 e kadar dönerken ilk harfi "r" ile başlıyorsa şöyle yap diyor. x diye bir değişken ata. bunu kümülatif toplat.
# ancak, "right 20" string malum. bunu split le iki parçaya ayır.Oluşan 0 ve 1 indexinin, 1 inci indexi olan sayıyı yani 20 yi int yap ve
# gönlünce aritmatik işlem yaptır. Bu işlemi düşünmek kolay değil ilk seferde ama buradan devam ederek bu soruyu açabiliriz, derinleşebiliriz.
    elif command[i].startswith("l"): x = x - int (command[i].split ()[1])
    elif command[i].startswith ("u"): y = y + int (command[i].split ()[1]) # yukarıdaki işlemi y ekseni içinde yapıyor.
    elif command[i].startswith ("d"): y = y - int (command[i].split ()[1])

print([x,y]) #BİTTİ GİTTİ...!!!!!! cevabını bildiğin soruyu çözmesi kolay tabiiii!!!!!!
# siz de cevabını bildiğiniz soruya açıklama getirerek, herkese daha fazla yardımcı olabilirsiniz. !!

