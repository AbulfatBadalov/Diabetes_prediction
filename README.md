# Diabetes_prediction

🩺 Diyabet Tahmin Uygulaması (Streamlit + SVM)
Badalov Abulfat tarafından geliştirilen bu proje, Pima Indians Diabetes Dataset kullanarak bir Support Vector Machine (SVM) modeli ile diyabet tahmini yapmaktadır. Uygulama, kullanıcıdan alınan medikal verilerle kişide diyabet riski olup olmadığını tahmin eder ve sonucu görsel olarak sunar.

🚀 Proje Özellikleri
Kullanıcı dostu arayüz: Streamlit ile geliştirilen modern ve etkileşimli bir uygulama.

Diyabet tahmini: Kullanıcıdan alınan 8 farklı medikal veri ile anlık tahmin yapılır.

Eğitilmiş model kullanımı: svm_diabetes_model.pkl dosyası ile tahminler yapılır.

Hızlı kurulum: Adım adım kolay kurulum ve kullanım.

🧰 Gereksinimler
Bu projeyi çalıştırabilmek için aşağıdaki yazılım ve kütüphanelerin yüklü olması gerekmektedir:

Python 3.x

Streamlit

Scikit-learn

Pandas

NumPy

Joblib

⚙️ Kurulum Adımları
1. Projeyi Klonlayın
İlk olarak, projeyi yerel bilgisayarınıza klonlayın:

bash
Copy
Edit
git clone https://github.com/badalov-abulfat/diabetes-predictor-app.git
cd diabetes-predictor-app
2. Gerekli Kütüphaneleri Yükleyin
Proje için gerekli olan Python kütüphanelerini yüklemek için:

bash
Copy
Edit
pip install -r requirements.txt
3. Model Dosyasını Ekleyin
Eğitilmiş modeli (svm_diabetes_model.pkl) projenin ana dizinine ekleyin. Bu dosya modelin tahmin yapabilmesi için gereklidir.

4. Uygulamayı Başlatın
Streamlit uygulamasını başlatmak için:

bash
Copy
Edit
streamlit run app.py
Uygulama, tarayıcınızda otomatik olarak açılacaktır.

🔧 Kullanıcı Arayüzü
Uygulama, kullanıcıdan aşağıdaki bilgileri alarak diyabet riski tahmini yapmaktadır:

Gebelik sayısı

Glikoz seviyesi

Kan basıncı

Deri kalınlığı

İnsülin seviyesi

Vücut Kitle İndeksi (BMI)

Diabetes Pedigree Function (genetik etki)

Yaş

🖼️ Örnek Ekran Görüntüsü:
Burada, kullanıcı arayüzü ile ilgili bir örnek ekran görüntüsü yer alabilir. (Ekran görüntüsünü eklemek isteyebilirsiniz.)

📊 Model Performansı
Doğruluk (Accuracy): Modelin eğitim verileri üzerinde sağladığı doğruluk oranı ~%X.

Confusion Matrix: Modelin doğruluk, yanlış pozitif, yanlış negatif gibi istatistikleri.

Classification Report: Precision, recall, F1-score gibi detaylı metrikler.

📁 Dosya Yapısı
Projede kullanılan dosya yapısı aşağıdaki gibi olacaktır:

bash
Copy
Edit
├── app.py                    # Streamlit uygulaması
├── diabetes.csv              # Eğitim verisi (CSV formatında)
├── svm_diabetes_model.pkl    # Eğitilmiş model dosyası
├── README.md                 # Proje açıklaması (bu dosya)
└── requirements.txt          # Gerekli kütüphaneler
📚 Proje Hakkında
Diyabet Tahmin Uygulaması, Pima Indians Diabetes veri seti üzerinde eğitilmiş bir SVM (Support Vector Machine) modeli kullanarak bireylerin diyabet riskini tahmin eder. Kullanıcı, yaş, glikoz seviyesi, vücut kitle indeksi gibi sağlık verilerini girer ve model, diyabet riski hakkında bir tahminde bulunur.

Model, sklearn'ün SVM algoritması kullanılarak eğitilmiştir ve kullanıcı dostu bir Streamlit uygulaması ile erişilebilir hale getirilmiştir.

📧 İletişim
Proje hakkında daha fazla bilgi almak veya katkı sağlamak için aşağıdaki iletişim bilgilerini kullanabilirsiniz:

E-posta: [e-posta adresiniz]

GitHub: [GitHub profiliniz]

🎯 Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, aşağıdaki adımları takip edebilirsiniz:

Repo'yu forklayın.

Yeni bir özellik ekleyin veya hata düzeltin.

Değişikliklerinizi pull request (PR) olarak gönderin.

Not: Bu proje, bir diyabet teşhisi aracı değildir ve sadece eğitim ve araştırma amaçlıdır.
