from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<!DOCTYPE html><html><head><title>Teknoloji Bağımlılığı</title></head><body><h1>Sosyal Medya Bağımlılığı</h1> <p>Sosyal medya, gerçek dünyada geçirdiğimiz zamanı azaltır. Ayrıca sürekli güncellemeler ve gönderilerle zihinlerimizi koşullandırır, bu da uzun vadede stresli hale gelebilir.</p><img width="450px" src="https://1.bp.blogspot.com/-aLBGw_ocK6Y/X1GIyVTzZzI/AAAAAAAABic/Ypm0hDSh09IKC7r5NG8gJ6ZN3kZj9sXlgCLcBGAsYHQ/s1280/sosyal-medya-ba%25C4%259F%25C4%25B1ml%25C4%25B1l%25C4%25B1%25C4%259F%25C4%25B1.jpg"><h2>Bu durumla nasıl başa çıkabiliriz?</h2><ul><li>Çevrimiçi/cevrimdışı harcanan zaman için sınırlar belirleyebiliriz </li>  <li>Rahatlamak ve dinlenmek için teknolojiden uzak bazı aktivitelerde bulunabilirsiniz.</li></ul> <iframe width="560" height="315" src="https://www.youtube.com/embed/C8eIxrkcXfs?si=AKTZ2lej8vfO2JJ1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><a href="/rastgele gerçekler">Rastgeele Gerçekler İçin Tıklayın!</a></body></html>'

@app.route("/rastgele gerçekler")
def rg ():
    gercekler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
                "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
                "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
                "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
                "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
                "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
                "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
                "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."]
    return f'<p>{random.choice(gercekler)}</p>'    

@app.route("/bagimlilik-yapan-seyler")
def bys ():
    bagimlilik_yapan_seyler = ["tütün",
                               "alkol",
                                "kokain",
                                "bonzai",
                                "sigara", 
                                "fazla teknolonojik aletlere bakmak"]
                

    return f'<p>{random.choice(bagimlilik_yapan_seyler)}</p>'
app.run(debug=True)